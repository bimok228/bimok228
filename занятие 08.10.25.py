"""
pomidori = True
ogurci = True
smetana = True
luk = True

if pomidori == True or ogurci == True or smetana == True or luk == True:
    print("сегодня будем есть салат ")
else:
    print("салата не будет ")

kurica = True
suhari = True
salat = True
sir = True
sous = True

if kurica and suhari and salat and sous and sir:
    print("цезарь можно приготовить")
else:
    print("Цезарь не получится приготовить")
"""

v = input("введите своё число/цифру:")
o = input("введите своё число/цифру:")
p = input("введите своё число/цифру:")

if v == "красный" and o == "жёлтый" and p == "зелёный" or \
 v == "3" and o == "2" and p == "1":
    print("поехали")
else:
    print("стой")