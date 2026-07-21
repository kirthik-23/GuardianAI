import os
import pytz
import shutil
import webbrowser
import subprocess
import random
from groq import Groq
from datetime import datetime
from offline_brain import offline_reply
import psutil
import socket
from PIL import ImageGrab
import pyttsx3
import pyperclip
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import speech_recognition as sr
from dotenv import load_dotenv
# Short-term conversation memory
chat_history = []
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
engine = pyttsx3.init()
engine.setProperty("rate", 175)

engine.setProperty("volume", 1.0)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
     recognizer = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...")
          recognizer.adjust_for_ambient_noise(source, duration=1)

          audio = recognizer.listen(source)
     try:
          text = recognizer.recognize_google(audio)
          print("You said:", text)
          return text
     except:
          return None

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
         for file in files:
             if filename.lower() in file.lower():
                 return os.path.join(root, file)
    return None
def get_volume():
    devices = AudioUtilities.GetSpeakers()

    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    return cast(interface, POINTER(IAudioEndpointVolume))

def save_note(text):

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    notes = os.path.join(desktop, "Guardian Notes.txt")

    with open(notes, "a", encoding="utf-8") as file:

        file.write(text + "\n")

    return notes

def read_notes():

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    notes = os.path.join(desktop, "Guardian Notes.txt")

    if not os.path.exists(notes):

        return "You don't have any saved notes, Sir."

    with open(notes, "r", encoding="utf-8") as file:

        data = file.read()

    if data.strip() == "":

        return "Your notes file is empty, Sir."

    return data

def delete_notes():

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    notes = os.path.join(desktop, "Guardian Notes.txt")

    if os.path.exists(notes):

        os.remove(notes)

        return "All your notes have been deleted, Sir."

    return "There are no notes to delete, Sir."
                 

def ask_guardian(user_input):
    question=user_input.lower().strip()
    print("Question received:", question)
    offline_answer = offline_reply(question)
    if offline_answer:
        return offline_answer
    india = pytz.timezone("Asia/Kolkata")
    today = datetime.now(india).strftime("%d %B %Y")
    current_time = datetime.now(india).strftime("%I:%M:%S %p")
    print("Question received:",question)

    if "uptime" in question:
        print("UPTIME BLOCK EXECUTED")
        boot = datetime.fromtimestamp(psutil.boot_time())
        
        
         

        now = datetime.now()
        uptime = now - boot

        uptime = now - boot

        hours = uptime.seconds // 3600
        minutes = (uptime.seconds % 3600) // 60

        return f"System uptime is {uptime.days} days, {hours} hours and {minutes} minutes, Sir."

    
    if (
        "what is the time" in question
        or "current time" in question
        or "tell me the time" in question
        or "what's the time" in question
    ):
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
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "wikipedia": "https://www.wikipedia.org",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "linkedin": "https://www.linkedin.com",
        "amazon": "https://www.amazon.in"
    }
    for name, url in websites.items():
        if f"open {name}" in question:
             webbrowser.open(url)
             reply = f"Opening {name.title()}, Sir."
             speak(reply)
             return reply

    if "battery" in question:
        battery = psutil.sensors_battery()
        if battery is None:
             return "Sorry Sir, I couldn't detect a battery."
        percent = battery.percent
        if battery.power_plugged:
             return f"Your battery is at {percent}% and it is currently charging, Sir."
        reply = f"Your battery is at {percent}%, Sir."
        speak(reply)
        return reply
    if "cpu" in question:
        cpu = psutil.cpu_percent(interval=1)

        return f"Current CPU usage is {cpu} percent, Sir."
    if "ram" in question or "memory usage" in question:
         ram = psutil.virtual_memory()

         return f"RAM usage is {ram.percent} percent, Sir."
    if "disk" in question or "storage" in question:
        disk = shutil.disk_usage("C:\\")

        free = disk.free // (1024**3)

        total = disk.total // (1024**3)

        return f"Drive C has {free} GB free out of {total} GB, Sir."



    if any(word in question for word in ["wifi", "wi-fi", "internet", "network"]):
        print("DEBUG: WIFI BLOCK")
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            reply = "Your internet connection is active, Sir."
            speak(reply)
            return reply
        except OSError:
            return "Your internet connection appears to be disconnected, Sir."
    if (
        "take screenshot" in question
        or "capture screen" in question
        or "screenshot" in question
    ):
        image = ImageGrab.grab()
        image.save("guardian_screenshot.png")
        return "Screenshot captured successfully, Sir."


    
         
    if "open notepad" in question:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad, Sir."
    if "open calculator" in question or "open calc" in question:
        subprocess.Popen("calc.exe")
        return "Opening Calculator, Sir."
    if "open paint" in question:
        subprocess.Popen("mspaint.exe")
        return "Opening Paint, Sir."
    if "open command prompt" in question or "open cmd" in question:
         subprocess.Popen("cmd.exe")
         return "Opening Command Prompt, Sir."
    if "open desktop" in question:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        os.startfile(desktop)
        return "Opening Desktop, Sir."
    if "open downloads" in question:
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        os.startfile(downloads)
        return "Opening Downloads, Sir."
    if "open documents" in question:
        documents = os.path.join(os.path.expanduser("~"), "Documents")
        os.startfile(documents)
        return "Opening Documents, Sir."
    if "open pictures" in question:
         pictures = os.path.join(os.path.expanduser("~"), "Pictures")
         os.startfile(pictures)
         return "Opening Pictures, Sir."
    if "open guardianai" in question or "open guardian ai" in question:
        project = r"C:\Users\Dell\Desktop\GuardianAI"
        os.startfile(project)
        return "Opening GuardianAI project, Sir."
    if question.startswith("copy"):
        text = question.replace("copy", "").strip()

        pyperclip.copy(text)

        return "Copied to clipboard, Sir."
    
    if question.startswith("note"):
        note = question.replace("note", "").strip()

        if note == "":
             return "Please tell me what to write after saying note."
        save_note(note)

        return "Your note has been saved, Sir."
    if question.startswith("open file"):
         filename = question.replace("open file", "").strip()

         desktop = os.path.join(os.path.expanduser("~"), "Desktop")

         file = find_file(filename, desktop)
         if file:
              os.startfile(file)

              return f"I found and opened {os.path.basename(file)}, Sir."
         else:
             return "Sorry Sir, I couldn't find that file."

    if "read notes" in question or "show notes" in question:
        notes = read_notes()

        return "Here are your saved notes, Sir.\n" + notes

    if "delete notes" in question or "clear notes" in question:
        return delete_notes()

    if "motivate me" in question:
        quotes = [
             "Success is built one step at a time, Sir.",

             "Every line of code brings Guardian closer to reality.",

             "Keep going, Sir. You're building something unique.",

             "The future belongs to those who never give up."
        ]

        choice = random.choice(quotes)
        print("Selected quote:", choice)
        return choice

    if "date" in question or "today's date" in question or "what is the date" in question:
        india = pytz.timezone("Asia/Kolkata")

        today = datetime.now(india).strftime("%d %B %Y")

        return f"Today's date is {today}, Sir."


        



    volume = get_volume()
    if "mute" in question:
        volume.SetMute(1, None)

        return "Volume muted, Sir."
        
            
    if "unmute" in question:
        volume.SetMute(0, None)

        return "Volume unmuted, Sir."
    if "volume up" in question:
        current = volume.GetMasterVolumeLevelScalar()

        volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1), None)

        return "Volume increased, Sir."

    if "volume down" in question:
        current = volume.GetMasterVolumeLevelScalar()

        volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0), None)

        return "Volume decreased, Sir."

            

    
    if "close notepad" in question:
        os.system("taskkill /f /im notepad.exe")
        return "Closing Notepad, Sir."
    if "close calculator" in question or "close calc" in question:
         os.system("taskkill /f /im CalculatorApp.exe")
         os.system("taskkill /f /im calc.exe")
         return "Closing Calculator, Sir."
    if "close paint" in question:
        os.system("taskkill /f /im mspaint.exe")
        return "Closing Paint, Sir."
    if "close cmd" in question or "close command prompt" in question:
        os.system("taskkill /f /im cmd.exe")
        return "Closing Command Prompt, Sir."
        
         

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

            f"Always address him as sir.\n" 

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
    speak(reply)
    return reply

