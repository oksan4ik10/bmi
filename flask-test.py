from flask import Flask, render_template, request, flash, redirect, url_for
from main import bmi, print_table

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #чтобы работал flash



@app.route('/')
def hi()->'html':
    return render_template('index.html', the_title='ИМТ', display = 'd-none', result='')


@app.route('/home', methods=['POST'])
def test():

    print(request.form)
    user = request.form['username']
    age = request.form['age']
    height = request.form['height']
    weight = request.form['weight']

    if (not(user)):
        flash('Не введено имя', 'alert-danger') 
    if(not(age)):
        flash('Не введен возраст', 'alert-danger') 
    if (not(height)):
        flash('Не введен рост', 'alert-danger') 
    if(not(weight)):
        flash('Не введен вес', 'alert-danger') 

    if not weight or not height or not age or not user:
            return redirect(url_for('hi'))


    age = int(age)
    height = float(height)
    weight = float(weight)


    if request.form.get('save'):
        save = True
    else:
        save = False
    
    result = bmi(height, weight, user, age, save)

    if not result:
        flash('Данные введены некорректно', 'alert-danger')
    else:
        flash(result, 'alert-primary')


    return redirect(url_for('hi'))

    
@app.route('/results')
def print_result():
    tables = print_table() #получаем результат сохраненных данных из файла
    return render_template('results.html', the_title='Результаты', tables = tables, count = len(tables))


if __name__=='__main__':
    app.run(debug=True)
    