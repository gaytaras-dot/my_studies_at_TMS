# main
# Домашнее задание от 01.07.2026
# Демонстрация некоторых возможностей Python

def greeting():
    """
    greeting(приветствие)
    Эта функция приветсвует пользователя
    """
    print('Привет, мир!')
    print('Привет лучшим ученикам десятилетия!\nНо это не точно!')

def addition(a, b):
    """
    addition(сложение)
    Эта функция производит сложение двух числел
    """
    add = a + b
    return add

def converting_to_decimal(bynary_str):
    """
    converting to decimal(перевод в десятичное) 
    Эта функция демонстрирует перевод бинарного числа в десятичное
    """
    num_list = []
    for x in bynary_str:
        num_list.append(int(x))
    num_list.reverse()
    decimal = 0
    for index, x in enumerate(num_list):  # используем enumerate для получения индекса
        decimal += x * (2 ** index)
    return decimal

def main():
    """Основная функция, запускающая программу"""
    greeting()
    print(f"Сумма 12 + 7 = {addition(12, 7)}")
    print(f"Бинарное число 0101011 в десятичном выражении равно {converting_to_decimal('0101011')}")

if __name__ == "__main__":
    """
    Функция реализует разделение между модулем (если как модуль - можно 
    использовать вдругих программах) и скриптом
    """
    main()