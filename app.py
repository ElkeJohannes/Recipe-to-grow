import os
from flask import Flask
from flask import render_template

if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
