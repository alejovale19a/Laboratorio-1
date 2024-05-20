# setup.py
from tkinter import *
import tkinter as tk
from Tooltip import Tooltip
from Iconos import load_icons
import pygame.mixer as mx
from Reproductor import*

def setup_ventana(reproductor):
    
    reproductor.numCancion = 0
    reproductor.ventana = tk.Tk()
    reproductor.ventana.title("Super Reproductor")
    reproductor.ventana.config(width=800, height=500, bg="black")
    reproductor.ventana.resizable(0, 0)
    reproductor.canciones = [
        "sounds/chopsuey.mp3", "sounds/Slipknot.mp3", "sounds/kaijuC1.mp3",
        "sounds/CrimsonC2.mp3", "sounds/jujutsuC3.mp3", "sounds/shingekiC4.mp3",
        "sounds/blackCloverC5.mp3"
    ]

    mx.init()
    reproductor.bandera = False

    iconos = load_icons()

    labelImagen = tk.Label(reproductor.ventana, image=iconos["electro"])
    labelImagen.place(x=0, rely=0.15, width=512, height=440, y=-70)
    reproductor.volumen = Scale(reproductor.ventana, bg="red", to=100, from_=0, orient=HORIZONTAL, label="", command=reproductor.cambiarVolumen)
    reproductor.volumen.place(relx=0.72, rely=1, y=-50, width=80, height=35)

    reproductor.btnLista = tk.Button(reproductor.ventana, image=iconos["carpeta"], bg="gray")
    reproductor.btnLista.place(relx=0.05, rely=1, y=-50, width=35, height=35)
    Tooltip(reproductor.btnLista, "presiona para mostrar carpeta de canciones/Alt+z")

    reproductor.btnDevolver10 = tk.Button(reproductor.ventana, image=iconos["retroceder"], bg="green")
    reproductor.btnDevolver10.place(relx=0.33, rely=1, y=-50, width=35, height=35)
    Tooltip(reproductor.btnDevolver10, "presiona para retroceder 10 segundos/Alt+x")

    reproductor.btnAdelantar10 = tk.Button(reproductor.ventana, image=iconos["adelantar"], bg="green")
    reproductor.btnAdelantar10.place(relx=0.67, rely=1, y=-50, width=35, height=35)
    Tooltip(reproductor.btnAdelantar10, "presiona para adelantar 10 segundos/Alt+c")

    reproductor.btnDevolver = tk.Button(reproductor.ventana, image=iconos["devolver"], bg="green")
    reproductor.btnDevolver.place(relx=0.38, rely=1, y=-50, width=35, height=35)
    Tooltip(reproductor.btnDevolver, "presione para devolver a la cancion anterior/<---")

    reproductor.btnPasar = tk.Button(reproductor.ventana, image=iconos["pasar"], bg="green")
    reproductor.btnPasar.place(relx=0.62, rely=1, y=-50, width=35, height=35)
    Tooltip(reproductor.btnPasar, "presione para pasar a la siguiente cancion/--->")

    reproductor.btnPlay = tk.Button(reproductor.ventana, image=iconos["play"], bg="red")
    reproductor.btnPlay.place(relx=0.5, rely=1, y=-50, width=35, height=35)
    Tooltip(reproductor.btnPlay, "presione para iniciar reproduccion/Alt+r")

    reproductor.btnPause = tk.Button(reproductor.ventana, image=iconos["pausa"], state="disabled", bg="red")
    reproductor.btnPause.place(relx=0.5, rely=1, y=-50, x=50, width=35, height=35)
    Tooltip(reproductor.btnPause, "presione para pausar la reproduccion/Espacio")

    reproductor.btnStop = tk.Button(reproductor.ventana, image=iconos["stop"], state="disabled", bg="red")
    reproductor.btnStop.place(relx=0.5, rely=1, y=-50, x=-50, width=35, height=35)
    Tooltip(reproductor.btnStop, "presiona para detener la reproduccion/Alt+s")

    reproductor.lblestado = tk.Label(reproductor.ventana,justify="left",text="Cargando", bg="green")
    reproductor.lblestado.place(x=0, y=0, width=512)

    reproductor.btnPlay.bind("<Button-1>", reproductor.play)
    reproductor.ventana.bind("<Alt-r>", reproductor.play)

    reproductor.btnPause.bind("<Button-1>", reproductor.pause)
    reproductor.ventana.bind("<space>", reproductor.pause)
    reproductor.btnStop.bind("<Button-1>", reproductor.stop)
    reproductor.ventana.bind("<Alt-s>", reproductor.stop)
    reproductor.btnPasar.bind("<Button-1>", reproductor.pasar)
    reproductor.ventana.bind("<Right>", reproductor.pasar)
    reproductor.btnDevolver.bind("<Button-1>", reproductor.devolver)
    reproductor.ventana.bind("<Left>", reproductor.devolver)

    reproductor.btnAdelantar10.bind("<Button-1>", reproductor.adelantar10s)
    reproductor.ventana.bind("<Alt-c>", reproductor.adelantar10s)
    reproductor.btnDevolver10.bind("<Button-1>", reproductor.retroceder10s)
    reproductor.ventana.bind("<Alt-x>", reproductor.retroceder10s)
    reproductor.btnLista.bind("<Button-1>", reproductor.cargarlista)
    reproductor.ventana.bind("<Alt-z>", reproductor.cargarlista)

    reproductor.scale = tk.Scale(reproductor.ventana, orient=HORIZONTAL, length=400)
    reproductor.scale.place(relx=0.5, rely=0.89, width=800, height=30, anchor="s")
    reproductor.scale.bind("<B1-Motion>", reproductor.set_position)

    reproductor.time_label = tk.Label(reproductor.ventana, text="00:00", fg="white", bg="black")
    reproductor.time_label.place(relx=0.20, rely=1, y=-50)

    

        # Botón para cargar canciones
    


    reproductor.ventana.mainloop()
