user_num =int(input("Введите положительное число :"))
max_num = 0
while user_num > 0:
    num = user_num % 10
    if num > max_num :
        max_num = num
    user_num = user_num // 10
print("Максимальная цифра в Вашем числе", max_num)
