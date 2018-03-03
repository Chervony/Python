time = int(input("Введите время "))
if time >= 6 and time <= 11:
    print("Утро")
elif time == 12:
    print("Полдень")
elif time >= 13 and time <=18:
    print("Обед")
elif time >= 19 and time <= 22:
    print("Вечер")
elif time == 24:
    print("Полночь")
elif time >=1 and time <= 5:
    print("Ночь")
elif time <=0 or time >= 25:
    print ("такого времени не существует")
print(goodbye.)
