import os
import math
import string
from random import Random, randint

# ==========================================================================================================
# FUNCTIONS
# ==========================================================================================================


def NewElementNego(func, x, i):
    return func(x, i)
# = = = = = = =


def NegoFibonachi(_Value):
    List1 = Fibonachi(_Value)
    List2 = [NewElementNego(lambda x, i: int(x*math.pow(-1, i+1)),
                            List1[i], i) for i in range(1, len(List1))]
    List2.reverse()
    List2.extend(List1)
    return List2

# = = = = = = =


def NewElement(func, List):
    List.append(func(List[len(List)-2], List[len(List)-1]))

# = = = = = = =


def Fibonachi(_Value):
    List = [0, 1]
    [NewElement(lambda x, y: x + y, List) for i in range(3, _Value+2)]
    return List

# = = = = = = =


def NewElementMultiplication(func, x, y):
    return func(x, y)
# = = = = = = =


def MultiplicationElementsOfList(_MyList):
    NewList = [NewElementMultiplication(lambda x, y: x*y,
                                        _MyList[i], _MyList[len(_MyList)-i-1]) for i in range(0, len(_MyList)//2)]

    NewList.append(_MyList[len(_MyList)//2] **
                   2) if len(_MyList) % 2 == 1 else NewList
    return NewList
# = = = = = = =


# ==========================================================================================================
# ==========================================================================================================


# task 1
os.system('cls')
print("\n")
print("Задача 5")
print('Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')
print("\n")
print("===== Введите значения ========\n")

while True:
    InputWord = input(
        'Введите  натуральное число >2 (длину последовательности Фибоначчи):     ')
    if InputWord.isdigit():
        DigitValue = int(InputWord)
        if DigitValue > 2:
            break
        else:
            print("Неверно! Введено натуральное число, но не больше 2")
    else:
        print("Неверно! Введено не натуральное число")
print()
print("===== Результат ========\n")
print(f'Список чисел Фибоначчи: {NegoFibonachi(DigitValue)}')
print("\n=============================\n")
input("ЭТО ПОСЛЕДНЯЯ ЗАДАЧА. НАЖМИТЕ ANYKEY ДЛЯ ЗАВЕРШЕНИЯ  ")

# ==========================================================================================================
# ==========================================================================================================


# task 2
os.system('cls')
print("\n")
print("Задача 2")
print('Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
print("\n")
print("===== Введите значения ========\n")
print('Введите через пробел значния списка, если не укажите ничего или не натуральное значение - это будет проигнорированно: \n ')
MyList = list(map(int, filter(lambda x: x.isdigit(), input().split())))
print("===== Результат ========\n")
print(f'Список = {MultiplicationElementsOfList(MyList)}')
print("\n=============================\n")
input("НАЖМИТЕ ANYKEY ДЛЯ ПЕРЕХОДА К СЛЕДУЮЩЕЙ ЗАДАЧЕ   ")

# ==========================================================================================================
# ==========================================================================================================
