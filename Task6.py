# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


number = input("Введите номер билета: ")
left = 0
right = 0
for i in range(len(number)//2):
    left += int(number[i])

for i in range(len(number)//2, len(number)):
    right += int(number[i])

print("Билет счастливый") if left == right else print("Билет несчастливый:(")
