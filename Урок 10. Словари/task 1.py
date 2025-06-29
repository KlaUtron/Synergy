
pets = {}


pet_name = input('Введите имя питомца: ')
pet_type = input('Введите вид питомца: ')
try:
    pet_age = int(input('Введите возраст питомца: '))
except ValueError:
    print("Ошибка: Возраст должен быть целым числом.")
    exit()
name = input('Введите имя владельца: ')


pet_info = {
    "вид питомца": pet_type,
    "возраст питомца": pet_age,
    "имя владельца": name
}


pets[pet_name] = pet_info


def format_age(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"

print("\nИнформация о питомце:")
for key, value in pets[pet_name].items():
    if key == "возраст питомца":
        print(f"{key}: {value} {format_age(value)}")
    else:
        print(f"{key}: {value}")