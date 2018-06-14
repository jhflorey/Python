from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = 'JessicaSecret'

@app.route('/')
def index():
    return render_template('index.html',fail=False)

@app.route('/result', methods=['POST'])
def result():
    red = int(request.form['red'])
    blue = int(request.form['blue'])
    green = int(request.form['green'])
    if (0<=red<=255) and (0<= blue <=255) and (0<= green <=255):
        # good case
        return render_template('index.html',red=red,blue=blue, green=green,fail=False)
    else:
        return render_template('index.html',fail=True)

app.run(debug=True)



