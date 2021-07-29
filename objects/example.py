class Person:
    def __init__(self, name: str, age: int, yummy_food: str):
        self.name = name
        self.age = age
        self.yummy_food = yummy_food

    def introduce(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} years old.")

    def food(self):
        print(f"I like to eat {self.yummy_food}.")


def main():
    john = Person("John", 15, "Cheese Pizza")
    john.introduce()
    john.food()


if __name__ == '__main__':
    main()
