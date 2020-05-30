#pillow Python imaging library
import pytesseract 
from PIL import Image, ImageFilter,ImageEnhance
import os

def process_image(image):
    image = image.convert('RGB')
    image = image.filter(ImageFilter.SHARPEN)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    return pytesseract.image_to_string(image)


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "images/chotabheem.png"
abs_file_path = os.path.join(script_dir, rel_path)

img=Image.open(abs_file_path)

#img=process_image(img)
sharpener = ImageEnhance.Brightness (img.convert('RGB'))
#img=img.convert('RGB')

img=img.convert('L')

filtered_img=img.filter(ImageFilter.DETAIL)
print(filtered_img)
filtered_img.save("DETAIL.png",'png') #png support imagefilter


''' ImageFilter

    BLUR
    CONTOUR
    DETAIL
    EDGE_ENHANCE
    EDGE_ENHANCE_MORE
    EMBOSS
    FIND_EDGES
    SHARPEN
    SMOOTH
    SMOOTH_MORE

'''

box=(50,50,279,270)
region=filtered_img.crop(box)
region.save("cropimg.png",'png')
#region.show()

print(filtered_img.size)
#filtered_img.show()
resize=filtered_img.resize((100,100))
resize.save("resize.png",'png') #png support imagefilter
rotate=filtered_img.rotate(90) #rotate 90,180 degree
rotate.save("rotate.png",'png') #png support imagefilter

rel_path = "images/train.jpg"
abs_file_path = os.path.join(script_dir, rel_path)

img1=Image.open(abs_file_path)
new_img=img1.resize((400,400))
new_img.save('thumbnail.jpg')#aspect ratio will be changed
#new_img.show()

img1.thumbnail((400,400))
img1.save('thumbnail.jpg')
print(img1.size)