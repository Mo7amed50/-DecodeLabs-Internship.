"""Rule-based response routing using if-elif-else logic."""

import random
from datetime import datetime

EXIT_SENTINEL = "__EXIT__"

GREETINGS = {
    "hi",
    "hello",
    "hey",
    "hiya",
    "good morning",
    "good afternoon",
    "good evening",
    "howdy",
}

EXIT_COMMANDS = {
    "bye",
    "exit",
    "quit",
    "goodbye",
    "see you",
    "see ya",
}

THANKS_PHRASES = {
    "thanks",
    "thank you",
    "thx",
    "ty",
}

NAME_PHRASES = {
    "what is your name",
    "what's your name",
    "who are you",
    "your name",
}

TIME_PHRASES = {
    "time",
    "what time is it",
    "what's the time",
    "current time",
}

DATE_PHRASES = {
    "date",
    "what day is it",
    "what's the date",
    "today's date",
    "todays date",
}

JOKE_TRIGGERS = {
    "joke",
    "tell me a joke",
    "make me laugh",
}

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the Python programmer stay calm? They had good except handling.",
    "I told my computer I needed a break. It said: 'No problem, I'll go to sleep.'",
    "Why do Java developers wear glasses? Because they don't C sharp.",
]

HELP_TEXT = """Here is what I understand:
  Greetings: hi, hello, hey, good morning
  Help: help or ?
  About me: who are you, what is your name
  Time / date: time, date, what time is it
  Fun: joke, tell me a joke
  Weather (demo): weather
  Exit: bye, exit, quit, goodbye
Type any of these and I will respond with predefined rules."""


def get_response(text: str) -> str:
    """Return a bot reply, or EXIT_SENTINEL when the user wants to leave."""
    if text in GREETINGS:
        return "Hello! Welcome to DecodeLabs Project 1. How can I help you today?"

    elif text in EXIT_COMMANDS:
        return EXIT_SENTINEL

    elif text == "help" or text == "?":
        return HELP_TEXT

    elif text in NAME_PHRASES:
        return (
            "I am DecodeBot, your rule-based assistant for DecodeLabs "
            "Industrial Training (Batch 2026). I respond using if-elif-else logic only."
        )

    elif text in TIME_PHRASES:
        now = datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."

    elif text in DATE_PHRASES:
        now = datetime.now()
        return f"Today is {now.strftime('%A, %B %d, %Y')}."

    elif text in THANKS_PHRASES:
        return "You're welcome! Happy to help."

    elif text in JOKE_TRIGGERS:
        return random.choice(JOKES)

    elif text == "weather" or text.startswith("weather "):
        return (
            "Weather (rule-based demo): It looks like a great day to practice "
            "control flow! (No API connected—add more elif branches to extend me.)"
        )

    else:
        return (
            f"I didn't understand '{text}'. "
            "Type 'help' to see what I can do."
        )
