from tkinter import Tk
from FramePrincipal import FramePrincipal
from Filtros import Filtros

#-------------------------------------------------
def main():

    root = Tk()
    #window_width = 940
    #window_height = 625

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = 0 #int(screen_width/2) # - window_width / 2)
    center_y = 0 #int(screen_height/2) # - window_height / 2)

    # set the position of the window to the center of the screen
    #root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
	
    #root.geometry("%dx%d" % (screen_width-2, screen_height-10))

    root.resizable(False, False)

    principal = FramePrincipal(root)
    principal.adiciona_menu()
    principal.adiciona_frames()

    root.mainloop()

#-------------------------------------------------
if __name__ == '__main__':
    main()

    
