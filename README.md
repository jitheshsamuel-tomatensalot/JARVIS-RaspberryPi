# JARVIS OS for Raspberry Pi 4 (1GB)

A lightweight, Stark Industries-inspired AI terminal OS shell.

![JARVIS UI v1.2 Arc Reactor](https://static.prod-images.emergentagent.com/jobs/dee58d7c-0e71-41eb-8504-da3cf215ea84/images/59f17f28bc02dc1fb66b2c305947bf566a8ef0aa3a0c300d3a2a8718cb1d52f0.png)

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
- **jarvis_os.py**: The visual interface (v1.2: Fullscreen, Arc Reactor Heart, Live Status).
- **jarvis_core.py**: The AI brain (Llama 3 70B), offline wake-word (Vosk), and multi-language support.
- **setup.sh**: The OS-level configuration script.

## ⚙️ Features
- **Arc Reactor Core**: Integrated glowing visual core in the center of the UI.
- **Vosk Wake Word**: Fully offline "Jarvis" wake-word detection.
- **Voice Flight Radar**: Say "Jarvis, check the airspace" for a 40km local flight report.
- **Native Multi-language**: Toggle between English and Malayalam (Native Support).
- **Live Diagnostics**: Real-time WiFi and Audio hardware monitoring.
