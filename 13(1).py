class House:
    def __init__(self, number, owner, area, price):
        self.number = number  
        self.owner = owner    
        self.area = area      
        self.price = price    
        print(f"Будинок {self.number} створено. Власник: {self.owner}, Площа: {self.area}, Ціна: {self.price}")

    def __del__(self):
        print(f"Будинок {self.number} знищено.")

    def change_owner(self, new_owner):
        self.owner = new_owner
        print(f"Власник будинку {self.number} змінюється з {self.owner} на {new_owner}.")

    def change_price(self, new_price):
        self.price = new_price
        print(f"Ціна будинку {self.number} змінюється з {self.price} на {new_price}.")

    def __str__(self):
        return f"Будинок {self.number}: Власник - {self.owner}, Площа - {self.area}, Ціна - {self.price}"


street = []

street.append(House(1, "Іван", 100, 50000))
street.append(House(2, "Марія", 120, 60000))
street.append(House(3, "Петро", 80, 40000))

for house in street:
    print(house)

street[0].change_owner("Олександр")
street[0].change_price(55000)

print(street[0])

del street[2]
del street[1]
del street[0]
