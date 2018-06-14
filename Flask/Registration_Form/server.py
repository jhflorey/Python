from flask import Flask, flash, render_template, redirect, request, flash, session
import re
app = Flask(__name__)
app.secret_key = 'JessicaSecret'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    email = request.form['email']
    first_name = request.form['first_name'].strip()
    last_name = request.form['last_name'].strip()
    password= request.form['password']
    confirm_password = request.form['confirm_password']
    if len(email) == 0 or len(first_name) == 0 or len(last_name)==0 or len(password) == 0 or len(confirm_password) == 0:
        flash('All fields are required and must not be blank')
        return redirect('/')
    if (not first_name.isalpha()) or (not last_name.isalpha()):
        flash('First and Last Name cannot contain any numbers')
        return redirect('/')
    if len(password) < 8:
        flash('Password should be more than 8 characters')
        return redirect('/')
    if not EMAIL_REGEX.match(email):
        flash('Email should be a valid email')
        return redirect('/')
    if password != confirm_password:
        flash('Password and Password Confirmation should match')
        return redirect('/')
    return render_template('result.html', email=email, first_name=first_name, last_name=last_name)

app.run(debug=True)
