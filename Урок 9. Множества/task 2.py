list1 = []
while True:
    line = input().strip()
    if line == "":
        break
    try:
        num = int(line)
        list1.append(num)
    except ValueError:
        print(f"Ошибка: '{line}' не является целым числом.")
        exit()

list2 = []
while True:
    line = input().strip()
    if line == '':
        break
    try:
        num = int(line)
        list2.append(num)
    except ValueError:
        print(f"Ошибка: '{line}' не является целым числом.")
        exit()

set1 = set(list1)
set2 = set(list2)

res_num = set1 & set2

print("\nРезультат:")
print(len(res_num))