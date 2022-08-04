# Parametros utilizados para crear el frame
COLOR_BG = "#272727"
COLOR_PRINCIPAL = "#C4C4C4"
COLOR_TITULOS = "#46FF05"
COLOR_BOTONES = "#C4C4C4"
COLOR_SECUNDARIO = "#494949"
LOGO = './assets/imgs/icono/logo'
IDIOMA_ACTUAL = 'en'
class Idioma:
    def __init__(self, actual):
        self.IDIOMA_ACTUAL = actual
    def cambiarEspanol(self):
        self.IDIOMA_ACTUAL = 'es'
    def cambiarIngles(self):
        self.IDIOMA_ACTUAL = 'en'
LENGUAJE = Idioma('en')