x = float(input("Введите значение x: "))
epsilon = float(input("Введите значение epsilon: "))


def taylor_exp(x, epsilon):
    result = 0.0
    temp = 1.0
    n = 1
    
    while abs(temp) >= epsilon:
        result += temp
        temp *= x / n
        n += 1
    
    return result

print (taylor_exp(x,epsilon))
