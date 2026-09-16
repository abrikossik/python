x = int(input("Введите значение x: "))
epsilon = int(input("Введите значение epsilon: "))


def taylor_exp(x, epsilon):
    """e^x = 1 + x + x²/2! + x³/3! + ..."""
    result = 0.0
    temp = 1.0
    n = 1
    
    while abs(temp) >= epsilon:
        result += temp
        temp *= x / n
        n += 1
    
    return result

print (taylor_exp(x,epsilon))