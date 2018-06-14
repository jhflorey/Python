from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/process', methods=['Post'])
def process():
  #do some validations here!copy
  if len(request.form['name']) < 1:
      flash("Name cannot be empty!")
  else:
      flash("success! Your name is {}".format(request.form['name']))
  return redirect('/')
app.run(debug=True)