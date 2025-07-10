class CaskRegister():
    def __init__(self):
        self.balance = 0

    def top_up(self, X):
        if X < 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += X

    def count_1000(self):
        return self.balance // 1000
    
    def take_away(self, X):
        if X < 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if self.balance < X:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= X

caskRegister = CaskRegister()

caskRegister.top_up(5000)
print(f"Текущий баланс: {caskRegister.balance}")

caskRegister.take_away(2000)
print(f"Текущий баланс после снятия: {caskRegister.balance}") 
try:
    caskRegister.take_away(4000)
except ValueError as e:
    print(e)
