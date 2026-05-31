import tkinter as tk
import os
from datetime import datetime

WALLPAPER_PATH = "wallpaper.jpg" 
LANGS = ["English", "French", "German", "Russian", "Malayalam"]

class JarvisOS:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS OS Shell")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.lang_idx = 0

        # Load Wallpaper
        if os.path.exists(WALLPAPER_PATH):
            try:
                from PIL import Image, ImageTk
                self.bg_image = Image.open(WALLPAPER_PATH)
                self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
                self.bg_photo = ImageTk.PhotoImage(self.bg_image)
                self.bg_label = tk.Label(self.root, image=self.bg_photo)
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            except Exception: pass

        self.color = "#00d4ff"
        self.time_label = tk.Label(self.root, font=('Courier', 40, 'bold'), fg=self.color, bg='black')
        self.time_label.pack(pady=20)
        self.update_time()

        menu_frame = tk.Frame(self.root, bg='black')
        menu_frame.pack(expand=True)

        self.create_button(menu_frame, "LAUNCH JARVIS AI", self.launch_ai)
        self.lang_btn = self.create_button(menu_frame, f"LANGUAGE: {LANGS[self.lang_idx]}", self.toggle_lang)
        self.create_button(menu_frame, "FLIGHT RADAR", self.launch_radar)
        self.create_button(menu_frame, "GAMES", self.launch_games)
        self.create_button(menu_frame, "EXIT", self.root.destroy)

    def create_button(self, parent, text, command):
        btn = tk.Button(parent, text=text, command=command, font=('Courier', 14, 'bold'), 
                        fg='black', bg=self.color, width=20, pady=10)
        btn.pack(pady=10)
        return btn

    def update_time(self):
        self.time_label.config(text=datetime.now().strftime("%H:%M:%S"))
        self.root.after(1000, self.update_time)

    def toggle_lang(self):
        self.lang_idx = (self.lang_idx + 1) % len(LANGS)
        self.lang_btn.config(text=f"LANGUAGE: {LANGS[self.lang_idx]}")
        with open("lang.txt", "w") as f: f.write(LANGS[self.lang_idx])

    def launch_ai(self): os.system("lxterminal -e 'python3 jarvis_core.py' &")
    def launch_radar(self): os.system("midori -a https://www.flightradar24.com &")
    def launch_games(self): os.system("lxterminal -e 'bastet' &")

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisOS(root)
    root.mainloop()
