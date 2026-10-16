magic_box = ("apple", "banana", "cherry")
backpack = ["apple", "banana", "cherry"]
print("Волшебная коробка(кортеж):", magic_box, "Рюкзак(список):", backpack)
backpack[0] = "kiwi"
print("Рюкзак после замены:", backpack)
#magic_box[0] = "kiwi"
#Нельзя изменять кортеж
backpack.append("orange")
print("Рюкзак после добавления:", backpack)
#magic_box.append("orange")
#Кортеж нельзя изменять
backpack[0] = "apple"
print("Рюкзак после замены:", backpack)
#magic_box[0] = "apple"
#Кортеж не поддерживает замену элементов
fruit = magic_box[1]
print("Смотрим элемент под номером 1:", fruit)
total = len(magic_box)
print("Сколько фруктов в коробке?", total)
has_banana = ("banana" in magic_box)
print("Есть ли банан в коробке?", has_banana)
#Перебираем фрукты в коробке:
for item in magic_box:
    print("Перебираем фрукты в коробке:", item)
animals = ("cat", "dog", "mouse","rabbit")
print("В волшебной коробке животные:",animals)
score = 0
for round_num in range(2):
    answer = input(f"\n Раунд {round_num + 1}: Какое животное под номером {round_num + 1}?")
    if answer == animals[round_num]:
        score += 1
    else:
        print("Неправильно! Там было", {animals[round_num]})
print(f"\n Твой счёт: {score} из 2")