"""
avengers = "WE ARE IN THE ENDGAME NOW"
print(avengers.isupper())

eddie = "we are Venom"
print(eddie.islower())

tony = "i am ironman"
print(tony.upper())

avengers = "WE ARE IN THE ENDGAME NOW"
print(avengers.lower())


list_of_meal = ["vegetables", "chiken", "cola"]
print(list_of_meal)
list_of_meal.pop()
print(list_of_meal)
list_of_meal.append("water")
print(list_of_meal)
print('#' * 30)
for i in range(len(list_of_meal)):
    print(list_of_meal[i])
print('#' * 30)
for item in list_of_meal:
    print(item)
print('#' * 30)

marks = [3, 4, 2, 5, 5, 5, 3, 4, 2, 5, 3]
print("1)", marks[0])
print("2)", marks[1])
print("3)", min(marks))
print("4)", max(marks))
print("5)", sum(marks))

ha1 = input(int("введите оценки:"))
ha2 = input(int("введите оценки:"))
ha3 = input(int("введите оценки:"))
ha4 = input(int("введите оценкb:"))
ha5 = input(int("введите оценки:"))
ha6 = input(int("введите оценки:"))
ha7 = input(int("введите оценки:"))
ha8 = input(int("введите оценки:"))
ha9 = input(int("введите оценки:"))
ha10 = input(int("введите оценки:"))

summa = ha1 + ha2 + ha3 + ha4 + ha5 + ha6 + ha7 + ha8 + ha9 + ha10
print(summa)
"""

marks = input("введите оценки:")
marks = marks.split()
for i in range(len(marks)):
    marks[i] = int(marks[i])

print(sum(marks) / len(marks))
