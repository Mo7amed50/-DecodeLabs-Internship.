"""DecodeLabs Project 1: Rule-Based AI Chatbot."""

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


def main() -> None:
    print(WELCOME)
    try:
        while True:
            raw = input("You: ").strip()
            if not raw:
                print("Bot: Please type something, or 'bye' to exit.")
                continue

            text = normalize(raw)
            reply = get_response(text)

            if reply == EXIT_SENTINEL:
                print("Bot: Goodbye! Thanks for chatting. See you at DecodeLabs.")
                break

            print(f"Bot: {reply}")

    except KeyboardInterrupt:
        print("\nBot: Interrupted. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
