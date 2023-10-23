class Human:
    def __init__(self, name = "Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passangers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passangers.append(passenger)

    def print_passengers_name(self):
        if self.passangers != []:
            print(f"Імена пасажирів в авто:{self.brand}")
            for passangers in self.passangers:
                print(passangers.name)
        else:
            print(f"В авто {self.brand} пасажири відсутні")

    def print_drive_name(self):
        if self.drive != []:
            print(f"Ім'я водія в авто:{self.brand}")
            for drive in self.drive:
                print(drive.name)
        else:
            print(f"В авто {self.brand} водій відсутній")

car = Auto("BMW M5 F90")

for i in range(4):
    p1 = Human(input("Введіть ім'я пасажира: "))
    car.add_passenger(p1)

p2 = Human(input("Введіть ім'я водія: "))
car.add_passenger(p2)

car.print_passengers_name()