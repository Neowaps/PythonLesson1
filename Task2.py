# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


number = input("Введите число: ")
result = 0
for i in range(len(number)):
    result += int(number[i])
print(f"Сумма цифр числа: {result}")
