from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponent(x, y):
    return x ** y

def modulus(x, y):
    return x % y

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    elif operation == 'exponent':
        result = exponent(num1, num2)
    elif operation == 'modulus':
        result = modulus(num1, num2)
    else:
        result = 'Invalid Operation'

    return jsonify(result=str(result))

if __name__ == '__main__':
    app.run(debug=True)
