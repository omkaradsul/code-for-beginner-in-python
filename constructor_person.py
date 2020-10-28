name = input("what is your name?  ")
bot = input("who did you like as your assistant? ")


class Person:
    def __init__(self, name, bot):
        Person.name = name
        Person.bot = bot

    def talk(self):
        print(f"Hi I am {self.name}")
        print(f"hello I am {self.bot}")
        print(f"how can i help you")


person1 = Person(name, bot)
person1.talk()
