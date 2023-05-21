class Auto():

    def __init__(self, name, age, producer, volume, color):
        self.name = name
        self.age = age
        self.producer = producer
        self.volume = volume
        self.color = color

    def show(self):
        print(f"Car: {self.name}, {self.age}, {self.producer}, {self.volume}, {self.color}")

d = Auto("volkswagen", 2016, "Germany", 1.8, "gray")

d.show()







