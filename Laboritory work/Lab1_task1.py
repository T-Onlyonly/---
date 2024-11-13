numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
print("Оригинальный список:", numbers)
# Найдем индекс пропущенного элемента
missing_index = numbers.index(None)

# Вычислим сумму всех чисел, кроме пропущенного
sum_excluding_none = sum(num for num in numbers if num is not None)

# Определим количество чисел, включая пропущенный элемент
total_elements = len(numbers)

# Вычислим среднее арифметическое
average = sum_excluding_none / total_elements

# Заменим пропущенный элемент на среднее арифметическое
numbers[missing_index] = average

# TODO заменить значение пропущенного элемента средним арифметическим
#Выведем измененный список
print("Измененный список:", numbers)