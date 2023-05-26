from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        input1 = int(request.form['input1'])
        input2 = int(request.form['input2'])
        operation = request.form['operation']
        result = None
        flag = True

        if operation == '+':
            result = input1 + input2
            res_opp = 'sum'
        elif operation == '-':
            result = input1 - input2
            res_opp = 'difference'
        elif operation == '*':
            result = input1 * input2
            res_opp = 'product'
        elif operation == '/':
            if input2 != 0:
                result = input1 / input2
                res_opp = 'quotient'
            else:
                result = "Error: Division by zero"
                flag = False
        elif operation == '%':
            result = input1 % input2
            res_opp = 'modulus'

        return render_template('calculator.html', flag=flag, res_opp=res_opp, input1=input1, input2=input2, operation=operation, result=result)

    return render_template('calculator.html', flag=False)

if __name__ == '__main__':
    app.run(debug=True)
