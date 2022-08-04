import tkinter as tk
from tkinter.font import Font
from assets.modulos.parametros import COLOR_BG, COLOR_SECUNDARIO, COLOR_BOTONES, COLOR_TITULOS, LOGO, LENGUAJE
from tkinter.constants import CENTER
from assets.modulos.idioma import asignarTEXTOS
from assets.modulos.obtenerPreciosCriptomonedas import iniciarDiccionario

def regresar(root):
    root.destroy()
    from assets.modulos.criptomonedas import criptomonedas
    criptomonedas()

def infoCriptomoneda(clave):
    CRIPTO = {cripto:iniciarDiccionario(clave) for cripto in range(1)}
    print(CRIPTO)
    if CRIPTO[0]['price'] == 0:
        print("---")
    else:    
        root = tk.Tk()
        root.title(CRIPTO[0]['symbol'])
        root.iconbitmap(LOGO+".ico")
        root.resizable(False,False)
        TITULO_FUENTE = Font(family="Roboto", size=20)
        TEXTO_TOP = Font(family="Roboto", size=12)   
        
        header = tk.Canvas(root, width=450, height=60, bg=COLOR_SECUNDARIO)
        header.grid(column=1,row=1)

        titulo = tk.Label(root, text=CRIPTO[0]['nombre'], font=TITULO_FUENTE, bg=COLOR_SECUNDARIO, fg=COLOR_TITULOS)
        titulo.grid(column=1, row=1) 

        canvas = tk.Canvas(root, width=450, height=200, bg=COLOR_BG)
        canvas.grid(columnspan=3, rowspan=12)

        titulo = tk.Label(root, text="$"+ str(CRIPTO[0]['price']) + " USD", font=TEXTO_TOP, bg=COLOR_BG, fg=COLOR_BOTONES)
        titulo.grid(column=1, row=4)

        titulo = tk.Label(root, text="$"+ str(CRIPTO[0]['price'] * 20) + " MXN", font=TEXTO_TOP, bg=COLOR_BG, fg=COLOR_TITULOS)
        titulo.grid(column=1, row=5)

        titulo = tk.Label(root, text="Circulating Supply: "+ str(CRIPTO[0]['circSupply']) + " " + CRIPTO[0]['symbol'], font=TEXTO_TOP, bg=COLOR_BG, fg=COLOR_BOTONES)
        titulo.grid(column=1, row=6)

        titulo = tk.Label(root, text="Market Cap: $"+ str(CRIPTO[0]['marketCap']) + " USD", font=TEXTO_TOP, bg=COLOR_BG, fg=COLOR_TITULOS)
        titulo.grid(column=1, row=7)
        
        textoBTN = tk.StringVar()
        btn_Iniciar = tk.Button(root, textvariable=textoBTN, command=lambda:regresar(root), fg=COLOR_BG, font=TEXTO_TOP, bg=COLOR_BOTONES, width=10)
        textoBTN.set(asignarTEXTOS("Regresar",LENGUAJE.IDIOMA_ACTUAL))
        btn_Iniciar.grid(column=1, row=9)
        root.mainloop()