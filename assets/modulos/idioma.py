import tkinter as tk
from tkinter.font import Font
from assets.modulos.parametros import COLOR_BG, COLOR_SECUNDARIO, COLOR_BOTONES, COLOR_TITULOS, LOGO, LENGUAJE

def regresar(root):
    root.destroy()
    from assets.modulos.main_interfaz import interfaz
    interfaz("Fresh Prices")

def idiomaEspanol(root):
    LENGUAJE.IDIOMA_ACTUAL = 'es'
    root.destroy()
    from assets.modulos.main_interfaz import interfaz
    interfaz("Fresh Prices")

def idiomaIngles(root):
    LENGUAJE.IDIOMA_ACTUAL = 'en'
    root.destroy()
    from assets.modulos.main_interfaz import interfaz
    interfaz("Fresh Prices")

def seleccionIdioma():
    root = tk.Tk()
    root.title("Selección de Idioma")
    root.iconbitmap(LOGO+".ico")
    root.resizable(False,False)
    TITULO_FUENTE = Font(family="Roboto", size=20)
    TEXTO_FUENTE = Font(family="Roboto", size=15)   
    
    header = tk.Canvas(root, width=450, height=60, bg=COLOR_SECUNDARIO)
    header.grid(column=1,row=1)

    titulo = tk.Label(root, text=asignarTEXTOS("Selecciona el Idioma",LENGUAJE.IDIOMA_ACTUAL), font=TITULO_FUENTE, bg=COLOR_SECUNDARIO, fg=COLOR_TITULOS)
    titulo.grid(column=1, row=1) 

    canvas = tk.Canvas(root, width=450, height=260, bg=COLOR_BG)
    canvas.grid(columnspan=3, rowspan=12)

    textoBTN = tk.StringVar()
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:idiomaIngles(root),fg=COLOR_BG, font=TEXTO_FUENTE, bg=COLOR_BOTONES, width=10)
    textoBTN.set(asignarTEXTOS("Ingles",LENGUAJE.IDIOMA_ACTUAL))
    btn_Iniciar.grid(column=1, row=5)
    
    textoBTN = tk.StringVar()
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:idiomaEspanol(root),fg=COLOR_BG, font=TEXTO_FUENTE, bg=COLOR_BOTONES, width=10)
    textoBTN.set(asignarTEXTOS("Español",LENGUAJE.IDIOMA_ACTUAL))
    btn_Iniciar.grid(column=1, row=7)

    textoBTN = tk.StringVar()
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:regresar(root), fg=COLOR_BG, font=TEXTO_FUENTE, bg=COLOR_BOTONES, width=10)
    textoBTN.set(asignarTEXTOS("Regresar",LENGUAJE.IDIOMA_ACTUAL))
    btn_Iniciar.grid(column=1, row=9)
    root.mainloop()

# Traducción de Textos
def asignarTEXTOS(TEXTO, LENGUAJE):
    import os
    from google.cloud import translate_v2 as translate
    ARCHIVO_JSON = "./freshprices-109347d836e6.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ARCHIVO_JSON
    traductor = translate.Client()
    TRADUCIENDO = traductor.translate(TEXTO,LENGUAJE)
    return TRADUCIENDO["translatedText"]