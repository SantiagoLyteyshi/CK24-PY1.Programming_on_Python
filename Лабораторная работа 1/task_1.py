from types import NoneType

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_ = numbers[0:4] + numbers[5:]
sum_numbers = sum(numbers_)
len_numbers = len(numbers_)
sr_arif_numbers = sum_numbers / (len_numbers + 1)

i = 0
for i in range(len_numbers + 1):
    if type(numbers[i]) is NoneType:
        numbers[i] = sr_arif_numbers


# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)

# print(type(None))
