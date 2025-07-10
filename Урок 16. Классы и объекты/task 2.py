import math

class Черепашка:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 0:
            raise ValueError
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        moves_x = math.ceil(dx / self.s)
        moves_y = math.ceil(dy / self.s)
        return moves_x + moves_y


черепашка = Черепашка(x=0, y=0, s=2)

черепашка.go_right()
print(f"Текущая позиция: ({черепашка.x}, {черепашка.y})") 


черепашка.evolve()
print(f"Новый шаг: {черепашка.s}") 

черепашка.degrade()
print(f"Новый шаг после деградации: {черепашка.s}") 

минимальные_действия = черепашка.count_moves(10, 10)
print(f"Минимальное количество действий до (10, 10): {минимальные_действия}")