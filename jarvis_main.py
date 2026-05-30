import os
import time
import speech_recognition as sr
from groq import Groq

# --- CONFIGURATION ---
# Get your key from https://console.groq.com/
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
VOICE_MODEL = "en_GB-ryan-medium.onnx"
PIPER_PATH = "./piper/piper" # Adjust if your path is different

client = Groq(api_key=GROQ_API_KEY)

def speak(text):
    """Uses Piper TTS to speak text through the Pi's speakers."""
    print(f"JARVIS: {text}")
    # Escape double quotes for shell command
    clean_text = text.replace('"', '\"')
    os.system(f'echo "{clean_text}" | {PIPER_PATH} --model {VOICE_MODEL} --output_file temp.wav && aplay temp.wav')

def listen():
    """Listens for voice input and returns text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[Listening...]")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("[Processing...]")
        # Using Google STT for quick testing (free)
        # For maximum JARVIS speed, use Groq's Whisper API here instead!
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
    speak("Systems initialized. All protocols online. Welcome back, Samuel.")
    
    while True:
        command = listen()
        
        if not command:
            continue
            
        if "stop" in command.lower() or "exit" in command.lower():
            speak("Understood. Powering down systems. Goodbye, sir.")
            break
            
        # Get JARVIS's response
        response = jarvis_brain(command)
        
        # Speak the response
        speak(response)

if __name__ == "__main__":
    main()
