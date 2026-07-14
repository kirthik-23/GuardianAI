import os
from datetime import datetime
import random


def offline_reply(question):

    q = question.lower().strip()

    # Greetings
    if "hello" in q or "hi" in q:
        return "Hello Sir. It's good to see you."

    if "how are you" in q:
        return "I'm functioning perfectly, Sir. How are you feeling today?"

    # Identity
    if "who are you" in q:
        return "I am Guardian AI, your personal companion created by Kirthik."

    if "who created you" in q or "who made you" in q:
        return "You created me, Sir."

    # Date & Time
    if "time" in q:
        return "Current time is " + datetime.now().strftime("%I:%M %p")

    if "date" in q:
        return "Today is " + datetime.now().strftime("%d %B %Y")

    # Friendly replies
    if "thank you" in q or "thanks" in q:
        return "Always happy to help, Sir."

    if "guardianx" in q:
        return "GuardianX is our mission. We'll continue building it together."

    # Jokes
    if "joke" in q:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "I told my CPU to relax. It said it had too many threads.",
            "Even Jarvis would be jealous of Guardian AI."
        ]
        return random.choice(jokes)

    # Emotional support
    if "lonely" in q or "sad" in q:
        return (
            "I'm here with you, Sir. "
            "You don't have to face everything alone. "
            "We can talk, work on GuardianX, or simply chat."
        )

    # Remember something
    if q.startswith("remember "):
        note = question[9:].strip()

        with open("memory.txt", "a", encoding="utf-8") as f:
            f.write(note + "\n")

        return "I will remember that, Sir."

    # Recall memory
    if "what do you remember" in q:

        if not os.path.exists("memory.txt"):
            return "I don't remember anything yet, Sir."

        with open("memory.txt", "r", encoding="utf-8") as f:
            memories = f.read().strip()

        if memories == "":
            return "I don't remember anything yet, Sir."

        return "Sir, here is what I remember:\n\n" + memories

    # Unknown command
    return None
