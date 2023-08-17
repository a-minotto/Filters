from tkinter import Label
from tkinter import Scale
from tkinter import HORIZONTAL
from tkinter import CENTER

import tkinter as tk

from  Filtros import Filtros

import Config
import FrameFiltro

class FrameFiltroGaussiano(FrameFiltro.FrameFiltro):

    #----------------------------------------------
    def __init__(self, principal):
        super().__init__(principal)
        
    #----------------------------------------------
    def updateValue(self, event):
        mascara = self.escala.get()
        self.principal.img_alterada = Filtros().filtro_gaussiano(self.principal.img_original, mascara)
        super().updateValue(event)
    
    #----------------------------------------------
    def executa_frame_filtro(self, titulo, dimensao, mascara_ini, mascara_fim, mascara_default):

        self.principal.img_alterada = Filtros().filtro_gaussiano(self.principal.img_original, mascara_default)
        super().executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)
        super().atualiza_imagem_alterada()

    #----------------------------------------------
        


    