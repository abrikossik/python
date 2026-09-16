num = int(input("Введите натуральное число: "))


def first_task(num):
    temp_str = str(num)
    most_common_num = max("0123456789", key = temp_str.count)
    temp_str = most_common_num + temp_str + most_common_num
    return(int(temp_str));

def check_armstr_num(num):
    temp_str = str(num)
    power = len(temp_str)
    return sum(int(i)**power for i in temp_str) == num

def second_task(num):
    arr = []
    for i in range(1, num + 1):
        if check_armstr_num(i):
            arr.append(i)
    return arr


def third_task(start,end):
    arr = []
    i = start
    while i <= end:
        check_armstr_num(i)
        i += 1
    return arr

print(first_task(num))
print(second_task(num))

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
result_3 = third_task(start, end)

if result_3:
    print("Числа Армстронга в диапазоне [{start}, {end}]: {result_3}")
else:
    print("В диапазоне [{start}, {end}] чисел Армстронга не найдено.")