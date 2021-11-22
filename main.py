def bmi(user_height, user_weight, name, age, save = False) -> str:

    bmi = round(user_weight/(user_height**2),2)

    if bmi == 0.0:
        return False
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



    
    return ['ИМТ: '+str(bmi)+'. '+res, bmi]

# print(bmi(1.64, 78, 'Oksana', 27, True))

def print_table():
    with open('file.txt', 'r') as file:
        content = file.readlines()
        result = []
        for i in content:
            res = i.strip().split('|')
            del res[-1]
            result.append(res)
    return result



