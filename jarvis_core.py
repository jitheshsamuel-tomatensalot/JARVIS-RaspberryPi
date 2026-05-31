import os
import sys
import subprocess
import time
import speech_recognition as sr
from groq import Groq

# --- CONFIGURATION ---
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
PIPER_PATH = "./piper/piper"

# Language settings: (Display Name, STT Code, Piper Model, LLM Prompt)
LANGUAGES = {
    "English": ("en-US", "en_GB-ryan-medium.onnx", "British English"),
    "French": ("fr-FR", "fr_FR-siwis-medium.onnx", "French"),
    "German": ("de-DE", "de_DE-thorsten-medium.onnx", "German"),
    "Russian": ("ru-RU", "ru_RU-dmitri-medium.onnx", "Russian"),
    "Malayalam": ("ml-IN", "ml_IN-gTTS", "Malayalam") # Fallback to gTTS for ML
}

CURRENT_LANG = "English"

def install_dependencies():
    dependencies = ['groq', 'SpeechRecognition', 'gTTS']
    for lib in dependencies:
        try:
            __import__(lib if lib != 'SpeechRecognition' else 'speech_recognition')
        except ImportError:
            print(f"[Setup] Installing {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

install_dependencies()
from gtts import gTTS
client = Groq(api_key=GROQ_API_KEY)

def speak(text):
    print(f"JARVIS ({CURRENT_LANG}): {text}")
    stt_code, model, desc = LANGUAGES[CURRENT_LANG]
    
    if CURRENT_LANG == "Malayalam":
        # Use gTTS for Malayalam (High quality, but needs internet)
        tts = gTTS(text=text, lang='ml')
        tts.save("temp.mp3")
        os.system("mpg123 temp.mp3")
    else:
        # Use Piper for local speed in other languages
        clean_text = text.replace('"', '\"')
        os.system(f'echo "{clean_text}" | {PIPER_PATH} --model {model} --output_file temp.wav && aplay temp.wav')

def listen():
    r = sr.Recognizer()
    stt_code, model, desc = LANGUAGES[CURRENT_LANG]
    try:
        with sr.Microphone() as source:
            print(f"\n[Listening in {CURRENT_LANG}...]")
            r.pause_threshold = 1
            audio = r.listen(source)
        print("[Processing...]")
        query = r.recognize_google(audio, language=stt_code)
        print(f"User said: {query}")
        return query
    except Exception:
        return ""

def jarvis_brain(user_input):
    stt_code, model, desc = LANGUAGES[CURRENT_LANG]
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": f"You are JARVIS. You speak in {desc}. Your creator is Samuel Jithesh. Maintain a professional, high-status tone."},
            {"role": "user", "content": user_input}
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

def main():
    # Check for language file from UI if exists
    global CURRENT_LANG
    if os.path.exists("lang.txt"):
        with open("lang.txt", "r") as f: CURRENT_LANG = f.read().strip()

    speak(f"All systems functional in {CURRENT_LANG}, Samuel.")
    while True:
        command = listen()
        if not command: continue
        if "stop" in command.lower(): break
        response = jarvis_brain(command)
        speak(response)

if __name__ == "__main__":
    main()
