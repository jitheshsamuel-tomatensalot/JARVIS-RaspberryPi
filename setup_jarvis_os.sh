#!/bin/bash

echo "=========================================="
echo "   STARK INDUSTRIES - JARVIS OS SETUP    "
echo "=========================================="

# 1. Update and Upgrade
echo "[1/6] Updating system..."
sudo apt update && sudo apt upgrade -y

# 2. Install Visual & Audio Essentials
echo "[2/6] Installing OS components..."
sudo apt install -y xserver-xorg xinit openbox leafpad bastet vlc midori-browser \
python3-tk python3-pil python3-pil.imagetk alsa-utils wget git python3-pip

# 3. Setup Python Dependencies
echo "[3/6] Installing Python AI libraries..."
pip3 install groq speechrecognition

# 4. Configure Auto-Login to Console
echo "[4/6] Configuring auto-login..."
sudo raspi-config nonint do_boot_behaviour B2

# 5. Create .xinitrc to launch Jarvis UI
echo "[5/6] Setting up Startup sequence..."
cat <<EOF > ~/.xinitrc
exec openbox-session &
while true; do
    python3 $(pwd)/jarvis_ui.py
    sleep 1
done
EOF

# 6. Auto-start X on login
if ! grep -q "startx" ~/.bashrc; then
  echo "if [ -z \"\$DISPLAY\" ] && [ \"\$(tty)\" = \"/dev/tty1\" ]; then startx; fi" >> ~/.bashrc
fi

echo "=========================================="
echo "   SETUP COMPLETE! REBOOTING IN 5 SECS   "
echo "=========================================="
sleep 5
sudo reboot
