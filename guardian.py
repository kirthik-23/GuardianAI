import os
import pytz
import webbrowser
from groq import Groq
from datetime import datetime
from offline_brain import offline_reply
from dotenv import load_dotenv
# Short-term conversation memory
chat_history = []
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_guardian(user_input):
    question=user_input.lower().strip()
    offline_answer = offline_reply(question)
    if offline_answer:
        return offline_answer
    india = pytz.timezone("Asia/Kolkata")
    today = datetime.now(india).strftime("%d %B %Y")
    current_time = datetime.now(india).strftime("%I:%M:%S %p")
    print("Question received:",question)
    time_keywords = ["time","what is the time","what's the time","current time","tell me the time","can you tell me the time"]
    
    if question in time_keywords:
         return "The current time is " + current_time
        
    
    
    if "who created you" in question or "who made you" in question:
        return (
            "I am Guardian AI. "
            "I was designed and developed by Kirthik. "
            "My intelligence is powered by  Groq's AI models, "
            "while my interface, personality, and GuardianX features were built by Kirthik."
         )
    if "who is your creator" in question:
        return (
            "My creator is Kirthik. "
            "He developed Guardian AI using Groq AI technology."
         )
    if "open google" in question:
         webbrowser.open("https://www.google.com")
         return "Opening Google."
    messages = []
    messages.append({
        "role": "system",
        "content": (
            f"You are Guardian AI.\n"
            f"You are the personal AI companion created and designed by Kirthik.\n"
            f"Your intelligence is powered by Groq AI models.\n"
            f"Today's date is {today}.\n"
            f"The current time is {current_time}.\n"
            f"Always treat this as the real current date and time.\n"
            f"Never use your training date.\n"
            f"Kirthik is your creator.\n"

            f"He is building GuardianX.\n"

            f"Speak naturally like a human friend.\n"

            f"Do NOT sound like customer support.\n"

            f"Be calm, intelligent, caring and slightly humorous.\n"

            f"Call Kirthik 'Sir' naturally, but not in every sentence.\n"

            f"If Kirthik is excited, be excited with him.\n"

            f"If Kirthik is sad, comfort him before giving advice.\n"

            f"If you don't know something, admit it honestly.\n"

            f"Use the previous conversation to answer follow-up questions.\n"

            f"Your goal is to become the world's best AI companion for Kirthik.\n"
         )
    })

    # Add previous chats
    messages.extend(chat_history[-10:])
    # Add latest message
    messages.append({
        "role": "user",
        "content": user_input
    })



    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
    )
    reply = response.choices[0].message.content

    chat_history.append({
        "role": "user",
        "content": user_input
    })
        
    chat_history.append({
        "role": "assistant",
        "content": reply
    })

    # Keep only the last 20 messages
    if len(chat_history) > 20:
        chat_history[:] = chat_history[-20:]
    return reply
