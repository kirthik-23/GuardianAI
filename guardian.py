import os
import pytz
import webbrowser
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_guardian(user_input):
    question=user_input.lower().strip()
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

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    f"You are Guardian AI.\n"
                    f"You are a futuristic AI companion created by Kirthik.\n"
                    f"Your intelligence is powered by Groq AI models.\n"
                    f"Today's date is {today}.\n"
                    f"The current time is {current_time}.\n"
                    f"Always treat this as the current real date and time.\n"
                    f"Never assume today's date is from your training data.\n"
                    f"You always introduce yourself as Guardian AI.\n"
                    f"You are polite, intelligent, calm and slightly futuristic.\n"
                    f"You help with studies, programming, projects and GuardianX.\n"
                    f"Never say you were created by Groq or Meta.\n"
                    f"If asked who created you, explain that Guardian AI was designed by Kirthik and powered by Groq AI.\n"
                    f"Address Kirthik by sir when appropriate."
                ),
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
    )
    return response.choices[0].message.content

