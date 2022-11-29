class Animal():

    def __init__(self, nama):
        self.nama = nama

    def info(self):
        print(f"I'm an animal. My name is {self.nama}.")

    def sound():
        pass


class Cat(Animal):

    def __init__(self, nama):
        super().__init__(nama)

    def info(self):
        print("I'm a cat. My name is {self.nama}.")

    def sound(self):
        print("Meow")


class Dog(Animal):

    def __init__(self, nama):
        super().__init__(nama)
        print(Animal)

    def info(self):
        print("I'm a dog. My name is {self.nama}.")

    def sound(self):
        print("Woof")


A = Cat("Win")
B = Dog("Wan")

A.sound()
B.sound()
