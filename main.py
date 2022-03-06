
import math
from flask import Flask
app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/<int:number>')
def getArea(number):
    return "The circle area is " + str(number * number * math.pi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
