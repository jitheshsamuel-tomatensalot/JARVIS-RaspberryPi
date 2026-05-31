# JARVIS OS for Raspberry Pi 4 (1GB)

A lightweight, Stark Industries-inspired AI terminal OS shell.

![JARVIS UI v1.2 Final](https://static.prod-images.emergentagent.com/jobs/dee58d7c-0e71-41eb-8504-da3cf215ea84/images/2c4ed96bc4bbcffc7a7f7d4dfeb7da5d3831a6e35321c59c468f15f8be701b70.png)

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
- **jarvis_os.py**: Full-screen visual interface with centered Arc Reactor heart.
- **jarvis_core.py**: AI brain (Llama 3 70B), offline wake-word (Vosk), and multi-language support.
- **setup.sh**: One-click OS-level configuration script.

## ⚙️ Features
- **Arc Reactor Visual**: Central glowing core for the ultimate movie feel.
- **Vosk Wake Word**: Fully offline "Jarvis" activation.
- **Voice Airspace Report**: Real-time 40km flight status via voice command.
- **Malayalam & Multi-lang**: Full support for English and Malayalam (Native).
- **Hardware Monitor**: Live WiFi and Audio I/O diagnostics.
