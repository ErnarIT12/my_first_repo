from math_utils.math_op import add, divide,subtract
print("1-сложение")
print("2-вычитание")
print("3-деление")
choice = int(input("Выберите операцию:"))
q2 = int(input("Введите число a:"))
q3 = int(input("Введите число b:"))
if choice == 1:
    print("Результат",add(q2, q3))
elif choice == 2:
    print("Результат",subtract(q2, q3))
else:
    print("Результат",divide(q2, q3))
