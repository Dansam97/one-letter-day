"""One Letter for Your Day — entry program.

Writes exactly one letter, "U", to entry.txt in the output directory.
The letter stands for the word "unhinged": a day that came off its
hinges — vivid, funny, and true. The gate requires entry.txt to be
UTF-8 text of exactly 1 character, so no trailing newline is written.
"""

import os

ENTRY_TEXT = "U"


def validated_text() -> str:
    """Return the entry text after checking it against the gate.

    The gate requires UTF-8 text of exactly 1 character, not only
    white space, so the entry must be a single letter A to Z.
    """
    text = ENTRY_TEXT
    encoded = text.encode("utf-8")  # raises if not encodable
    if len(text) != 1:
        raise ValueError(f"entry must be exactly 1 character, got {len(text)}")
    if not ("A" <= text <= "Z"):
        raise ValueError(f"entry must be one letter A to Z, got {text!r}")
    if len(encoded) != 1:
        raise ValueError("entry must encode to exactly 1 UTF-8 byte")
    return text


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Read the bytes back and confirm they are exactly the entry letter.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != text.encode("utf-8"):
        raise IOError(f"entry.txt mismatch: wrote {written!r}")


if __name__ == "__main__":
    main()
