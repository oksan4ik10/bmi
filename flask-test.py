from flask import Flask, render_template, request, escape

app = Flask(__name__)


@app.route('/')
def hi()->'html':
    return render_template('index.html', the_title='ИМТ')


@app.route('/', methods=['POST'])
def test():
    return render_template('index.html', the_title='ИМТ hjfgskhl')


if __name__=='__main__':
    app.run(debug=True)
    