number = int(input("Введите интересующее количество секунд для подсчета :"))
hours = int(number / 3600)
minutes = int(number / 60 - (hours*60))
seconds = int(number % 60)
#Время в формате чч:мм:сс
print(f"{hours:02}.{minutes:02}.{seconds:02} ")
