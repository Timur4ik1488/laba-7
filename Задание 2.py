from random import randint

n = int(input("Введите количество строк и столбцов: "))
auto_list = [[[randint(0,20) for _ in range(n)] for _ in range(n)]]
auto_list1 = [[[randint(0,20) for _ in range(n)] for _ in range(n)]]
print("Первый список: ", *auto_list, sep = "\n")
print("Второй список: ", *auto_list1, sep = "\n")

l = len(auto_list)
z = []
for i in range(l): # цикл проходит по строкам
    z = [*z, [] ]
    for j in range(len(auto_list[i])): # цикл проходит по элементам в строке
        z [i] = [*z[i], auto_list [i][j]]
        z [i] = [*z[i], auto_list1 [i][j]]
print("Список после преобразований: ", *z, sep = "\n")




