from PIL import Image, ImageDraw, ImageFont
holidays = {"Новый год": "newyear.jpg", "День рождения": "hapbirt.jpg", "8 Марта": "march8.jpg"}
print("Доступные праздники:")
for a in holidays:
    print(f" - {a}")
holiday = input("К какому празднику нужна октрытка? ")
if holiday not in holidays:
    print("Такого праздника нет!")
    exit()
name = input("Введите имя того, кого хотите поздравить: ")
img = Image.open(holidays[holiday])
draw = ImageDraw.Draw(img)
text = f"{name}, поздравляю!"
font = ImageFont.load_default()
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
x = (img.width - text.width) // 2
y = 30
draw.text((x, y), text, font=font, fill=(255, 0, 0))
output_name = f"otkrytka_{holiday}_{name}.png"
img.save(output_name)
print(f"Готово! Открытка сохранена как {output_name}")
img.show()
