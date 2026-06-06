"""DecodeLabs Project 1: Rule-Based AI Chatbot."""

import argparse
import re
import sys

from responses import EXIT_SENTINEL, get_response

WELCOME = """========================================
  DecodeLabs | Project 1: Rule-Based Bot
  Batch 2026
========================================
Type 'help' to see commands, or 'bye' to exit.
"""


def normalize(raw: str) -> str:
    """Prepare user input for matching."""
    text = raw.strip().lower()
    text = re.sub(r"\s+", " ", text)
    text = text.rstrip("!.?")
    return text


def cli_main() -> None:
    print(WELCOME)
    while True:
        try:
            raw = input("You: ")
        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print("\nBot: Goodbye! Thanks for chatting. See you at DecodeLabs.")
            return

        raw = raw.strip()
        if not raw:
            print("Bot: Please type something, or 'bye' to exit.")
            continue

        text = normalize(raw)
        reply = get_response(text)

        if reply == EXIT_SENTINEL:
            print("Bot: Goodbye! Thanks for chatting. See you at DecodeLabs.")
            return

        print(f"Bot: {reply}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="DecodeLabs Project 1: Rule-Based Bot"
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Launch the graphical bot interface",
    )
    args = parser.parse_args()

    if args.gui:
        from gui import run_gui

        run_gui()
    else:
        cli_main()


if __name__ == "__main__":
    main()
