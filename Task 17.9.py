def chek(lst)->bool:
    for c in range(len(lst)):
        try:
            lst[c] = float(lst[c])
        except:
            return False
    return True

def sort(lst):
    for i in range(len(lst)):
        idx_min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[idx_min]:
                idx_min = j
        if i != idx_min:
            lst[i], lst[idx_min] = lst[idx_min], lst[i]


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] < element and array[middle+1]>=element:
        return middle
    elif element <= array[middle]:
        return binary_search(array, element, left, middle)
    else:
        return binary_search(array, element, middle + 1, right)

#код программы
sequence = input("Введите последовательность чисел через пробел: ").split()
try:
    element = float(input('Введите любое число: '))
except:
    print('Введено некорректное значение. Введите число')
else:
    if chek(sequence):
        sort(sequence)
        idx = binary_search(sequence,element,0,len(sequence)-1)
        if  idx != False:
            print(sequence)
            print(f'Индекс элемента списка, удовлетворяющий условиям найден: {idx}')
        else:
            print(f'Элемента списка, удовлетворяющий условиям отсутствует')
    else:
        print('Введены некорректные значения в последовательности чисел')