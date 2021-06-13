from tkinter import *

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= 'gray')
        self.root.resizable(True, True)
    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= 'white', highlightbackground= 'black', highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)
        self.frame_2 = Frame(self.root, bd = 4, bg= 'white', highlightbackground= 'black', highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)



Application()
