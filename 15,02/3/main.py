from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def slogan():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    lines = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return '<br>'.join(lines)


@app.route('/image_mars')
def image_mars():
    return render_template("image_mars.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
