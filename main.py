from flask import Flask

app = Flask(__name__)
lines = []
for i in range(1000):
    lines.append("1")

@app.route('/users/<int:i>')
def profile(i):
    return f'<h>Профиль {i}</h>'


@app.route("/about")
def index():
    return "<pre>" + "\n".join(lines)+"<pre>"


@app.route("/feed/")
def page_feed():
    return "Лента пользователя"


app.run(host='127.0.0.6', port=890)


