import tkinter as tk
import os
import math
import requests
from datetime import datetime

# --- CONFIGURATION ---
WALLPAPER_PATH = "wallpaper.jpg" 
LANGS = ["English", "French", "German", "Russian", "Malayalam"]

# RADAR CONFIG (Change these to your home coordinates!)
HOME_LAT = 10.8505 # Kerala center approx
HOME_LON = 76.2711
RADIUS_KM = 40

class JarvisOS:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS OS Shell")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.lang_idx = 0
        self.planes = []

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
        
        # --- Left Side: Controls ---
        left_frame = tk.Frame(self.root, bg='black', padx=50)
        left_frame.pack(side="left", fill="y")

        self.time_label = tk.Label(left_frame, font=('Courier', 40, 'bold'), fg=self.color, bg='black')
        self.time_label.pack(pady=20)
        self.update_time()

        tk.Label(left_frame, text="STARK INDUSTRIES - JARVIS OS", font=('Courier', 12), fg=self.color, bg='black').pack(pady=10)

        self.create_button(left_frame, "LAUNCH JARVIS AI", self.launch_ai)
        self.lang_btn = self.create_button(left_frame, f"LANGUAGE: {LANGS[self.lang_idx]}", self.toggle_lang)
        self.create_button(left_frame, "GAMES", self.launch_games)
        self.create_button(left_frame, "EXIT", self.root.destroy)

        # --- Right Side: Mini Flight Radar ---
        right_frame = tk.Frame(self.root, bg='black', padx=20)
        right_frame.pack(side="right", fill="both", expand=True)

        tk.Label(right_frame, text="FLIGHT RADAR (40KM)", font=('Courier', 14, 'bold'), fg=self.color, bg='black').pack(pady=10)
        
        self.canvas = tk.Canvas(right_frame, width=400, height=400, bg="black", highlightthickness=1, highlightbackground=self.color)
        self.canvas.pack(pady=20)

        self.draw_radar_grid()
        self.update_radar()

    def create_button(self, parent, text, command):
        btn = tk.Button(parent, text=text, command=command, font=('Courier', 14, 'bold'), 
                        fg='black', bg=self.color, width=20, pady=10)
        btn.pack(pady=10)
        return btn

    def update_time(self):
        self.time_label.config(text=datetime.now().strftime("%H:%M:%S"))
        self.root.after(1000, self.update_time)

    def draw_radar_grid(self):
        self.canvas.delete("all")
        cx, cy = 200, 200
        # Draw Rings
        for r in [50, 100, 150, 190]:
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#004455", width=1)
        # Draw Crosshair
        self.canvas.create_line(cx, 10, cx, 390, fill="#004455")
        self.canvas.create_line(10, cy, 390, cy, fill="#004455")
        self.canvas.create_text(cx, cy+200, text="HOME", fill=self.color, font=("Courier", 8))

    def update_radar(self):
        # OpenSky API Bounding Box (Approx 40km)
        # Lat: 1 deg ~ 111km. 40km ~ 0.36 deg
        lat_min, lat_max = HOME_LAT - 0.36, HOME_LAT + 0.36
        lon_min, lon_max = HOME_LON - 0.36, HOME_LON + 0.36
        
        try:
            url = f"https://opensky-network.org/api/states/all?lamin={lat_min}&lamin={lat_min}&lamax={lat_max}&lomin={lon_min}&lomax={lon_max}"
            r = requests.get(url, timeout=5)
            data = r.json()
            self.draw_radar_grid()
            if data['states']:
                for s in data['states']:
                    # s[6] = lon, s[5] = lat
                    px = 200 + (s[6] - HOME_LON) * (200/0.36)
                    py = 200 - (s[5] - HOME_LAT) * (200/0.36)
                    self.canvas.create_oval(px-3, py-3, px+3, py+3, fill="red", outline=self.color)
                    self.canvas.create_text(px, py-10, text=s[1], fill=self.color, font=("Courier", 8))
        except Exception as e:
            print(f"Radar error: {e}")
        
        # Update every 30 seconds to stay within free API limits
        self.root.after(30000, self.update_radar)

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
