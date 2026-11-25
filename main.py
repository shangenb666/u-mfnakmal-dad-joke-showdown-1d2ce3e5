"""Write the entry joke for make.fun's "Dad Joke Showdown" bounty.

One dad joke, at most 200 characters, written to be told out loud.
The program writes the joke to entry.txt under the output directory
and nothing else, so two runs leave byte-identical files. It uses only
the standard library and never touches the network.
"""

import os
import sys
from pathlib import Path

JOKE = "My son kept impersonating a flamingo, so I put my foot down \u2014 and he finally did too."


def write_entry() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / "entry.txt"
    if len(JOKE) > 200 or len(JOKE) < 1:
        sys.exit("joke must be 1 to 200 characters")
    if JOKE.strip() == "":
        sys.exit("joke must not be only whitespace")
    output_dir.mkdir(parents=True, exist_ok=True)
    # make.fun collects the outputs as another user than the one the
    # program runs as, so the output must be readable by everyone.
    output_dir.chmod(0o755)
    target.write_text(JOKE, encoding="utf-8")
    target.chmod(0o644)
    return target


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written} ({len(JOKE)} characters)")
