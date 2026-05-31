import os
import sys
import subprocess
import time
import json
import queue
import requests
import speech_recognition as sr
from groq import Groq
from vosk import Model, KaldiRecognizer

# --- CONFIGURATION ---
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
PIPER_PATH = "./piper/piper"
# Download model from: https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"

LANGUAGES = {
    "English": ("en-US", "en_GB-ryan-medium.onnx", "British English"),
    "Malayalam": ("ml-IN", "ml_IN-g6p-medium.onnx", "Malayalam")
}

CURRENT_LANG = "English"

# Vosk Audio Queue
q = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status: print(status, file=sys.stderr)
    q.put(bytes(indata))

def install_dependencies():
    dependencies = ['groq', 'SpeechRecognition', 'vosk', 'sounddevice']
    for lib in dependencies:
        try:
            __import__(lib)
        except ImportError:
            print(f"[Setup] Installing {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Check for Vosk Model
if not os.path.exists(VOSK_MODEL_PATH):
    print(f"\n[!] VOSK WAKE-WORD MODEL MISSING.")
    print(f"Please download and unzip it in this folder: alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip\n")

install_dependencies()
import sounddevice as sd
client = Groq(api_key=GROQ_API_KEY)

def speak(text):
    stt_code, model, desc = LANGUAGES.get(CURRENT_LANG, LANGUAGES["English"])
    clean_text = text.replace('"', '\"')
    os.system(f'echo "{clean_text}" | {PIPER_PATH} --model {model} --output_file temp.wav && aplay temp.wav')

def listen_for_command():
    """Uses Groq for high-accuracy command processing."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[JARVIS Listening...]")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        return r.recognize_google(audio, language=LANGUAGES[CURRENT_LANG][0])
    except: return ""

def wait_for_wake_word():
    """Offline wake-word detection using Vosk."""
    model = Model(VOSK_MODEL_PATH)
    with sd.RawInputStream(samplerate=16000, blocksize=8000, device=None, dtype='int16', 
                           channels=1, callback=audio_callback):
        rec = KaldiRecognizer(model, 16000)
        print("\n[Vosk Active: Waiting for 'Jarvis'...]\n")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if "jarvis" in result.get("text", ""):
                    return True

def main():
    global CURRENT_LANG
    while True:
        if wait_for_wake_word():
            speak("Yes, Samuel?")
            command = listen_for_command()
            if command:
                print(f"User: {command}")
                # Process with Groq Llama 3
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "system", "content": f"You are JARVIS. Speak in {CURRENT_LANG}."}, 
                              {"role": "user", "content": command}],
                    model="llama3-70b-8192",
                )
                speak(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    main()
