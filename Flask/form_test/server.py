from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # we'll talk about the following two submission
    # about forms
    name = request.form['name']
    email = request.form['email']
    print(request.form)
    # redirects back to the '/' route
    return redirect('/')

@app.route('/users/<username>')
def show_user_profile(username):
    print(username)
    return render_template("users.html")

@app.route('/route/with/<vararg>')
def handle_function(vararg):
    # here you can the variable "vararg"
    # if you want to see what our argument looks like
    print(vararg)
    # we could do other things with information from this point on such as:
    # use it to retrieve some records from the database
    # render a particular template
    return vararg
@app.route('/users/<username>/<id>')
def show_user_profile_with_Id(username, id):
    print(username)
    print(id)
    return "%s has id: %s" %(username,id)

@app.route('/show')
def show_user():
    return render_template('users.html', name='Jessica', email='jessica@florey.com')
app.run(debug=True) # run our server