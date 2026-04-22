#1
name = "Данил"

#2
a = 3
if name == "Данил":#если
    print("ывфвфвфв")
elif name == "не данил":#иначе если
    print("ывфвфы")
elif name == "не не иван" and a == 5 or a == 6: #3
    print(a)
else:# иначе
    print("ыавфвыффвф")

#4
stroka = "авааыфвфывфыв"
print(stroka[0])
print(len(stroka))
#5
i = 0
while i < 10:
    print(i)
    i += 1
#6
for i in range(0, 10, 1):
    print(i)
#7
spisok = [] #создание списка
spisok.append("привет")# добавление в список
spisok.pop()#удаление из списка
print(len(spisok))
#8
def  ask_password():#объявление функции
    password = input("введите пароль")
    if password == "123":
        print("слишком лёгкий пароль")
ask_password()#вызов функции
