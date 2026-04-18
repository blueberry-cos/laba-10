from PIL import Image
img = Image.open("picter.jpg")
cropped = img.crop((100, 50, 400, 300))
cropped.save("cropped_picter.jpg")
print("Готово как cropped_picter.jpg")