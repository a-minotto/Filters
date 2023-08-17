from tkinter import Label
from tkinter import Scale
from tkinter import HORIZONTAL
from tkinter import CENTER

import tkinter as tk

from  Filtros import Filtros

import Config
import FrameFiltro

class FrameFiltroBilateral(FrameFiltro.FrameFiltro):

    #----------------------------------------------
    def __init__(self, principal):
        super().__init__(principal)
        self.escala_sigma = None

    #----------------------------------------------
    def updateValue(self, event):
        mascara = self.escala.get()
        sigma = self.escala_sigma.get()

        self.principal.img_alterada = Filtros().filtro_bilateral(self.principal.img_original, mascara, sigma)
        super().updateValue(event)
    
    #----------------------------------------------
    def executa_frame_filtro(self, titulo, dimensao, mascara_ini, mascara_fim, mascara_default):

        self.principal.img_alterada = Filtros().filtro_bilateral(self.principal.img_original, mascara_default, Config.SIGMA_BILATERAL_DEFAULT)
        super().executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)
        
        label_sigma = Label(self.secudaria, text='Sigma:')
        label_sigma.config(font=('Arial', 10))
        label_sigma.grid(row=1, column=0, sticky=tk.SW)

        self.escala_sigma = Scale(self.secudaria, length=Config.ESCALA_PIXELS, resolution=Config.SIGMA_BILATERAL_INC, from_= Config.SIGMA_BILATERAL_INI, to=Config.SIGMA_BILATERAL_FIM, orient = HORIZONTAL)
        self.escala_sigma.config(font=('Arial', 8))
        self.escala_sigma.set(Config.SIGMA_BILATERAL_DEFAULT)
        self.escala_sigma.bind("<ButtonRelease-1>", self.updateValue)
        self.escala_sigma.grid(row=1, column=1)
            
        super().atualiza_imagem_alterada()

    #----------------------------------------------
        


    