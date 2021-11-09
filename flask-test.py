from flask import Flask, render_template, request, escape
from main import bmi, print_table

app = Flask(__name__)


@app.route('/')
def hi()->'html':
    return render_template('index.html', the_title='ИМТ', display = 'd-none', done = 'd-none')


@app.route('/home', methods=['POST'])
def test():
    print(request.form)
    user = request.form['username']
    age = request.form['age']
    height = request.form['height']
    weight = request.form['weight']

    if (not user) or (not age) or (not height) or (not weight):
        return render_template('index.html', the_title='ИМТ результат', done='',display = 'd-none', result = 'Не все данные были заполнены')

    age = int(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])


    if request.form.get('save'):
        save = True
    else:
        save = False
    
    result = bmi(height, weight, user, age, save)

    return render_template('index.html', the_title='ИМТ результат', display = '',done = 'd-none', result = result)
    
@app.route('/results')
def print_result():
    tables = print_table()
    return render_template('results.html', the_title='Результаты', tables = tables, count = len(tables))


if __name__=='__main__':
    app.run(debug=True)
    