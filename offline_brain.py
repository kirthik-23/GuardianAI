import os
import json
from datetime import datetime
import random
MEMORY_FILE = "memory.json"
def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(memory):

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4)



def offline_reply(question):

    q = question.lower().strip()
    print("DEBUG QUESTION:", q)
    memory = load_memory()

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

  
    

    # Unknown command

    # Permanent Memory
    
    if q.startswith("my ") and " is " in q:
         key, value = q.split(" is ", 1)
         key = key.replace("my ", "").strip()
         value = value.strip()
         memory[key] = value
         save_memory(memory)
         return f"I've learned that, Sir. Your {key} is now stored."
        # Greetings

    if "good morning" in q:
        return "Good morning, Sir. I hope you have a productive day."

    if "good afternoon" in q:
        return "Good afternoon, Sir. I'm ready whenever you need me."

    if "good evening" in q:
        return "Good evening, Sir. It's good to see you again."

    if "good night" in q or "goodnight" in q:
        return (
            "Good night, Sir. "
            "Get a good rest. "
            "I'll be here whenever you need me tomorrow."
        )

    if q == "gn":
        return "Good night, Sir. Sleep well."

    if q.startswith("i like "):
        thing = question[7:].strip()

        memory["likes"] = thing

        save_memory(memory)

        return f"I'll remember that you like {thing}, Sir."
    if q.startswith("i am building "):
         thing = question[14:].strip()

         memory["current project"] = thing

         save_memory(memory)

         return f"I'll remember that you're building {thing}, Sir."
    if "guardianx" in q:
        return "GuardianX is our mission. We'll continue building it together."
    patterns = [
        ("my favourite movie is ", "favourite movie"),
        ("my favorite movie is ", "favourite movie"),
        ("my favourite food is ", "favourite food"),
        ("my favorite food is ", "favourite food"),
        ("my favourite colour is ", "favourite colour"),
        ("my favorite colour is ", "favourite colour"),
        ("my hobby is ", "hobby"),
        ("i study in ", "school"),
        ("i live in ", "city"),
    ]
    for pattern, key in patterns:
        if q.startswith(pattern):
             value = question[len(pattern):].strip()
             memory[key] = value
             save_memory(memory)
             return f"I'll remember that, Sir. Your {key} is {value}."






    if q.startswith("remember "):
        

        text = question[9:].strip()

        if " is " in text:

            key, value = text.split(" is ", 1)

            key = key.strip().replace("?", "").replace(".", "")
            value = value.strip()

            memory[key] = value

            save_memory(memory)

            return f"I'll remember that, Sir. {key} is now stored."

        return "Please say: Remember favourite movie is Iron Man."


    if (
    q.startswith("what is ")
    or q.startswith("what's ")
    or q.startswith("tell me ")
    or q.startswith("do you remember ")
    ):
        key = q
        

        key = key.replace("what is ", "")
        key = key.replace("what's ", "")
        key = key.replace("tell me ", "")
        key = key.replace("do you remember ", "")
        key = key.replace("my ", "")
        key = key.replace("?", "")
        key = key.strip()

        if key in memory:
             return f"Your {key} is {memory[key]}, Sir."
    # Automatic Learning

    if q.startswith("my ") and " is " in q:
        key, value = q.split(" is ", 1)
        key = key.replace("my ", "").strip()
        value = value.strip()
        memory[key] = value
        save_memory(memory)
        return f"I've learned that, Sir. Your {key} is now stored."
    if q.startswith("i am "):
        value = question[5:].strip()
        memory["status"] = value
        save_memory(memory)
        return f"I'll remember that you're {value}, Sir."
    if q.startswith("i want to become "):
        value = question[17:].strip()
        memory["dream"] = value
        save_memory(memory)
        return f"Your dream to become {value} has been remembered, Sir."
    if q.startswith("my dream is "):
        value = question[12:].strip()
        memory["dream"] = value
        save_memory(memory)
        return f"I'll remember your dream, Sir."


        

    # Search memory intelligently

    for key, value in memory.items():
        if "what do i like" in q and "likes" in memory:
             return f"You like {memory['likes']}, Sir."
        if "what am i building" in q and "current project" in memory:
            return f"You are building {memory['current project']}, Sir."
         # Exact key match
        if key in q:
             return f"Sir, your {key} is {value}."
         # Partial word matching
        words = key.split()
        matches = 0
        for word in words:
            if word in q:
                matches += 1
        if matches >= 2:
            return f"Sir, your {key} is {value}."
            
                
    return None
       


    
