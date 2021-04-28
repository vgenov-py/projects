class Human: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def envejecer(self):
        self.age += 1



a = Human("pepe", 10)
a.envejecer()
print(a.age)