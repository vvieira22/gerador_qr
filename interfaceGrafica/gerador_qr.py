#requeriespyqrcode and pypng (to convert to png) to run qr.
import os
from PIL import Image
import pyqrcode

class QR():
    def __init__(self):
            scriptpath = os.path.abspath(__file__)
            scriptdir = os.path.dirname(scriptpath)
            self._imagepath = os.path.join(scriptdir, "imagens/")

    def gerar_qr_temporario(self, conteudo):
        try:
            imagem_qr = pyqrcode.create(conteudo, error='L')
            with open(self._imagepath + 'qr_temp.png', 'wb') as f:
                imagem_qr.png(f, scale=15, quiet_zone=2)
        except:
            raise "Error ao gerar qr."
        self.adicionar_logo()

    def adicionar_logo(self):
        # Now open that png image to put the logo
        img = Image.open(self._imagepath + 'qr_temp.png')
        img = img.convert("RGBA")
        width, height = img.size
        
        # How big the logo we want to put in the qr code png
        logo_size = 70

        # Open the logo image
        logo = Image.open(self._imagepath + 'vvieira.jpg')

        # Calculate xmin, ymin, xmax, ymax to put the logo
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))

        # resize the logo as calculated
        logo = logo.resize((xmax - xmin, ymax - ymin))

        # put the logo in the qr code
        img.paste(logo, (xmin, ymin, xmax, ymax))

        img.save(self._imagepath + 'qr_temp.png')
    
    def retornar_qr_temp(self):
        return Image.open(self._imagepath + "qr_temp.png")

    def excluir_qr_temporario(self):
        os.remove(self._imagepath + 'qr_temp.png')

