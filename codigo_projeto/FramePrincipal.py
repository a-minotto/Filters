from tkinter import Tk
from tkinter import Label
from tkinter import Menu
from tkinter import filedialog
from tkinter import Frame
from tkinter import BOTH
from tkinter import LEFT

from PIL import Image, ImageTk

import numpy as np
import cv2

from Filtros import Filtros
from FrameFiltroMediana import FrameFiltroMediana
from FrameFiltroGaussiano import FrameFiltroGaussiano
from FrameFiltroSobel import  FrameFiltroSobel
from FrameFiltroCanny import FrameFiltroCanny
from FrameFiltroMedia import FrameFiltroMedia
from FrameFiltroBilateral import FrameFiltroBilateral
from FrameFiltroLaplaciano import FrameFiltroLaplaciano

import Config

class FramePrincipal:

    #-------------------------------------------------
    def __init__(self, root):

        self.root = root
        
        self.frame1 = None
        self.frame2 = None
        self.painel1 = None
        self.painel2 = None
        
        self.menubar = None
        self.arquivomenu = None
        self.suavizacaomenu = None
        self.realce = None
        self.helpmenu = None

        self.img_original = None
        self.img_alterada = None
   
    #-------------------------------------------------
    def __calcula_tamamho_imagem(self, img):
        
        self.root.update_idletasks() 
        largura_tela = self.root.winfo_width()
        altura_tela = self.root.winfo_height()
        largura_img, altura_img = img.size
        nova_largura = int(0.8 * (largura_tela/2))
        nova_altura = int((altura_img * nova_largura)/largura_img)  
        
        return nova_largura, nova_altura

    #-------------------------------------------------
    def __abre_imagem_frames(self, nome_arquivo):

        img = Image.open(nome_arquivo)
        largura, altura = self.__calcula_tamamho_imagem(img)
        
        img = img.resize( (largura, altura) )
        self.img_original = np.array(img)
        self.img_alterada = np.array(img)
        
        img_label = ImageTk.PhotoImage(img)
        self.painel1.configure(image = img_label)
        self.painel1.image = img_label
        self.painel2.configure(image = img_label)
        self.painel2.image = img_label
        
        self.menubar.entryconfig('Suavização', state='normal')
        self.menubar.entryconfig('Realce', state='normal')
        self.arquivomenu.entryconfig('Salvar', state='normal')
       
    #-------------------------------------------------
    def __seleciona_arquivo(self):
        
        tipos_arquivos = [
                        ('*.png', '*.png'), 
                        ('*.jpg',  '*.jpg'),
                        ('*.jpeg', '*.jpeg'),
                        ('*.bmp',  '*.bmp'),
                        ('*.gif', '*.gif'),
                        ('*.tiff' , '*.tiff')]
                       
        nome_arquivo = filedialog.askopenfilename(title='Abrir', initialdir='.', filetypes=tipos_arquivos)
        self.__abre_imagem_frames(nome_arquivo)
        return nome_arquivo

    #-------------------------------------------------
    def __salvar_arquivo(self):

        nome_arquivo = filedialog.asksaveasfilename(title='Salvar', filetypes=[('Portable Graphics Network (png)', '.png')],  defaultextension='.png')
        if nome_arquivo:
            img = Image.fromarray(self.img_alterada)
            img.save(nome_arquivo)
    
    #-------------------------------------------------
    def adiciona_frames(self):
        
        self.frame1 = Frame(self.root)
        self.frame1.pack(expand = True, fill = BOTH, side=LEFT)
        self.painel1 = Label(self.frame1, image = None)
        self.painel1.pack(side='bottom', fill='both', expand='yes')

        self.frame2 = Frame(self.root)
        self.frame2.pack(expand=True, fill=BOTH, side=LEFT)
        self.painel2 = Label(self.frame2, image = None)
        self.painel2.pack(side='bottom', fill='both', expand='yes')

    #-------------------------------------------------
    def adiciona_menu(self):
        
        self.menubar = Menu(self.root)
        self.arquivomenu = Menu(self.menubar, tearoff=0)
        self.arquivomenu.add_command(label='Abrir', command=self.__seleciona_arquivo)
        self.arquivomenu.add_command(label='Salvar', state = 'disable',  command=self.__salvar_arquivo)
        self.arquivomenu.add_separator()
        self.arquivomenu.add_command(label='Exit', command= self.root.quit)
        self.menubar.add_cascade(label='Arquivo', menu=self.arquivomenu)

        self.suavizacaomenu = Menu(self.menubar, tearoff=0)
        self.suavizacaomenu.add_cascade(label='Media', command=self.__executa_filtro_media)
        self.suavizacaomenu.add_cascade(label='Mediana', command= self.__executa_filtro_mediana)
        self.suavizacaomenu.add_command(label='Gaussiano', command= self.__executa_filtro_gaussiano)
        self.suavizacaomenu.add_command(label='Bilateral', command= self.__executa_filtro_bilateral)
        self.menubar.add_cascade(label='Suavização', state= 'disabled', menu=self.suavizacaomenu)

        self.realcemenu = Menu(self.menubar, tearoff=0)
        self.realcemenu.add_command(label='Laplaciano', command= self.__executa_filtro_laplaciano)
        self.realcemenu.add_command(label='Sobel', command= self.__executa_filtro_sobel)
        self.realcemenu.add_command(label='Canny', command= self.__executa_filtro_canny)
        self.menubar.add_cascade(label='Realce', state= 'disabled', menu=self.realcemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label='Sobre', command=None)
        self.menubar.add_cascade(label='Help', menu=self.helpmenu)

        self.root.config(menu=self.menubar)

    #-------------------------------------------------

    def __executa_filtro_media(self):
        
        titulo = 'Media'
        dimensao= Config.DIM_FRAME_MEDIA
        mascara_ini=Config.MASK_MEDIA_INI
        mascara_fim=Config.MASK_MEDIA_FIM
        mascara_default=Config.MASK_MEDIA_DEFAULT

        frame_media = FrameFiltroMedia(self).executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)
    
    #-------------------------------------------------
    def __executa_filtro_mediana(self):
        
        titulo = 'Mediana'
        dimensao= Config.DIM_FRAME_MEDIANA
        mascara_ini=Config.MASK_MEDIANA_INI
        mascara_fim=Config.MASK_MEDIANA_FIM
        mascara_default=Config.MASK_MEDIANA_DEFAULT
        
        frame_mediana = FrameFiltroMediana(self).executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)
    
    #-------------------------------------------------
    def __executa_filtro_gaussiano(self):

        titulo = 'Gaussiano'
        dimensao= Config.DIM_FRAME_GAUSSIANO
        mascara_ini=Config.MASK_GAUSSIANO_INI
        mascara_fim=Config.MASK_GAUSSIANO_FIM
        mascara_default=Config.MASK_GAUSSIANO_DEFAULT
        
        frame_gaussiano = FrameFiltroGaussiano(self).executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)

    #-------------------------------------------------
    def __executa_filtro_bilateral(self):

        titulo = 'Bilateral'
        dimensao= Config.DIM_FRAME_BILATERAL
        mascara_ini=Config.MASK_BILATERAL_INI
        mascara_fim=Config.MASK_BILATERAL_FIM
        mascara_default=Config.MASK_BILATERAL_DEFAULT
        
        frame_bilateral = FrameFiltroBilateral(self).executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)

    #-------------------------------------------------
    def __executa_filtro_laplaciano(self):
        
        titulo = 'LAPLACIANO'
        dimensao= Config.DIM_FRAME_LAPLACIANO
        mascara_ini=Config.MASK_LAPLACIANO_INI
        mascara_fim=Config.MASK_LAPLACIANO_FIM
        mascara_default=Config.MASK_LAPLACIANO_DEFAULT
        
        self.img_alterada  = FrameFiltroLaplaciano(self).executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)
       
    #-------------------------------------------------
    def __executa_filtro_sobel(self):
        
        titulo = 'Sobel'
        dimensao= Config.DIM_FRAME_SOBEL
        mascara_ini=Config.MASK_SOBEL_INI
        mascara_fim=Config.MASK_SOBEL_FIM
        mascara_default=Config.MASK_SOBEL_DEFAULT

        frame_sobel = FrameFiltroSobel(self).executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)

    #-------------------------------------------------
    def __executa_filtro_canny(self):

        titulo = 'Canny'
        dimensao= Config.DIM_FRAME_CANNY
        mascara_ini=Config.MASK_CANNY_INI
        mascara_fim=Config.MASK_CANNY_FIM
        mascara_default=Config.MASK_CANNY_DEFAULT

        frame_canny = FrameFiltroCanny(self).executa_frame_filtro(titulo, dimensao, mascara_ini, mascara_fim, mascara_default)

    #-------------------------------------------------
    