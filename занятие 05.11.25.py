"""
name = "inginirium"
print(name[0:4:1])
print(name[4:0:-1])
print(name[:])
print(name[::-1])


print(chr(125))
print(ord("п"))
print(chr(ord("a") + 3))

for i in range(26):
    print(chr(ord("a") + i ), chr(ord("A") + i),sep=" ")
"""
afd = input("введите ваше слово:")
for i in range(1, len(afd), 1):
    print(ord(afd[i]),end=", ")
