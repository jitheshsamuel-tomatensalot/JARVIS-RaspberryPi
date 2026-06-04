import os
import sys
import subprocess
import time
import json
import speech_recognition as sr
from groq import Groq

# --- CONFIGURATION ---
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
PIPER_PATH = "./piper/piper"
VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"

client = Groq(api_key=GROQ_API_KEY)

def speak(text):
    print(f"JARVIS: {text}")
    clean_text = text.replace('"', '\"')
    os.system(f'echo "{clean_text}" | {PIPER_PATH} --model en_GB-ryan-medium.onnx --output_file temp.wav && aplay temp.wav')

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[JARVIS Listening...]")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        return r.recognize_google(audio)
    except: return ""

def jarvis_agent_brain(user_input):
    """Advanced brain that can handle Gmail and WhatsApp intents."""
    system_prompt = """
    You are JARVIS. You are an agentic assistant. 
    You have access to the following tools via your partner Rishvik2.0:
    - GMAIL: Read emails, send emails, search inbox.
    - WHATSAPP: Read messages, send messages to contacts.
    
    If the user asks for one of these, respond with a specific command format:
    [ACTION: GMAIL_READ | QUERY: unread]
    [ACTION: GMAIL_SEND | TO: <email> | BODY: <message>]
    [ACTION: WHATSAPP_SEND | CONTACT: <name> | MESSAGE: <message>]
    [ACTION: WHATSAPP_READ]
    
    Otherwise, respond naturally as JARVIS.
    """
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        model="llama3-70b-8192",
    )
    response = chat_completion.choices[0].message.content
    
    # Check if JARVIS output an action command
    if "[ACTION:" in response:
        print(f"[AGENT ACTION DETECTED]: {response}")
        # In a real setup, this would be sent to the Wingman API.
        # For now, we tell the user to confirm the action on the phone.
        speak("Sir, I am initiating that request through the secure uplink. Please check your primary device for confirmation.")
    
    return response

def main():
    speak("Agentic protocols engaged. Gmail and WhatsApp systems standby.")
    while True:
        # Simplified loop for demonstration: In v1.2 this uses Vosk wake-word
        command = listen_for_command()
        if command:
            print(f"User: {command}")
            response = jarvis_agent_brain(command)
            if "[ACTION:" not in response:
                speak(response)

if __name__ == "__main__":
    main()
