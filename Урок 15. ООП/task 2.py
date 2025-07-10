class Transport:
    def __init__(self, name, max_passengers):
        self.name = name
        self.max_passengers = max_passengers
        
    
autobus = Transport('Renaul Logan', 50)

print(f"Вместимость одного автобуса {autobus.name}  {autobus.max_passengers} пассажиров")