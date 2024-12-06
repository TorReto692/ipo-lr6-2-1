import random #Модуль random для генерации случайных чисел

h = int(input("Введите высоту матрицы: ")) #Запрос высоты от пользвоателя
w = int(input("Введите ширину матрицы: ")) #Запрос ширины от пользвоателя

if h > 8 or h < 4: #Условие
    print("Матрица не подходит по размеру") #Проверка высоты матрицы
    quit() #Выход

if w > 8 or w < 4: #Условие
    print("Матрица не подходит по размеру") #Проверка ширины матрицы
    quit() #Выход

n = [-3, -5, -2, -12, 0, 15, 4, 7, 2] #Список возможных значений матрицы
mtr = [[random.choice(n) for i in range(w)] for j in range(h)] #Создание матрицы двумерным списком

sum = 0 #Значение переменной 

print() #Переход на новую строку

for i in mtr:  #Вывод матрицы
    for j in i:
        print(j,end=" ")   #Вывод каждого элемента в строке без перехода на новую строку
    print()  # переход на новую строку

for i in mtr: #Цикл для подсчета суммы четных элементов матрицы
    for j in i: #Перебор элементов
        if j%2 ==0: #Проверка, является ли элемент четным
            sum+=j #Счетчик

print("Сумма всех четных элементов равна :", sum) #Вывод на экран