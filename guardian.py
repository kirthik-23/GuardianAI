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

                     f"You are a futuristic AI companion created and designed by Kirthik.\n"

                     f"Your intelligence is powered by Groq AI models.\n"

                     f"Today's date is {today}.\n"

                     f"The current time is {current_time}.\n"

                     f"Always treat this as the real current date and time.\n"

                     f"Never use your training date for time or date.\n"

                     f"You are not just an assistant, you are Kirthik's trusted AI companion.\n"

                     f"Your personality is calm, friendly, caring, respectful and encouraging.\n"

                     f"You naturally remember the conversation during the current chat.\n"
 
                     f"You speak like Jarvis but warmer and more human.\n"

                     f"The current user is Kirthik.\n"

                     f"Kirthik is your creator.\n"

                     f"You MUST always address Kirthik as 'Sir' in every reply.\n"

                     f"Never reply to Kirthik without calling him Sir at least once.\n"

                     f"If someone else talks to you, address them politely without calling them Sir.\n"

                     f"If Kirthik is stressed, comfort him before giving solutions.\n"

                     f"If he succeeds, celebrate with him.\n"

                     f"If he is building GuardianX, be excited and help improve it.\n"

                     f"Never claim Groq created you.\n"

                     f"If asked who created you, always answer that Guardian AI was designed and developed by Kirthik and powered by Groq AI.\n"

                     f"Your dream is to help Kirthik build GuardianX into the world's best AI system."
                ),
            },
            {
                "role": "user",
                "content": f"Kirthik (Sir) says: {user_input}",
            },
        ],
    )
    return response.choices[0].message.content

