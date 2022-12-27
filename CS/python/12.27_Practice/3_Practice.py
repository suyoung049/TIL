cabinet = {3:"유재석", 4:"조세호"}
print(cabinet[3])

print(cabinet.get(3))
print(cabinet.get(5,"하하"))

cabinet["A-3"] = '김종국'
cabinet["c-20"] = "조세호"

del cabinet[4]

print(cabinet.keys())
print(cabinet.items())
print(cabinet.values())

menue = ("돈까스", "치즈까스")
print(menue[1])


