from os import name
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from main import bmi, print_table

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #чтобы работал flash

#работа с БД в mySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/bmi'
db = SQLAlchemy(app)

class ResultSave(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer(), primary_key=True, index=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    height = db.Column(db.Float(), nullable=False)
    weight = db.Column(db.Float(), nullable=False)
    bmi = db.Column(db.Float(), nullable=False)
    # def __repr__(self):
	#     return "<{}:{}>".format(self.id,  self.title[:10])
db.create_all()

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
        flash(result[0], 'alert-primary')
        user = ResultSave(name = user, age = age , height = height, weight = weight, bmi = result[1])
        db.session.add(user)
        db.session.commit()



    return redirect(url_for('hi'))

    
@app.route('/results')
def print_result():
    #получаем данные из БД
    users =  ResultSave.query.all()
    return render_template('results.html', the_title='Результаты', tables = users, count = len(users))


if __name__=='__main__':
    app.run(debug=True)
    