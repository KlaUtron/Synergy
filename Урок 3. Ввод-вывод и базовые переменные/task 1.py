name_pet = input("Как зовут вашего питемца? ")
Porode = input("Какая порода у вашего животного? ")
age = int(input("Сколько лет вашему питомцу? "))

if age == 1: 
    print(f"Это {Porode} по кличке \"{name_pet}\". Возраст: {age} год.")
elif age <= 4:
    print(f"Это {Porode} по кличке \"{name_pet}\". Возраст: {age} года.")
else:
    print(f"Это {Porode} по кличке \"{name_pet}\". Возраст: {age} лет.")