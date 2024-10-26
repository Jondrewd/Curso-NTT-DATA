# imagemagic/imagemagic.py
from PIL import Image, ImageFilter

def aplicar_filtro(imagem_path, filtro):
    imagem = Image.open(imagem_path)
    
    if filtro == 'desfocar':
        imagem = imagem.filter(ImageFilter.BLUR)
    elif filtro == 'contorno':
        imagem = imagem.filter(ImageFilter.CONTOUR)
    
    imagem.save(f'output_{filtro}.png')
    print(f'Imagem salva como output_{filtro}.png')

