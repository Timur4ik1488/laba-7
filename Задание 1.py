try:
    from random import randint

    m=int(input("Введите количество строк: "))
    n=int(input("Введите значение элементов в строках: "))
    auto_list = [[randint(0,20) for _ in range(n)] for _ in range(m)]
    print("Исходный список: ", *auto_list, sep="\n")

    p=[]
    for i in range(len(auto_list)):
        if i%2!=0:
            auto_list[i] = (auto_list[i]) [::-1] 
    print("Выходной список: ", *auto_list, sep = "\n")

except:
    print("Неверно введены значения для количества строк и элементов")



