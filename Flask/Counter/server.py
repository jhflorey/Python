from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "HuySecret"

@app.route('/')
def index():
    if 'times' in session:
        session['times'] +=1
    else:
        session['times']= 1
    return render_template('index.html')

@app.route('/increase_2')
def increase_2():
    if 'times' not in session:
        session['times'] = 0
    else:
        session['times'] += 1
    return redirect('/')
    
@app.route('/rest_1')
def reset_1():
    session['times'] = 1
    return render_template('index.html')
app.run(debug=True)