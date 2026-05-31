# JARVIS OS for Raspberry Pi 4 (1GB)

A lightweight, Stark Industries-inspired AI terminal OS shell.

![JARVIS UI v1.1 Mockup](https://static.prod-images.emergentagent.com/jobs/dee58d7c-0e71-41eb-8504-da3cf215ea84/images/245d16b58a0dd6ac12abf8c6d90f0f88a9e2a0487a4edde660432d3e18b40096.png)

## 🚀 Quick Start (3 Steps)

### 1. Clone the Lab
```bash
git clone https://github.com/jitheshsamuel-tomatensalot/JARVIS-RaspberryPi.git
cd JARVIS-RaspberryPi
```

### 2. Build the OS
Run the master setup script. This will install all dependencies and configure the Pi to boot directly into the JARVIS shell.
```bash
chmod +x setup.sh
sudo ./setup.sh
```

### 3. Connect the Brain
Open `jarvis_core.py` and add your **Groq API Key**.

## 📂 System Components
- **jarvis_os.py**: The visual interface (V1.1: Clock, WiFi Status, Audio Monitor).
- **jarvis_core.py**: The AI brain (Llama 3), speech recognition (Vosk/Google), and voice output (Piper/gTTS).
- **setup.sh**: The OS-level configuration script.

## ⚙️ Features
- **Voice Flight Radar**: Ask "Jarvis, any planes nearby?" and he'll report flights in a 40km radius.
- **Voice-controlled AI Assistant**: Powered by Llama 3 70B.
- **Multi-language support**: English, Malayalam (Native Support), French, German, Russian.
- **Live Diagnostics**: Real-time WiFi quality and Audio I/O device monitoring.
- **Zero-Lag performance**: Highly optimized for 1GB RAM hardware.
