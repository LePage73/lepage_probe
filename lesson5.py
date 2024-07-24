print("create var type tuple")
immutable_var = ("year of birth", 1969, True)
print(immutable_var)
print(immutable_var[0])
print(immutable_var[1])
print(immutable_var[2])

print("Аttempt to change var type tuple")
# immutable_var[1] = 2001 # Здесь выдает ошибку - объект типа кортеж не поддерживает изменение
print("The attempt failed")
print(immutable_var)

print("create var type list")
mutable_list =["year of birth", 1969, True]

print(mutable_list)
print(mutable_list[0])
print(mutable_list[1])
print(mutable_list[2])

print("Аttempt to change var type list")

mutable_list[1] = 2001
print(mutable_list)
print(mutable_list[0])
print(mutable_list[1])
print(mutable_list[2])

