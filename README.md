# JARVIS OS for Raspberry Pi 4 (1GB)

A lightweight, Stark Industries-inspired AI terminal OS shell.

![JARVIS UI Mockup](https://static.prod-images.emergentagent.com/jobs/dee58d7c-0e71-41eb-8504-da3cf215ea84/images/fb922d403336419417a6f4c5c5dbb97e53af16d169f32c282610351ee7370745.png)

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
- Real-time Native Flight Radar (40km Radius)
- Voice-controlled AI Assistant (Llama 3)
- Multi-language support (English, Malayalam, French, German, Russian)
- Integrated Notepad & Media Player
- Zero-Lag performance on 1GB RAM
