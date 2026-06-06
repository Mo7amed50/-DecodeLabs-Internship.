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

HOW_ARE_YOU_PHRASES = {
    "how are you",
    "how are you doing",
    "how's it going",
    "how is it going",
}

CAPABILITY_PHRASES = {
    "what can you do",
    "what are your capabilities",
    "what do you do",
    "help me",
}

WEATHER_PHRASES = {
    "weather",
    "weather report",
    "what's the weather",
    "whats the weather",
}

JOKE_TRIGGERS = {
    "joke",
    "tell me a joke",
    "make me laugh",
    "tell me something funny",
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
  Status: how are you
  Fun: joke, tell me a joke
  Weather (demo): weather
  Exit: bye, exit, quit, goodbye
Type any of these and I will respond with predefined rules."""


def matches(text: str, phrases: set[str]) -> bool:
    """Check exact and natural phrase variations for rule-based matching."""
    if text in phrases:
        return True
    return any(
        text.startswith(f"{phrase} ")
        or text.endswith(f" {phrase}")
        or f" {phrase} " in text
        for phrase in phrases
    )


def get_response(text: str) -> str:
    """Return a bot reply, or EXIT_SENTINEL when the user wants to leave."""
    if matches(text, GREETINGS):
        return "Hello! Welcome to DecodeLabs Project 1. How can I help you today?"

    elif matches(text, EXIT_COMMANDS):
        return EXIT_SENTINEL

    elif text == "help" or text == "?":
        return HELP_TEXT

    elif matches(text, NAME_PHRASES):
        return (
            "I am DecodeBot, your rule-based assistant for DecodeLabs "
            "Industrial Training (Batch 2026). I respond using if-elif-else logic only."
        )

    elif matches(text, HOW_ARE_YOU_PHRASES):
        return "I'm just code, but I'm ready to help you with DecodeLabs tasks!"

    elif matches(text, CAPABILITY_PHRASES):
        return (
            "I can greet you, tell the date and time, tell a joke, show a weather demo, "
            "answer questions about myself, and exit cleanly when you say bye."
        )

    elif matches(text, TIME_PHRASES):
        now = datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}"

    elif matches(text, DATE_PHRASES):
        now = datetime.now()
        return f"Today is {now.strftime('%A, %B %d, %Y')}"

    elif matches(text, THANKS_PHRASES):
        return "You're welcome! Happy to help."

    elif matches(text, JOKE_TRIGGERS):
        return random.choice(JOKES)

    elif matches(text, WEATHER_PHRASES) or text.startswith("weather "):
        city = text.removeprefix("weather ").strip()
        if city:
            return (
                f"Weather (rule-based demo): I don't have live data, but {city.title()} "
                "sounds like a nice place to learn Python today!"
            )
        return (
            "Weather (rule-based demo): It looks like a great day to practice "
            "control flow! (No API connected—add more elif branches to extend me.)"
        )

    else:
        return (
            f"I didn't understand '{text}'. "
            "Type 'help' to see what I can do."
        )
