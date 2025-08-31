def add(a, b):
    return a+b
def divide(a, b):
    try:
        return a/b 
    except ZeroDivisionError:
        return "Ошибка,Число нельзя делить на ноль!"
def subtract(a, b):
    return a-b


