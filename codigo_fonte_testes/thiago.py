from copy import copy

import sys
import cv2
import numpy as np


#-----------------------------------------
def mediana(img, mascara):
    img_mediana = cv2.medianBlur(img, mascara)
    return img_mediana

#-----------------------------------------
def gaussiano(img, mascara):
    img_gaussiano = cv2.GaussianBlur(src=img,ksize=(mascara, mascara),sigmaX=0)
    return img_gaussiano

#-----------------------------------------
def mediana(img, mascara):
    img_mediana = cv2.medianBlur(img, mascara)
    return img_mediana

#-----------------------------------------
def bilateral(img, mascara):
    
    img_bilateral = cv2.bilateralFilter(img, mascara,75,75)
    return img_bilateral

#-----------------------------------------
def canny(img, thr1, thr2):
    
    arestas = cv2.Canny(img, thr1, thr2)
    return arestas

#-----------------------------------------
def laplaciano(img, mascara):
    img_laplaciano = cv2.Laplacian(img, ddepth=cv2.CV_64F, ksize=mascara)
    img_laplaciano = np.uint8(img_laplaciano)
    return img_laplaciano

#-----------------------------------------
def sobel(img, mascara):
    sobel_x = cv2.Sobel(img, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=mascara)
    sobel_y = cv2.Sobel(img, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=mascara)

    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    sobel_comb = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    return sobel_x, sobel_y, sobel_comb

#-----------------------------------------
def equalizacao(img):
    equ = cv2.equalizeHist(img)
    return equ

#-----------------------------------------
def equalizacao_clahe(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_clahe = clahe.apply(img)
    return img_clahe

#-----------------------------------------
def nitidez(img):
    kernel = np.array([ [0, -1,  0],
                        [-1,  5, -1],
                        [0, -1,  0] ] )
    img_nitidez = cv2.filter2D(img, ddepth=-1, kernel=kernel)
    return img_nitidez
    
#-----------------------------------------
def mostra_imagens(lista_imagens):
    
    parte1 = np.hstack(lista_imagens[0:4])
    parte2 = np.hstack(lista_imagens[4:8])
    parte3 = np.hstack(lista_imagens[8:12])
    
    final = np.vstack((parte1, parte2, parte3))
    cv2.imshow('final', final)
    cv2.imwrite('cervical.jpg', final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#-----------------------------------------
def main(arquivo_img):
    
    lista_imagens = []

    img = cv2.imread(arquivo_img, cv2.IMREAD_GRAYSCALE)
    lista_imagens.append(img)

    img_gaussiano = gaussiano(img, mascara = 3)
    lista_imagens.append(img_gaussiano)

    img_mediana = mediana(img, mascara = 3)
    lista_imagens.append(img_mediana)

    img_bilatereal = bilateral(img, mascara = 3)
    lista_imagens.append(img_bilatereal)

    img_canny = canny(img, thr1=20, thr2=30)
    lista_imagens.append(img_canny)

    img_laplaciano = laplaciano(img, mascara=3)
    lista_imagens.append(img_laplaciano)
    
    sobel_x, sobel_y, sobel_comb = sobel(img, mascara = -1)
    lista_imagens.append(sobel_x)
    lista_imagens.append(sobel_y)
    lista_imagens.append(sobel_comb)

    img_equ = equalizacao(img)
    lista_imagens.append(img_equ)
      
    img_clahe = equalizacao_clahe(img)
    lista_imagens.append(img_clahe)
    
    img_nitidez = nitidez(img)
    lista_imagens.append(img_nitidez)
    
    mostra_imagens(lista_imagens)
    
#-----------------------------------------
if __name__ == '__main__':
    
    #if len(sys.argv) != 2:
    #    print('%s <imagem>' % sys.argv[0]) 
    #    sys.exit(0)
    main('cervical.jpg')
    #main(sys.argv[1])
