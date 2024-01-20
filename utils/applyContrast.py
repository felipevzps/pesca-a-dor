from PIL import Image, ImageEnhance

image_path = 'images/1024x768/fish.PNG'
image = Image.open(image_path)

# Increase contrast (+50%)
#enhancer = ImageEnhance.Contrast(image)
#image = enhancer.enhance(1.5)

#convert image to grayscale
image = image.convert('L')

#binarize image using the global thresholding method
threshold=127
image = image.point(lambda x: 0 if x < threshold else 255, '1')

#save image with increased contrast
new_image_path = 'images/1024x768/fish_bin.PNG'
image.save(new_image_path)