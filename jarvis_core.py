import os
import sys
import subprocess
import time
import speech_recognition as sr
from groq import Groq

# --- CONFIGURATION ---
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
VOICE_MODEL = "en_GB-ryan-medium.onnx"
PIPER_PATH = "./piper/piper"

def install_dependencies():
    dependencies = ['groq', 'SpeechRecognition']
    for lib in dependencies:
        try:
            __import__(lib if lib != 'SpeechRecognition' else 'speech_recognition')
        except ImportError:
            print(f"[Setup] Installing {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

install_dependencies()
client = Groq(api_key=GROQ_API_KEY)

def speak(text):
    print(f"JARVIS: {text}")
    clean_text = text.replace('"', '\"')
    os.system(f'echo "{clean_text}" | {PIPER_PATH} --model {VOICE_MODEL} --output_file temp.wav && aplay temp.wav')

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("\n[Listening...]")
            r.pause_threshold = 1
            audio = r.listen(source)
        print("[Processing...]")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except Exception:
        return ""

def jarvis_brain(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are JARVIS, a sophisticated, slightly sarcastic, and extremely efficient AI assistant. You speak in British English. Your creator is Samuel Jithesh."},
            {"role": "user", "content": user_input}
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

def main():
    if not os.path.exists(PIPER_PATH):
        print("Piper not found.")
        return
    speak("All systems functional, Samuel.")
    while True:
        command = listen()
        if not command: continue
        if "stop" in command.lower(): break
        response = jarvis_brain(command)
        speak(response)

if __name__ == "__main__":
    main()
