import tkinter as tk
from tkinter.font import Font
from assets.modulos.parametros import COLOR_BG, COLOR_SECUNDARIO, COLOR_BOTONES, COLOR_TITULOS, LOGO, LENGUAJE
from tkinter.constants import CENTER
from assets.modulos.idioma import asignarTEXTOS
from assets.modulos.obtenerPreciosCriptomonedas import getTop

def regresar(root):
    root.destroy()
    from assets.modulos.main_interfaz import interfaz
    interfaz("Fresh Prices")

def irCriptomoneda(root,clave):
    root.destroy()
    from assets.modulos.infoCriptomoneda import infoCriptomoneda
    try:
        infoCriptomoneda(clave)
    except UnboundLocalError:
        from assets.modulos.error import error
        error()
        

def criptomonedas():
    root = tk.Tk()
    root.title("Criptomonedas")
    root.iconbitmap(LOGO+".ico")
    root.resizable(False,False)
    TITULO_FUENTE = Font(family="Roboto", size=20)
    TEXTO_FUENTE = Font(family="Roboto", size=15)
    TEXTO_TOP = Font(family="Roboto", size=12)   
    
    header = tk.Canvas(root, width=450, height=60, bg=COLOR_SECUNDARIO)
    header.grid(column=1,row=1)

    titulo = tk.Label(root, text=asignarTEXTOS("Criptomonedas",LENGUAJE.IDIOMA_ACTUAL), font=TITULO_FUENTE, bg=COLOR_SECUNDARIO, fg=COLOR_TITULOS)
    titulo.grid(column=1, row=1) 

    canvas = tk.Canvas(root, width=450, height=600, bg=COLOR_BG)
    canvas.grid(columnspan=3, rowspan=12)

    titulo = tk.Label(root, text="Top 5", font=TITULO_FUENTE, bg=COLOR_BG, fg=COLOR_TITULOS)
    titulo.grid(column=1, row=2)
    
    CRIPTOS = {cripto:getTop(cripto) for cripto in range(5)}
    CLAVES = ['','','','','']
    for cripto in range(5):
        CLAVES[cripto] = CRIPTOS[cripto]
    # 1
    textoBTN = tk.StringVar()
    textoBTN.set(CLAVES[0])
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:irCriptomoneda(root,CLAVES[0]), fg=COLOR_TITULOS, font=TEXTO_TOP, bg=COLOR_BG, width=12)
    btn_Iniciar.grid(column=1, row=3)
    # 2
    textoBTN = tk.StringVar()
    textoBTN.set(CLAVES[1])
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:irCriptomoneda(root,CLAVES[1]), fg=COLOR_TITULOS, font=TEXTO_TOP, bg=COLOR_BG, width=12)
    btn_Iniciar.grid(column=1, row=4)
    # 3
    textoBTN = tk.StringVar()
    textoBTN.set(CLAVES[2])
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:irCriptomoneda(root,CLAVES[2]), fg=COLOR_TITULOS, font=TEXTO_TOP, bg=COLOR_BG, width=12)
    btn_Iniciar.grid(column=1, row=5)
    # 4
    textoBTN = tk.StringVar()
    textoBTN.set(CLAVES[3])
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:irCriptomoneda(root,CLAVES[3]), fg=COLOR_TITULOS, font=TEXTO_TOP, bg=COLOR_BG, width=12)
    btn_Iniciar.grid(column=1, row=6)
    # 5
    textoBTN = tk.StringVar()
    textoBTN.set(CLAVES[4])
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:irCriptomoneda(root,CLAVES[4]), fg=COLOR_TITULOS, font=TEXTO_TOP, bg=COLOR_BG, width=12)
    btn_Iniciar.grid(column=1, row=7)
    
    titulo = tk.Label(root, text=asignarTEXTOS("Ingresa la clave o el nombre de la criptomoneda",LENGUAJE.IDIOMA_ACTUAL), font=TEXTO_TOP, bg=COLOR_BG, fg=COLOR_TITULOS)
    titulo.grid(column=1, row=8)

    cripto = tk.Entry(root, fg=COLOR_TITULOS, font=TEXTO_TOP, bg=COLOR_SECUNDARIO, width=12, justify=CENTER)
    cripto.grid(row=9,column=1)

    textoBTN = tk.StringVar()
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:irCriptomoneda(root,cripto.get()), fg=COLOR_BG, font=TEXTO_TOP, bg=COLOR_BOTONES, width=8)
    textoBTN.set(asignarTEXTOS("Buscar",LENGUAJE.IDIOMA_ACTUAL))
    btn_Iniciar.grid(column=1, row=10)

    textoBTN = tk.StringVar()
    btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:regresar(root), fg=COLOR_BG, font=TEXTO_TOP, bg=COLOR_BOTONES, width=10)
    textoBTN.set(asignarTEXTOS("Regresar",LENGUAJE.IDIOMA_ACTUAL))
    btn_Iniciar.grid(column=1, row=12)
    root.mainloop()