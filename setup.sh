#!/bin/bash
echo "Starting JARVIS OS Installation..."
sudo apt update && sudo apt upgrade -y
sudo apt install -y xserver-xorg xinit openbox leafpad bastet vlc midori-browser \
python3-tk python3-pil python3-pil.imagetk alsa-utils wget git python3-pip
pip3 install groq speechrecognition
sudo raspi-config nonint do_boot_behaviour B2
cat <<EOF > ~/.xinitrc
exec openbox-session &
while true; do
    python3 $(pwd)/jarvis_os.py
    sleep 1
done
EOF
if ! grep -q "startx" ~/.bashrc; then
  echo "if [ -z \"\$DISPLAY\" ] && [ \"\$(tty)\" = \"/dev/tty1\" ]; then startx; fi" >> ~/.bashrc
fi
echo "Installation complete. Rebooting..."
sleep 3 && sudo reboot
