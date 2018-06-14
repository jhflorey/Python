from flask import Flask , render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.form['action'] == 'register':
        message = "you are register"
    elif request.form['action'] == 'login':
        message = "you successful login with %s" %(request.form['email'])
    return render_template('result.html', message=message)
app.run(debug=True)