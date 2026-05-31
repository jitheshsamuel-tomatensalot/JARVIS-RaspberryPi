import tkinter as tk
import os
import subprocess
from datetime import datetime

# --- CONFIGURATION ---
# Change this path to your wallpaper file later
WALLPAPER_PATH = "wallpaper.jpg" 

class JarvisOS:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS OS Shell")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')

        # Load Wallpaper if exists, else keep black
        if os.path.exists(WALLPAPER_PATH):
            try:
                from PIL import Image, ImageTk
                self.bg_image = Image.open(WALLPAPER_PATH)
                self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
                self.bg_photo = ImageTk.PhotoImage(self.bg_image)
                self.bg_label = tk.Label(self.root, image=self.bg_photo)
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            except Exception:
                pass

        # UI Elements (Stark Style Cyan)
        self.color = "#00d4ff"
        
        # Clock
        self.time_label = tk.Label(self.root, font=('Courier', 40, 'bold'), fg=self.color, bg='black')
        self.time_label.pack(pady=20)
        self.update_time()

        # Header
        tk.Label(self.root, text="STARK INDUSTRIES - JARVIS SYSTEM v1.0", font=('Courier', 12), fg=self.color, bg='black').pack()

        # Main Menu Frame
        menu_frame = tk.Frame(self.root, bg='black')
        menu_frame.pack(expand=True)

        # App Buttons
        self.create_button(menu_frame, "LAUNCH JARVIS AI", self.launch_ai)
        self.create_button(menu_frame, "FLIGHT RADAR", self.launch_radar)
        self.create_button(menu_frame, "NOTEPAD", self.launch_notepad)
        self.create_button(menu_frame, "GAMES", self.launch_games)
        self.create_button(menu_frame, "VLC PLAYER", self.launch_vlc)
        self.create_button(menu_frame, "EXIT TO TERMINAL", self.root.destroy)

    def create_button(self, parent, text, command):
        btn = tk.Button(parent, text=text, command=command, font=('Courier', 14, 'bold'), 
                        fg='black', bg=self.color, activebackground='white', width=20, pady=10)
        btn.pack(pady=10)

    def update_time(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=now)
        self.root.after(1000, self.update_time)

    # App Launchers
    def launch_ai(self):
        os.system("lxterminal -e 'python3 jarvis_main.py' &")

    def launch_radar(self):
        # Opens a lightweight browser to a flight radar site
        os.system("midori -a https://www.flightradar24.com &")

    def launch_notepad(self):
        os.system("leafpad &")

    def launch_games(self):
        os.system("lxterminal -e 'bastet' &")

    def launch_vlc(self):
        os.system("vlc &")

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisOS(root)
    root.mainloop()
