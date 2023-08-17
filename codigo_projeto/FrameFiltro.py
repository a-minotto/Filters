from tkinter import Toplevel
from tkinter import Label
from tkinter import Scale
from tkinter import HORIZONTAL
from tkinter import CENTER

import tkinter as tk

from PIL import Image, ImageTk

import Config 

class FrameFiltro:

    #----------------------------------------------
    def __init__(self, principal):

        self.principal = principal 
        self.secudaria = None
        self.escala = None

    #----------------------------------------------
    def executa_frame_filtro(self, titulo, dimensao, mascara_ini, mascara_fim, mascara_default):
        
        self.secudaria = Toplevel()
        self.secudaria.resizable(False,False)

        self.secudaria.title('Filtro:  ' + titulo)
        self.secudaria.geometry(dimensao)
    
        label = Label(self.secudaria, text='Máscara:')
        label.config(font=('Arial', 10))
        label.grid(row=0, column=0, sticky=tk.SW)

        self.escala = Scale(self.secudaria, length=Config.ESCALA_PIXELS, resolution=Config.INC_MASK, from_= mascara_ini, to=mascara_fim, orient = HORIZONTAL)
        self.escala.config(font=('Arial', 8))
        self.escala.set(mascara_default)
        self.escala.bind("<ButtonRelease-1>", self.updateValue)
        self.escala.grid(row=0, column=1)
       
    #----------------------------------------------
    def updateValue(self, event):

        self.atualiza_imagem_alterada()

    #----------------------------------------------
    def atualiza_imagem_alterada(self):

        img_label = ImageTk.PhotoImage(Image.fromarray(self.principal.img_alterada))        
        self.principal.painel2.configure(image = img_label)
        self.principal.painel2.image = img_label
    