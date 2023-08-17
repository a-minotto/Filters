import cv2

class Filtros:

    #--------------------------------------
    def __init__(self):
        pass

    
    #--------------------------------------
    def filtro_media(self, img, mascara):
    
        media = cv2.blur(img,(mascara,mascara))
        return media 

    #--------------------------------------
    
    def filtro_mediana(self, img, mascara):
    
        mediana = cv2.medianBlur(img, mascara)
        return mediana
    
    #--------------------------------------
    def filtro_gaussiano(self, img, mascara):
    
        gaussiano = cv2.GaussianBlur(img,(mascara,mascara), 0)
        return gaussiano

    #--------------------------------------
    
    def filtro_bilateral(self, img, mascara, sigma):
    
        bilateral = cv2.bilateralFilter(img, mascara, sigma, sigma)
        return bilateral
    
    #--------------------------------------
    
    def filtro_laplaciano(self, img, mascara):
    
        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        suavizada = cv2.GaussianBlur(cinza, (3,3), 0) 
        laplaciano = cv2.Laplacian(suavizada, cv2.CV_8U,  ksize=mascara) 
        return laplaciano
    
    #--------------------------------------
    
    def filtro_sobel(self, img, mascara):
    
        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        suavizada = cv2.GaussianBlur(cinza, (3,3), 0) 
        sobel = cv2.Sobel(suavizada, ddepth=cv2.CV_8U, dx=1, dy=1, ksize=mascara) 
        return sobel

    #--------------------------------------
    
    def filtro_canny(self, img, mascara, thr_inf, thr_sup):
    
        canny = cv2.Canny(img, thr_inf, thr_sup, 200, apertureSize= mascara)
        return canny
    
    #--------------------------------------
    