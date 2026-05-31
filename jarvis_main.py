import os
import sys
import subprocess

def install_dependencies():
    """Checks for and installs missing dependencies."""
    dependencies = ['groq', 'SpeechRecognition']
    for lib in dependencies:
        try:
            __import__(lib if lib != 'SpeechRecognition' else 'speech_recognition')
        except ImportError:
            print(f"[Setup] Installing missing library: {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Run the installer before anything else
install_dependencies()

import time
import speech_recognition as sr
from groq import Groq

# --- CONFIGURATION ---
# Get your key from https://console.groq.com/
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
VOICE_MODEL = "en_GB-ryan-medium.onnx"
PIPER_PATH = "./piper/piper"

client = Groq(api_key=GROQ_API_KEY)

def speak(text):
    """Uses Piper TTS to speak text through the Pi's speakers."""
    print(f"JARVIS: {text}")
    clean_text = text.replace('"', '\"')
    os.system(f'echo "{clean_text}" | {PIPER_PATH} --model {VOICE_MODEL} --output_file temp.wav && aplay temp.wav')

def listen():
    """Listens for voice input and returns text."""
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("\n[Listening...]")
            r.pause_threshold = 1
            audio = r.listen(source)
    except (AttributeError, ImportError, Exception) as e:
        print("\n[Error] PyAudio is likely missing or your microphone is not connected.")
        print("Please run: sudo apt install python3-pyaudio -y")
        return ""

    try:
        print("[Processing...]")
        # Using Google STT for quick testing
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except Exception as e:
        print("Could not understand audio.")
        return ""

def jarvis_brain(user_input):
    """Sends the user's text to Groq (Llama 3) for a response."""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are JARVIS, a sophisticated, slightly sarcastic, and extremely efficient AI assistant. You speak in British English. Your creator is Samuel Jithesh. Be helpful but maintain a professional, high-status tone."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

def main():
    # Check if Piper exists before starting
    if not os.path.exists(PIPER_PATH):
        print(f"[Error] Piper binary not found at {PIPER_PATH}. Did you follow Phase 1?")
        return

    speak("Systems initialized. All protocols online. Welcome back, Samuel.")
    
    while True:
        command = listen()
        
        if not command:
            # Prevent infinite loop if mic is broken
            time.sleep(1)
            continue
            
        if "stop" in command.lower() or "exit" in command.lower():
            speak("Understood. Powering down systems. Goodbye, sir.")
            break
            
        response = jarvis_brain(command)
        speak(response)

if __name__ == "__main__":
    main()
