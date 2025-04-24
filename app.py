from flask import Flask, render_template
from routes.tasks import task_bp

app = Flask(__name__)
app.register_blueprint(task_bp)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

