def min_needed(max_weigth, num_fishers, weights):

    weights.sort()

    left = 0
    right = num_fishers - 1
    boats_count = 0

    while left <= right:
        if weights[left] + weights[right] <= max_weigth:
            left += 1
        right -= 1
        boats_count += 1

    return boats_count

if __name__ == "__main__":
    m = int(input("Введите максимальный вес лодки: "))
    n = int(input("Введите количество рыбаков: "))
    weights = []

    for _ in range(n):
        weight = int(input("Введите вес рыбака: "))
        weights.append(weight)

    result = min_needed(m, n, weights)
    print(result)