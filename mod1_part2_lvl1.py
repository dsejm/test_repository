num_1 = int(input("Введите 1 число: "))
num_2 = int(input("Введите 2 число: "))
num_3 = int(input("Введите 3 число: "))
if num_1 == num_2 & num_1 == num_3:
    print("Совпадающих чисел: 3")
elif num_1 == num_2 or num_1 == num_3:
    print("Совпадающих чисел: 2")
elif num_2 == num_3:
    print("Совпадающих чисел: 2")
else:
    print("Совпадающих чисел: 0")
