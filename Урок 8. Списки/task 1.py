N = int(input())

res = []

for _ in range(N):
    a = int(input())
    res.append(a)

reversed_res = res[::-1]

for num in reversed_res:
    print(num)

