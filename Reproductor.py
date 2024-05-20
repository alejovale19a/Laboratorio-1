from tkinter import*
from tkinter import messagebox 
from Tooltip import*
import pygame.mixer as mx
from setup import setup_ventana
import tkinter.filedialog as fd



class Reproductor():       
    def play(self,event):
        if not self.bandera:
            if not mx.music.get_busy(): 
                mx.music.load(self.canciones[self.numCancion])
                mx.music.play()

                volumen = self.volumen.get() / 100
                mx.music.set_volume(volumen)
                titulo_cancion = self.canciones[self.numCancion].split("\\")[-1]
                duracion_cancion = mx.Sound(self.canciones[self.numCancion]).get_length()
                self.lblestado.config(text=f"Reproduciendo: {titulo_cancion} ({duracion_cancion:.2f} segundos)")
                self.btnPause.config(state="normal")
                self.btnStop.config(state="normal")
                self.btnPlay.config(state="disabled")
                self.update_time()
                
        else:
            mx.music.unpause()
            titulo_cancion = self.canciones[self.numCancion].split("\\")[-1]
            duracion_cancion = mx.Sound(self.canciones[self.numCancion]).get_length()
            self.lblestado.config(text=f"Reproduciendo: {titulo_cancion} ({duracion_cancion:.2f} segundos)")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.bandera= False

    def pause(self,event):
        if self.bandera==False:
            mx.music.pause()
            titulo_cancion = self.canciones[self.numCancion].split("\\")[-1]
            duracion_cancion = mx.Sound(self.canciones[self.numCancion]).get_length()
            self.lblestado.config(text=f"pausado: {titulo_cancion} ({duracion_cancion:.2f} segundos)")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.bandera=True
        else:
            mx.music.unpause()
            
            titulo_cancion = self.canciones[self.numCancion].split("\\")[-1]
            duracion_cancion = mx.Sound(self.canciones[self.numCancion]).get_length()
            self.lblestado.config(text=f"Reproduciendo: {titulo_cancion} ({duracion_cancion:.2f} segundos)")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")   
            self.bandera=False       

    def stop(self,event):
        mx.music.stop()
        self.lblestado.config(text="detenido")
        self.btnPause.config(state="disabled")
        self.btnStop.config(state="disabled")
        self.btnPlay.config(state="normal")

    def pasar(self, event):

        self.numCancion += 1
       
        if self.numCancion < len(self.canciones):
            
            mx.music.load(self.canciones[self.numCancion])
            mx.music.play()
            titulo_cancion = self.canciones[self.numCancion].split("\\")[-1]
            duracion_cancion = mx.Sound(self.canciones[self.numCancion]).get_length()
            self.lblestado.config(text=f"Reproduciendo: {titulo_cancion} ({duracion_cancion:.2f} segundos)")
        else:
            messagebox.showinfo("Información", "¡Ya estás en la última canción de la lista!")
            
            self.numCancion -= 1
    def devolver(self, event):
        self.numCancion -= 1
        if 0 <= self.numCancion < len(self.canciones):
            mx.music.load(self.canciones[self.numCancion])
            mx.music.play()
            titulo_cancion = self.canciones[self.numCancion].split("//")[-1]
            duracion_cancion = mx.Sound(self.canciones[self.numCancion]).get_length()
            self.lblestado.config(text=f"Reproduciendo: {titulo_cancion} ({duracion_cancion:.2f} segundos)")
        else:
            messagebox.showinfo("Información", "¡Ya estás en la primera canción de la lista!")
            self.numCancion += 1

    def adelantar10s(self, event):
        posicion = mx.music.get_pos() / 100 
        newP = posicion + 10  
        mx.music.set_pos(newP)
        

    def retroceder10s(self,event):
        posicion = mx.music.get_pos() / 100 
        newP = posicion - 10  
        mx.music.set_pos(newP)  
       

    def cambiarVolumen(self, event):
        volumen = self.volumen.get() / 100
        mx.music.set_volume(volumen)
    
    def cargarlista(self,event):
        filenames = fd.askopenfilenames(filetypes=[("Archivos MP3", "*.mp3"), ("Todos los archivos", "*.*")])
        self.listbox = Listbox(self.ventana, bg="gray")
        self.listbox.place(x=512, y=0, width=288, height=417)
        if filenames:
            self.canciones = list(filenames)
            self.listbox.delete(0, END)  # Borra las canciones existentes en la Listbox
            for cancion in self.canciones:
                self.listbox.insert(END, cancion)
    
    def update_time(self):
        if mx.music.get_busy():
            current_time = mx.music.get_pos() / 1000  # obtener la posición actual en segundos
            self.scale.set(current_time)
            self.ventana.after(1000, self.update_time)  # actualizar cada segundo
            minutes, seconds = divmod(current_time, 60)
            time_str = f"{int(minutes):02d}:{int(seconds):02d}"
            self.time_label.config(text=time_str)

    def set_position(self, event):
        new_pos = self.scale.get() 
        mx.music.play(start=new_pos)  # Reproducir desde la nueva posición
        self.update_time()
        self.scale.set(new_pos / 1000)
        minutes, seconds = divmod(new_pos, 60)
        time_str = f"{int(minutes):02d}:{int(seconds):02d}"
        self.time_label.config(text=time_str)

    def __init__(self):
        setup_ventana(self)


