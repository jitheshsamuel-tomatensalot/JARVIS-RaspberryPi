import tkinter as tk
import os
import subprocess
from datetime import datetime
from PIL import Image, ImageTk

# --- CONFIGURATION ---
WALLPAPER_PATH = "wallpaper.jpg" 
ARC_REACTOR_PATH = "arc_reactor.png"
LANGS = ["English", "French", "German", "Russian", "Malayalam"]

class JarvisOS:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS OS v1.2")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.lang_idx = 0

        # Force focus and keep on top for 'OS' feel
        self.root.focus_set()
        
        # Load Wallpaper
        if os.path.exists(WALLPAPER_PATH):
            try:
                self.bg_image = Image.open(WALLPAPER_PATH)
                self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
                self.bg_photo = ImageTk.PhotoImage(self.bg_image)
                self.bg_label = tk.Label(self.root, image=self.bg_photo)
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            except Exception: pass

        self.color = "#00d4ff"
        
        # --- Header Section ---
        header_frame = tk.Frame(self.root, bg='black', pady=20)
        header_frame.pack(side="top", fill="x")
        
        self.time_label = tk.Label(header_frame, font=('Courier', 60, 'bold'), fg=self.color, bg='black')
        self.time_label.pack()
        self.update_time()

        tk.Label(header_frame, text="STARK INDUSTRIES - JARVIS OS v1.2", font=('Courier', 12), fg=self.color, bg='black').pack()

        # --- Center Section: Arc Reactor ---
        center_frame = tk.Frame(self.root, bg='black')
        center_frame.pack(expand=True)

        if os.path.exists(ARC_REACTOR_PATH):
            try:
                arc_img = Image.open(ARC_REACTOR_PATH).resize((350, 350))
                self.arc_photo = ImageTk.PhotoImage(arc_img)
                tk.Label(center_frame, image=self.arc_photo, bg='black').pack()
            except Exception: 
                tk.Label(center_frame, text="[ ARC REACTOR OFFLINE ]", font=('Courier', 20), fg=self.color, bg='black').pack()
        else:
            tk.Label(center_frame, text="[ ARC REACTOR OFFLINE ]", font=('Courier', 20), fg=self.color, bg='black').pack()

        # --- Left Side: Controls ---
        left_frame = tk.Frame(self.root, bg='black', padx=50)
        left_frame.place(relx=0.05, rely=0.5, anchor="w")

        self.create_button(left_frame, "LAUNCH JARVIS AI", self.launch_ai)
        self.lang_btn = self.create_button(left_frame, f"LANGUAGE: {LANGS[self.lang_idx]}", self.toggle_lang)
        self.create_button(left_frame, "GAMES", self.launch_games)
        self.create_button(left_frame, "EXIT", self.root.destroy)

        # --- Status Bar (Bottom) ---
        status_frame = tk.Frame(self.root, bg='black', pady=10)
        status_frame.pack(side="bottom", fill="x")

        self.wifi_label = tk.Label(status_frame, text="WIFI: SCANNING...", font=('Courier', 10), fg=self.color, bg='black')
        self.wifi_label.pack(side="left", padx=20)

        self.audio_label = tk.Label(status_frame, text="AUDIO: SCANNING...", font=('Courier', 10), fg=self.color, bg='black')
        self.audio_label.pack(side="right", padx=20)

        self.update_status()

    def create_button(self, parent, text, command):
        btn = tk.Button(parent, text=text, command=command, font=('Courier', 14, 'bold'), 
                        fg='black', bg=self.color, width=20, pady=10)
        btn.pack(pady=10)
        return btn

    def update_time(self):
        self.time_label.config(text=datetime.now().strftime("%H:%M:%S"))
        self.root.after(1000, self.update_time)

    def update_status(self):
        try:
            cmd = "iwconfig wlan0 | grep -i quality"
            res = subprocess.check_output(cmd, shell=True).decode("utf-8")
            self.wifi_label.config(text=f"WIFI: {res.strip()}")
        except: self.wifi_label.config(text="WIFI: OFFLINE")

        try:
            mic = subprocess.check_output("arecord -l | grep 'card'", shell=True).decode("utf-8").split('\n')[0][:20]
            spk = subprocess.check_output("aplay -l | grep 'card'", shell=True).decode("utf-8").split('\n')[0][:20]
            self.audio_label.config(text=f"IN: {mic} | OUT: {spk}")
        except: self.audio_label.config(text="AUDIO: ERROR")

        self.root.after(5000, self.update_status)

    def toggle_lang(self):
        self.lang_idx = (self.lang_idx + 1) % len(LANGS)
        self.lang_btn.config(text=f"LANGUAGE: {LANGS[self.lang_idx]}")
        with open("lang.txt", "w") as f: f.write(LANGS[self.lang_idx])

    def launch_ai(self): os.system("lxterminal -e 'python3 jarvis_core.py' &")
    def launch_games(self): os.system("lxterminal -e 'bastet' &")

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisOS(root)
    root.mainloop()
