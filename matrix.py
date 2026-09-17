size_mtr = int(input("Введите размеры матрицы: "))

mtr = []

def fill_mtr(mtr,size):
    print("Вводите элементы матрицы размеров ", size," на ", size)
    for i in range(size):
        row = []
        for j in range(size):
            val = int(input())
            row.append(val)
        mtr.append(row)
            
def print_mtr(mtr,size):
    for i in range(size):
        for j in range(size):
            print(mtr[i][j], end = " ")
        print()

def check_lower_right_triangle(mtr,size):
    max_val = None
    for i in range(size):
        for j in range(size):
            if i + j >= size - 1:
                if mtr[i][j] is None or mtr[i][j]> max_val:
                    max_val = mtr[i][j]                
    return max_val

def find_max_positive_el(mtr, size):
    max_r, max_c, max_val = -1, -1, -1

    for i in range(size):
        for j in range(size):
            if mtr[i][j] > 0 and mtr[i][j] > max_val:
                max_val = mtr[i][j]
                max_r, max_c = i, j

    if max_r == -1:
        print("В матрице нет положительных элементов, перестановка невозможна.")
        return
    return max_r,max_c,max_val

def swap_to_top_left(mtr,size, max_r, max_c):
    
    if max_r == -1 and max_c == -1:
        print("В матрице нет положительных элементов, перестановка невозможна.")
        return

    mtr[0], mtr[max_r] = mtr[max_r], mtr[0]

    for i in range(size):
        mtr[i][0], mtr[i][max_c] = mtr[i][max_c], mtr[i][0]

fill_mtr(mtr,size_mtr)

max_in_triangle = check_lower_right_triangle(mtr, size_mtr)
max_r, max_c, max_val = find_max_positive_el(mtr, size_mtr)

print("максимальный положительный элемент: {max_val} на позиции [{max_r}][{max_c}]")
swap_to_top_left(mtr, size_mtr, max_r, max_c)
print_mtr(mtr, size_mtr)