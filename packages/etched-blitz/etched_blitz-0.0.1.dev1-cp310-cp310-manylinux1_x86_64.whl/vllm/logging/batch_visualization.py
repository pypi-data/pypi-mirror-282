from collections import deque
from typing import Deque, Dict, Iterable, List, Tuple, Union

from vllm.core.scheduler import ScheduledSequenceGroup
from vllm.outputs import EmbeddingRequestOutput, RequestOutput
from vllm.transformers_utils.detokenizer import Detokenizer


class BatchVisualizer:
    """Logging for how the batches are allocated

    Stores last 8 batches and tokens that were batched inside of it. Different
    colors for different sequences. Useful for seeing how prompts are getting
    processed by Blitz.
    """

    ANSI_COLORS: Dict[str, str] = {
        "green": "\033[38;2;60;168;78m",
        "cyan": "\033[38;2;134;231;235m",
        "blue": "\033[38;2;81;139;255m",
        "magenta": "\033[38;2;255;0;255m",
        "red": "\033[38;2;255;73;58m",
        "orange": "\033[38;2;255;165;0m",
        "yellow": "\033[38;2;234;230;39m",
        "light-green": "\033[38;2;144;238;144m",
        "reset": "\033[0m",
    }

    def __init__(self, detokenizer: Union[Detokenizer, None]) -> None:
        self.current_color: int = 0
        # (color, content)
        self.batches: Deque[List[Tuple[str, str]]] = deque(maxlen=8)
        self.requests: Dict[str, str] = {}
        self.detokenizer: Detokenizer = detokenizer
        self.current_max_batch_size = 0

    def update_state(self,
                     scheduled_seq_groups: Iterable[ScheduledSequenceGroup]):
        current_batch: List[Tuple[str, str]] = []
        for scheduled_seq_group in scheduled_seq_groups:
            seq_group = scheduled_seq_group.seq_group
            request_id = seq_group.request_id
            all_tokens = []
            for seq in seq_group.get_seqs():
                seq_tokens = seq.get_token_ids()
                all_tokens.extend(seq_tokens)

            tokens_added_to_batch = all_tokens[-scheduled_seq_group.
                                               token_chunk_size:]

            seq_tokenizer = self.detokenizer.get_tokenizer_for_seq(
                sequence=seq)
            decoded_tokens = seq_tokenizer.batch_decode(tokens_added_to_batch)

            if request_id in self.requests:
                color = self.requests[request_id]
            else:
                color_keys = [
                    key for key in self.ANSI_COLORS if key != "reset"
                ]
                color = self.ANSI_COLORS[color_keys[self.current_color]]
                self.requests[request_id] = color
                self.current_color = (self.current_color + 1) % len(color_keys)

            batch_items = [(token, color) for token in decoded_tokens]

            current_batch.extend(batch_items)

        self.batches.append(current_batch)
        self.current_max_batch_size = max(
            (len(batch) for batch in self.batches), default=0)

    def drop_finished_requests(
        self,
        request_outputs: List[Union[RequestOutput, EmbeddingRequestOutput]],
    ):
        """Please make sure you call this so it doesn't memory leak"""

        for request_output in request_outputs:
            if request_output.finished:
                del self.requests[request_output.request_id]

    @staticmethod
    def _to_raw_string(string: str) -> str:
        repr_string = repr(string)

        # Check if the string is enclosed in single or double quotes
        if repr_string.startswith(("'", '"')):
            # Remove the first and last character (the enclosing quotes)
            ret_str = repr_string[1:-1]
        else:
            # In case of some very unusual case
            ret_str = repr_string

        truncate_length = 12
        return ((ret_str[:truncate_length - 2] +
                 "..") if len(ret_str) > truncate_length else ret_str)

    def render(self):
        output = ""

        headers = ""
        for i in range(1, 9):
            headers += f"Batch {i:<5}" + " " * 5
        output += headers + "\n" + "─" * (16 * 8) + "\n"

        blank_cell = " " * 16

        for row in range(self.current_max_batch_size):
            row_output = ""
            # Render top ┌--------┐ border for all cells in the row
            for batch in self.batches:
                if row >= len(batch):
                    row_output += blank_cell
                else:
                    content, color = batch[row]
                    row_output += (
                        f"{color}┌{'─' * 14}┐{self.ANSI_COLORS['reset']}")
            row_output += "\n"

            # Render |  content  | for all cents in the row
            for batch in self.batches:
                if row >= len(batch):
                    row_output += blank_cell
                else:
                    content, color = batch[row]

                    content = self._to_raw_string(string=content)
                    row_output += (
                        f"{color}│ {content:<12} │{self.ANSI_COLORS['reset']}")
            row_output += "\n"

            # Render bottom └--------┘ border for all cells in the row
            for batch in self.batches:
                if row >= len(batch):
                    row_output += blank_cell
                else:
                    content, color = batch[row]
                    row_output += (
                        f"{color}└{'─' * 14}┘{self.ANSI_COLORS['reset']}")
            row_output += "\n"

            # In all it should render all cells in the row in this format:
            # ┌---------┐
            # | content |
            # └---------┘

            output += row_output

        print(output)
