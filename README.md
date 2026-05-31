# JARVIS OS for Raspberry Pi 4 (1GB)

A lightweight, Stark Industries-inspired AI terminal OS shell.

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
- **jarvis_os.py**: The visual interface (Wallpaper, Flight Radar, App Launcher).
- **jarvis_core.py**: The AI brain, speech recognition, and voice output.
- **setup.sh**: The OS-level configuration script.

## ⚙️ Features
- Real-time Flight Radar
- Voice-controlled AI Assistant (Llama 3)
- Integrated Notepad & Media Player
- Zero-Lag performance on 1GB RAM
