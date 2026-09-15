size_array = int(input("Введите размер массива: "))
arr = []

for _ in range (size_array):
    arr.append(int(input("Введите элемент массива ")))

def search_min_el(arr):
    return min(arr)


def search_last_zero_el(arr):
    sum_val = 0
    for i in range(len(arr)-1,-1,-1):
        sum_val += arr[i]
        if arr[i] == 0:
            break
    return sum_val

        
def magic(arr):
    temp_arr = []                       #yvidel v ii
    for i in range(0,len(arr),2):       #if not arr:
        temp_arr.append(arr[i])         #   return []
    for i in range(1,len(arr),2):       #return arr[::2] + arr[1::2]
        temp_arr.append(arr[i])
    arr[:] = temp_arr
    return arr

print(search_min_el(arr))
print(search_last_zero_el(arr))
print(magic(arr))
