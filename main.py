from flask import Flask

app = Flask(__name__)



@app.route('/users/<int:i>')
def profile(i):
    return f'<h>Профиль {i}</h>'


@app.route("/about")
def index():
    return "Я about"


@app.route("/feed/")
def page_feed():
    return "Лента пользователя"


app.run(host='127.0.0.6', port=890)

# app.add_url_rule('/', viewfunc=page_index)
