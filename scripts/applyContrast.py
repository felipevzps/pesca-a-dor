import pyautogui
from PIL import Image, ImageEnhance

image_path = 'fish_1024x768.PNG'
image = Image.open(image_path)

# aumentar o contraste em 50%
#enhancer = ImageEnhance.Contrast(image)
#image = enhancer.enhance(1.5)

# converter a imagem para escala de cinza
image = image.convert('L')

# binarizar a imagem usando o método de limiar global
threshold=127
image = image.point(lambda x: 0 if x < threshold else 255, '1')


# salvar a imagem com contraste aumentado
new_image_path = 'fish_1024x768_binarizada.PNG'
image.save(new_image_path)