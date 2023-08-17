from tkinter import Label
from tkinter import Scale
from tkinter import HORIZONTAL
from tkinter import CENTER

import tkinter as tk

from Filtros import Filtros

import Config
import FrameFiltro

class FrameFiltroCanny(FrameFiltro.FrameFiltro):

    #----------------------------------------------
    def __init__(self, principal):

        super().__init__(principal)
        self.escala_thr_inf = None
        self.escala_thr_sup = None
    
    #----------------------------------------------
    def updateValue(self, event):

        mascara = self.escala.get()
        thr_inf = self.escala_thr_inf.get()
        thr_sup = self.escala_thr_sup.get()
        self.principal.img_alterada = Filtros().filtro_canny(self.principal.img_original, mascara, thr_inf, thr_sup)
        super().updateValue(event)
        
    #----------------------------------------------
    def executa_frame_filtro(self, titulo, dimensao, mascara_ini, mascara_fim, mascara_default):
        
        self.principal.img_alterada = Filtros().filtro_canny(self.principal.img_original, mascara_default, Config.THR_CANNY_INF_DEFAULT, Config.THR_CANNY_SUP_DEFAULT)
        super().executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)
        
        label_inf = Label(self.secudaria, text='Threshold inferior:')
        label_inf.config(font=('Arial', 10))
        label_inf.grid(row=1, column=0, sticky=tk.SW)

        self.escala_thr_inf = Scale(self.secudaria, length=Config.ESCALA_PIXELS, resolution=Config.THR_CANNY_INC, from_= Config.THR_CANNY_INF_INI, to=Config.THR_CANNY_INF_FIM, orient = HORIZONTAL)
        self.escala_thr_inf.config(font=('Arial', 8))
        self.escala_thr_inf.set(Config.THR_CANNY_INF_DEFAULT)
        self.escala_thr_inf.bind("<ButtonRelease-1>", self.updateValue)
        self.escala_thr_inf.grid(row=1, column=1)
               
        label_sup = Label(self.secudaria, text='Threshold superior:')
        label_sup.config(font=('Arial', 10))
        label_sup.grid(row=2, column=0, sticky=tk.SW)

        self.escala_thr_sup = Scale(self.secudaria, length=Config.ESCALA_PIXELS, resolution=Config.THR_CANNY_INC, from_= Config.THR_CANNY_SUP_INI, to=Config.THR_CANNY_SUP_FIM, orient = HORIZONTAL)
        self.escala_thr_sup.config(font=('Arial', 8))
        self.escala_thr_sup.set(Config.THR_CANNY_SUP_DEFAULT)
        self.escala_thr_sup.bind("<ButtonRelease-1>", self.updateValue)
        self.escala_thr_sup.grid(row=2, column=1)
        
        super().atualiza_imagem_alterada()

    #----------------------------------------------
