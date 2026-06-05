# DecodeLabs Project 1: Rule-Based AI Chatbot

**Batch:** 2026  
**Track:** Artificial Intelligence — Industrial Training Kit  
**Organization:** DecodeLabs

## Overview

A command-line chatbot that simulates basic conversation using explicit **if-elif-else** rules—no machine learning. This is the foundation milestone for control flow and decision-making in AI engineering.

## Requirements

- Python 3.8 or newer
- No third-party packages (standard library only)

## How to Run

```bash
cd d:\Decode
python chatbot.py
```

## Project Structure

| File | Role |
|------|------|
| `chatbot.py` | Main loop, input normalization, exit handling |
| `responses.py` | All rule-based replies (`if` / `elif` / `else`) |
| `requirements.txt` | Notes that no pip install is needed |

## PDF Checklist (Project 1)

| Requirement | Implementation |
|-------------|----------------|
| Continuous loop | `while True` in `chatbot.py` `main()` |
| Greetings | `GREETINGS` set → greeting reply |
| Exit commands | `EXIT_COMMANDS` set → `EXIT_SENTINEL` → break loop |
| If-else logic | `get_response()` in `responses.py` |

## Supported Commands

| Category | Examples |
|----------|----------|
| Greetings | `hi`, `hello`, `hey`, `good morning` |
| Help | `help`, `?` |
| About | `who are you`, `what is your name` |
| Time / date | `time`, `what time is it`, `date` |
| Thanks | `thanks`, `thank you` |
| Fun | `joke`, `tell me a joke` |
| Weather (demo) | `weather` |
| Exit | `bye`, `exit`, `quit`, `goodbye` |

Input is normalized (lowercase, trimmed, collapsed spaces, trailing punctuation removed) for friendlier matching.

## Sample Transcript

```
========================================
  DecodeLabs | Project 1: Rule-Based Bot
  Batch 2026
========================================
Type 'help' to see commands, or 'bye' to exit.

You: hello
Bot: Hello! Welcome to DecodeLabs Project 1. How can I help you today?
You: time
Bot: The current time is 02:30 PM.
You: joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs.
You: xyz
Bot: I didn't understand 'xyz'. Type 'help' to see what I can do.
You: bye
Bot: Goodbye! Thanks for chatting. See you at DecodeLabs.
```

## Extensions (Beyond Minimum)

- Input normalization in `normalize()`
- Extra intents: help, name, time, date, thanks, joke, weather stub
- `KeyboardInterrupt` (Ctrl+C) handled gracefully
- Split modules for clear grading of control flow vs. loop logic

## Contact (DecodeLabs)

- Web: www.decodelabs.tech
- Email: decodelabs.tech@gmail.com
