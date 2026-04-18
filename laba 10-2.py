from PIL import Image
holidays = {"Новый год": "newyear.jpg", "День рождения": "hapbirt.jpg", "8 Марта": "march8.jpg"}
print("Доступные праздники:")
for a in holidays:
    print(f" - {a}")
B = input("К какому празднику нужна октрытка? ")
if B in holidays:
    img = Image.open(holidays[B])
    img.show()
    print(f"Открытка к {B} открыта")
else:
    print("Такого праздника в списаке нет!")

