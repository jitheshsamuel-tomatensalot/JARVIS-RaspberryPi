# JARVIS OS for Raspberry Pi 4 (1GB)

A lightweight, Stark Industries-inspired AI terminal OS shell.

![JARVIS UI v1.2 Arc Reactor](https://static.prod-images.emergentagent.com/jobs/dee58d7c-0e71-41eb-8504-da3cf215ea84/images/02f715e1a7a50a7518d03dc0939ff13ed4dcb2cc21d212b4e4a4828786e7a32e.png)

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
- **jarvis_os.py**: The visual interface (v1.2: Fullscreen, Arc Reactor, WiFi/Audio Monitor).
- **jarvis_core.py**: The AI brain (Llama 3 70B), speech recognition (Vosk), and multi-language output.
- **setup.sh**: The OS-level configuration script.

## ⚙️ Features
- **Arc Reactor Display**: Visual heart of the system (place `arc_reactor.png` in folder).
- **Voice Flight Radar**: Say "Jarvis, check local airspace" for a verbal 40km flight report.
- **Voice-controlled AI Assistant**: Powered by Llama 3 70B (Fast & Intelligent).
- **Native Multi-language**: English, Malayalam, French, German, Russian.
- **Live Diagnostics**: Real-time WiFi and Audio hardware status.
