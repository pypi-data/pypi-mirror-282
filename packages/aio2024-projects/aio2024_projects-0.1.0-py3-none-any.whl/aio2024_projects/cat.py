class Cat:
    def __init__(self, name):
        self.__name = name
    def describe(self):
        return f"Name of cat is {self.__name}"

cat = Cat("Han")
print(cat)
