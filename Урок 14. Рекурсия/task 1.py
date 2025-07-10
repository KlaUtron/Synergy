def print_elements(lst, index):
    if index >= len(lst):
        print("Конец списка")
        return
    
    print(lst[index])
    
    print_elements(lst, index + 1)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print_elements(my_list, 0)