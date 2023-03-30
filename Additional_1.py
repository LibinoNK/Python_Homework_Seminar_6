# Даны числа a и b. Определите, сколько существует последовательностей из a нулей и b единиц, в которых никакие два нуля не стоят рядом.
# Ввод 5 8
# Вывод 126

def sequence(a, b):
    if a > b + 1: return 0
    if a == 0 or b == 0:
        return 1
    return sequence(a, b - 1) + sequence(a - 1, b - 1)


print(sequence(5, 8))
