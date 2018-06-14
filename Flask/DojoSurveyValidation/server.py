from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "JessicaSecret"

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
    if len(request.form['name']) < 1:
        flash("Name can't be empty!")
        return render_template('index.html')
    if len(request.form['comment']) > 120:
        flash("Your comment is funcking long!")
        return render_template('index.html')
    return render_template('result.html', name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])
app.run(debug=True)