from flask import Flask, request
from service import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/1')
def hello_world1():
    return "Hello World1"


@app.route('/table/<int:i>')
def table(i):
    return n_table(i)


@app.route('/table1/<int:i>')
def table1(i):
    return n_table1(i)


@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        name = request.json['name']
        id = request.json['id']
        try:
            if type(name) == str:
                print('...............name....', type(name))
                print('...........id.................', type(id))
                return f'my name is {name} and id is {id}'
            else:
                raise ValueError("you have entered invalid string")
        except ValueError as ve:
            print(ve)
            return 'from except block'
    else:
        return "im a get method"


@app.route('/post1', methods=['POST'])
def post1():
    if request.method == 'POST':
        i = request.json['i']
        j = request.json['j']
        return pattern(i, j)


if __name__ == '__main__':
    app.run(debug=True)
