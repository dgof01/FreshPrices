import tkinter as tk
from tkinter.font import Font
from assets.modulos.parametros import COLOR_BG, COLOR_SECUNDARIO, COLOR_BOTONES, COLOR_TITULOS, LOGO, LENGUAJE
from assets.modulos.idioma import asignarTEXTOS

def regresar(root):
    root.destroy()
    from assets.modulos.criptomonedas import criptomonedas
    criptomonedas()

def error():
    root = tk.Tk()
    root.title("Error")
    root.iconbitmap(LOGO+".ico")
    root.resizable(False,False)
    TITULO_FUENTE = Font(family="Roboto", size=12)
    TEXTO_FUENTE = Font(family="Roboto", size=12)   
    
    canvas = tk.Canvas(root, width=650, height=100, bg=COLOR_BG)
    canvas.grid(columnspan=3, rowspan=12)

    titulo = tk.Label(root, text=asignarTEXTOS("Asegurate de ingresar correctamente la clave de la criptomoneda que deseas buscar",LENGUAJE.IDIOMA_ACTUAL), font=TITULO_FUENTE, bg=COLOR_BG, fg=COLOR_TITULOS)
    titulo.grid(column=1, row=5)

    textoBTN = tk.StringVar()
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:regresar(root), fg=COLOR_BG, font=TEXTO_FUENTE, bg=COLOR_BOTONES, width=10)
    textoBTN.set(asignarTEXTOS("Regresar",LENGUAJE.IDIOMA_ACTUAL))
    btn_Iniciar.grid(column=1, row=7)
    root.mainloop()