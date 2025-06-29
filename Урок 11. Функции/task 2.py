pets = {}

# Возраст питомца
def format_age(age):
    if age % 10 == 1 and age % 100 != 11:
        return f'{age} год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 > 20):
        return f'{age} года'
    else:
        return f'{age} лет'
    
# Информация о питомце
def add_pet(pets):
    name = input('Введите кличку питомца ')
    pet_type = input('Введите вид питомца ')
    try:
        age = int(input('Введите возраст питомца '))
    except ValueError:
        print('Ошибка: Введите число!')
        return
    owner = input('Введите имя владельца ')

    pets[name] = {
        'Вид питомца': pet_type,
        'Возраст питомца': age,
        'Имя владельца': owner
    }

    print(f"\nПитомец '{name}' успешно добавлен")

# Выводит информацию о питомце
def list_pets(pets):
    if not pets:
        print('\nНет записей о питомцах.\n')
        return
    
    print("\nСписок питомцев:")
    for name, info in pets.items():
        print(f"Кличка: {name}")
        print(f"Вид: {info['Вид питомца']}")
        print(f"Возраст: {format_age(info['Возраст питомца'])}")
        print(f"Имя владельца: {info['Имя владельца']}")
        print("-" * 30)

def main():

    while True:
        print('====Блокнот питомцев===')
        print('1. Добавить питомца')
        print('2. Список питомцев')
        print('3. Выход')
        choice = input('Выберите действие (1 - 3): ')

        if choice == '1':
            add_pet(pets)
        elif choice == '2':
            list_pets(pets)
        elif choice == '3':
            print('Выход')
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()