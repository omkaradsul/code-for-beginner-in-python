class mammal:
    def walk(self):
        print("walk")


class dog(mammal):
    def bark(self):
        print("dogs bark")


class cat(mammal):
    def meow(self):
        print("cats meow")

dog1 = dog()
dog1.walk()
dog1.bark()

cat1 = cat()
cat1.walk()
cat1.meow()