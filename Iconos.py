# icons.py

import tkinter as tk

def load_icons():
    iconos = {
        "play": tk.PhotoImage(file=r"icons\icons\control_play.png"),
        "pausa": tk.PhotoImage(file=r"icons\icons\control_pause_blue.png"),
        "stop": tk.PhotoImage(file=r"icons\icons\control_stop_blue.png"),
        "pasar": tk.PhotoImage(file=r"icons\icons\control_end_blue.png"),
        "devolver": tk.PhotoImage(file=r"icons\icons\control_start_blue.png"),
        "adelantar": tk.PhotoImage(file=r"icons\icons\control_fastforward_blue.png"),
        "retroceder": tk.PhotoImage(file=r"icons\icons\control_rewind_blue.png"),
        "electro": tk.PhotoImage(file="icons\icons\electro.png"),
        "carpeta": tk.PhotoImage(file=r"icons\icons\folder.png")
    }
    return iconos
