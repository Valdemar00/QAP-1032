numbers = input('Введите любое количество чисел через пробел: ').split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

import operator

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
list_of_numbers = merge_sort(numbers)

print(f'''Список чисел, отсортированный по возрастанию:''', *(list_of_numbers))

additional_number = int(input('Введите еще одно число: '))


def binary_search(array, element, left, right):
    try:
        if left > right:
            return False

        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return "Ошибка! Выходит за границы списка. Введите другое число."

if not binary_search(list_of_numbers, additional_number, 0, len(list_of_numbers)):
    n = min(list_of_numbers, key=lambda x: (abs(x - additional_number), x))
    index = list_of_numbers.index(n)
    minimum_index = index - 1
    maximum_index = index + 1
    if n < additional_number:
        print(f'''Вашего элемента не было в списке.
Индекс позиции ближайшего элемента, который МЕНЬШЕ введенного Вами числа: {index} (число  {n} ).
Индекс позиции ближайшего элемента, который БОЛЬШЕ введенного Вами числа: {maximum_index} (число {list_of_numbers[maximum_index]} ).''')
    elif n > additional_number:
        print(f'''Вашего элемента не было в списке.
Индекс позиции ближайшего элемента, который БОЛЬШЕ введенного Вами числа: {list_of_numbers.index(n)} (число {n} ).
В списке нет элементов МЕНЬШЕ Вашего.''')
    elif list_of_numbers.index(n) == 0:
        print(f'''Номер позиции Вашего элемента в списке: {list_of_numbers.index(n)}''')
    elif minimum_index < 0:
        print(f'''Вашего элемента не было списке.
Индекс позиции ближайшего элемента, который БОЛЬШЕ введенного Вами числа: {list_of_numbers.index(n)} (число {n} ).
В списке нет элементов МЕНЬШЕ Вашего.''')
else:
    print(f'''Индекс позиции Вашего элемента в списке: {binary_search(list_of_numbers, additional_number, 0, len(list_of_numbers))}''')
