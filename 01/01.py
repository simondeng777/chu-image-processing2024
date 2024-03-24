import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\path\Tesseract-OCR\tesseract.exe"
img = Image.open("english.jpg")
#img.show()
print(pytesseract.image_to_string(img, lang="eng"))

