"""
class Human:
    def __init__(self, age, name, height):
        self.age = age
        self.name = name
        self.height = height
        print("Привет меня зовут", name)

    def say_hello_to(self, name_to):
        print('Привет,', name_to)

    def tell_about_yourself(self):
        print('Привет,меня зовут', self.name)
        print('Мне', self.age, 'лет')

    def happy_birthday(self):
        print('Сегодня у меня день рождения!')
        self.age += 1

print('Саша')
Alex = Human(10, 'Саша', 130)
print(Alex.age)
Alex.happy_birthday()

print("Андрей")
Andrew = Human(15, 'Андрей', 170)
Andrew.say_hello_to('Саша')


class Car:
    def sound(self):
        print("beep")
    def long_sound(self):
        print("beep-beep")
car = Car()
car.sound()
car.long_sound()
"""
s = 1
class Button:
    def __init__(self, click, click_count, reset):
        self.count = 0
    def click(self):
        self.count += 1
    def click_count(self):
        self.count -= 1
count = Button()
count.click_count()
count.click()
print()