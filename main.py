
#основная программа
user_height = 1.60
user_weight = 77.8
name = 'Oksana'
age = 28

results = {}

bmi = round(user_weight/(user_height**2),2)

print('Ваш ИМТ составляет: ', bmi,2)
if bmi <=16:
    res = ('Выраженный дефицит массы тела')
elif bmi <=18.5:
    res = ('Недостаточная (дефицит) масса тела')
elif bmi <=25:
    res = ('Норма')
elif bmi <=30:
    res = ('Избыточная масса тела (предожирение)')
elif bmi <= 35:
    res = ('Ожирение 1 степени')
elif bmi <= 40:
    res = ('Ожирение 2 степени')
else:
    res = ('Ожирение 3 степени')


#запись и чтение из файла
results = [name,age, user_height, user_weight, bmi, res]
print (results)


with open('file.txt','a') as file:
    for i in results:
        item = str(i)
        file.write(item)
        file.write(' ')
    file.write('\n')

with open('file.txt', 'r') as file:
    content = file.readlines()
    for i in content:
        print(i.strip())