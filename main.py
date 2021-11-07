user_height = 1.60
user_weight = 77.8

bmi = user_weight/(user_height**2)

print('Ваш ИМТ составляет: ', round(bmi,2))
if bmi <=16:
    print('Выраженный дефицит массы тела')
elif bmi <=18.5:
    print('Недостаточная (дефицит) масса тела')
elif bmi <=25:
    print('Норма')
elif bmi <=30:
    print('Избыточная масса тела (предожирение)')
elif bmi <= 35:
    print('Ожирение 1 степени')
elif bmi <= 40:
    print('Ожирение 2 степени')
else:
    print('Ожирение 3 степени')