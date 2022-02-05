import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/odd_even/<int:number>')
def odd_even(number):
    return render_template('odd_even.html', number=number)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.load(f)
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route("/queque")
def queue():
    return render_template("queque.html", title="ОЧЕРЕДЬ")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')