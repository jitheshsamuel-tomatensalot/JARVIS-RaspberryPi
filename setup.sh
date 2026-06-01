#!/bin/bash
echo "=========================================="
echo "   STARK INDUSTRIES - JARVIS OS SETUP    "
echo "=========================================="

# 1. Update and Upgrade
echo "[1/7] Updating system..."
sudo apt update && sudo apt upgrade -y

# 2. Install Visual & Audio Essentials (Fixed for Debian 12+)
echo "[2/7] Installing OS components..."
# leafpad is replaced by mousepad; midori is often unavailable, using chromium-browser as light alternative or just xterm
sudo apt install -y xserver-xorg xinit openbox mousepad bastet vlc chromium-browser \
python3-tk python3-pil python3-pil.imagetk alsa-utils wget git python3-pip unzip mpg123 libportaudio2 python3-pyaudio

# 3. Setup Python Dependencies (Fixed for 'externally-managed-environment')
echo "[3/7] Installing Python AI libraries..."
# Using --break-system-packages for convenience on a dedicated Pi project, or a venv is better.
# For a 12-year-old on a dedicated OS, --break-system-packages is the simplest fix.
pip3 install groq speechrecognition vosk sounddevice gTTS --break-system-packages

# 4. Download AI Models (The 'Core' Models)
echo "[4/7] Downloading Voice and Wake-word models..."
# Piper Engine
if [ ! -d "piper" ]; then
    wget https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_arm64.tar.gz
    tar -xf piper_arm64.tar.gz
fi

# English Voice (Ryan)
if [ ! -f "en_GB-ryan-medium.onnx" ]; then
    wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/ryan/medium/en_GB-ryan-medium.onnx
    wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/ryan/medium/en_GB-ryan-medium.onnx.json
fi

# Malayalam Voice (Fallback)
if [ ! -f "ml_IN-g6p-medium.onnx" ]; then
    wget https://huggingface.co/rhasspy/piper-voices/resolve/main/ml/ml_IN/g6p/medium/ml_IN-g6p-medium.onnx
    wget https://huggingface.co/rhasspy/piper-voices/resolve/main/ml/ml_IN/g6p/medium/ml_IN-g6p-medium.onnx.json
fi

# Vosk Wake-word Model
if [ ! -d "vosk-model-small-en-us-0.15" ]; then
    wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
    unzip vosk-model-small-en-us-0.15.zip
fi

# 5. Configure Auto-Login to Console
echo "[5/7] Configuring auto-login..."
sudo raspi-config nonint do_boot_behaviour B2

# 6. Create .xinitrc to launch Jarvis UI
echo "[6/7] Setting up Startup sequence..."
cat <<EOF > ~/.xinitrc
exec openbox-session &
while true; do
    python3 $(pwd)/jarvis_os.py
    sleep 1
done
EOF

# 7. Auto-start X on login
if ! grep -q "startx" ~/.bashrc; then
  echo 'if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then startx; fi' >> ~/.bashrc
fi

echo "=========================================="
echo "   SETUP COMPLETE! REBOOTING IN 5 SECS   "
echo "=========================================="
sleep 5
sudo reboot
