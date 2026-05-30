# JARVIS-RaspberryPi
A replica of the JARVIS AI for Raspberry Pi 4 (1GB RAM) using Piper and Groq.

## Installation & Commands

### Phase 1: The Mouth (Voice)
1. Update your system:
   `sudo apt update && sudo apt upgrade -y` 
2. Install dependencies:
   `sudo apt install wget alsa-utils -y` 
3. Create project folder:
   `mkdir jarvis && cd jarvis` 
4. Download Piper engine:
   `wget https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_arm64.tar.gz` 
5. Extract files:
   `tar -xf piper_arm64.tar.gz` 
6. Download Ryan voice model:
   `wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/ryan/medium/en_GB-ryan-medium.onnx` 
7. Download config:
   `wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/ryan/medium/en_GB-ryan-medium.onnx.json` 
8. Test voice:
   `echo "Systems online. Welcome back, Samuel." | ./piper/piper --model en_GB-ryan-medium.onnx --output_file welcome.wav && aplay welcome.wav` 

### Phase 2: The Ears (STT)
1. Install Python libraries:
   `pip install groq SpeechRecognition pyaudio` 
   *(If pyaudio fails, run `sudo apt install python3-pyaudio -y` first)* 

## Usage
Run the master script:
`python jarvis_main.py` 
