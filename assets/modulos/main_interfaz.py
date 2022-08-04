import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
from assets.modulos.parametros import COLOR_BG, COLOR_SECUNDARIO, COLOR_BOTONES, COLOR_TITULOS, LOGO, LENGUAJE
from assets.modulos.idioma import seleccionIdioma
from assets.modulos.idioma import asignarTEXTOS
from assets.modulos.repositorio import irRepositorio
from assets.modulos.criptomonedas import criptomonedas

def interfaz(TITULO_VENTANA):
    root = tk.Tk()
    root.title(TITULO_VENTANA)
    root.iconbitmap(LOGO+".ico")
    root.resizable(False,False)
    TITULO_FUENTE = Font(family="Roboto", size=20)
    TEXTO_FUENTE = Font(family="Roboto", size=15)   
    
    header = tk.Canvas(root, width=450, height=60, bg=COLOR_SECUNDARIO)
    header.grid(column=1,row=1)

    titulo = tk.Label(root, text="Fresh Prices", font=TITULO_FUENTE, bg=COLOR_SECUNDARIO, fg=COLOR_TITULOS)
    titulo.grid(column=1, row=1) 

    canvas = tk.Canvas(root, width=450, height=450, bg=COLOR_BG)
    canvas.grid(columnspan=3, rowspan=12)
    
    logo = Image.open(LOGO+".png")
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo, bg=COLOR_BG)
    logo_label.image = logo
    logo_label.grid(columnspan=3, column=0, row=2)

    textoBTN = tk.StringVar()
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:menucriptomonedas(root), fg=COLOR_BG, font=TEXTO_FUENTE, bg=COLOR_BOTONES, width=8)
    textoBTN.set(asignarTEXTOS("Iniciar",LENGUAJE.IDIOMA_ACTUAL))
    btn_Iniciar.grid(column=1, row=3)

    textoBTN = tk.StringVar()
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:cambiarIdioma(root), fg=COLOR_BG, font=TEXTO_FUENTE, bg=COLOR_BOTONES, width=16)
    textoBTN.set(asignarTEXTOS("Cambiar Idioma",LENGUAJE.IDIOMA_ACTUAL))
    btn_Iniciar.grid(column=1, row=6)

    textoBTN = tk.StringVar()
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:irRepositorio(), fg=COLOR_BG, font=TEXTO_FUENTE, bg=COLOR_BOTONES, width=10)
    textoBTN.set(asignarTEXTOS("Repositorio",LENGUAJE.IDIOMA_ACTUAL))
    btn_Iniciar.grid(column=1, row=9)

    root.mainloop()

def cambiarIdioma(root):
    root.destroy()
    seleccionIdioma()

def menucriptomonedas(root):
    root.destroy()
    criptomonedas()

