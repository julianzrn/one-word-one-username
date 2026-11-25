"""Entry for make.fun bounty: One Word, One Username, One Reward.

Writes the entry username to /output/entry.txt with no trailing newline.
The entrant's own make.fun username and nothing else, at most 30 characters.
"""

from pathlib import Path

ENTRY_TEXT = "nimble-finch-92-9082"

OUTPUT_PATH = Path("/output/entry.txt")


def render_entry() -> bytes:
    """Return the entry encoded exactly as it will be stored."""
    return ENTRY_TEXT.encode("utf-8")


def write_entry() -> None:
    """Write the entry text to the output file exactly as specified."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(render_entry())


if __name__ == "__main__":
    write_entry()
