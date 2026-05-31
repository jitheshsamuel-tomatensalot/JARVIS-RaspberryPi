import os
import sys
import subprocess
import time
import requests
import speech_recognition as sr
from groq import Groq

# --- CONFIGURATION ---
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
PIPER_PATH = "./piper/piper"
HOME_LAT = 10.8505
HOME_LON = 76.2711

LANGUAGES = {
    "English": ("en-US", "en_GB-ryan-medium.onnx", "British English"),
    "Malayalam": ("ml-IN", "ml_IN-g6p-medium.onnx", "Malayalam")
}

CURRENT_LANG = "English"

def get_nearby_flights():
    """Fetches planes within 40km and returns a summary string."""
    lat_min, lat_max = HOME_LAT - 0.36, HOME_LAT + 0.36
    lon_min, lon_max = HOME_LON - 0.36, HOME_LON + 0.36
    try:
        url = f"https://opensky-network.org/api/states/all?lamin={lat_min}&lamax={lat_max}&lomin={lon_min}&lomax={lon_max}"
        r = requests.get(url, timeout=5)
        data = r.json()
        if data['states']:
            count = len(data['states'])
            return f"Sir, I've detected {count} aircraft in our local airspace."
        return "Airspace is clear, sir. No aircraft detected within 40 kilometers."
    except:
        return "I am unable to access flight data at the moment, sir."

client = Groq(api_key=GROQ_API_KEY)

def speak(text):
    print(f"JARVIS: {text}")
    stt_code, model, desc = LANGUAGES.get(CURRENT_LANG, LANGUAGES["English"])
    clean_text = text.replace('"', '\"')
    os.system(f'echo "{clean_text}" | {PIPER_PATH} --model {model} --output_file temp.wav && aplay temp.wav')

def listen():
    r = sr.Recognizer()
    stt_code, model, desc = LANGUAGES.get(CURRENT_LANG, LANGUAGES["English"])
    try:
        with sr.Microphone() as source:
            print("\n[Listening...]")
            r.pause_threshold = 1
            audio = r.listen(source)
        query = r.recognize_google(audio, language=stt_code)
        print(f"User: {query}")
        return query
    except: return ""

def jarvis_brain(user_input):
    # Special check for flights
    if "flight" in user_input.lower() or "planes" in user_input.lower():
        return get_nearby_flights()

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": f"You are JARVIS. Speak in {CURRENT_LANG}. Be sophisticated and efficient."},
            {"role": "user", "content": user_input}
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

def main():
    global CURRENT_LANG
    if os.path.exists("lang.txt"):
        with open("lang.txt", "r") as f: CURRENT_LANG = f.read().strip()
    
    speak(f"Systems online in {CURRENT_LANG}. Waiting for your command.")
    while True:
        command = listen()
        if not command: continue
        if "stop" in command.lower(): break
        response = jarvis_brain(command)
        speak(response)

if __name__ == "__main__":
    main()
