from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return"<h1> Hello biertje </h1>"


@app.route('/hello')
def hello():
    return "hello world"

@app.route('/greet/<name>')
def greet(name):
    return f"hello {name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555, debug=True)