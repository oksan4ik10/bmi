from flask import Flask, render_template, request, escape
from main import bmi, print_table

app = Flask(__name__)


@app.route('/')
def hi()->'html':
    return render_template('index.html', the_title='ИМТ', display = 'd-none')


@app.route('/home', methods=['POST'])
def test():
  
    user = request.form['username']
    age = int(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])

    if request.form.get('save'):
        save = True
    else:
        save = False
    
    result = bmi(height, weight, user, age, save)

    return render_template('index.html', the_title='ИМТ результат', display = '', result = result)
    
@app.route('/result')
def print_result():
    tables = print_table()
    return render_template('results.html', the_title='Результаты', tables = tables, count = len(tables))


if __name__=='__main__':
    app.run(debug=True)
    