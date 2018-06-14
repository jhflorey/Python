from flask import Flask, render_template, jsonify, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = 'JessicaSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def render_character():
    my_images = {
        'purple':['donatello.jpg', "You choose Nonatello"],
        'blue': ['leonardo.jpg', "You choose Leonardo"],
        'orange': ['michelangelo.jpg', "You choose michelangelo"],
        'red' : ['raphael.jpg', "You choose raphael"]
    }
    result = my_images.get(request.form['color'], ['Ninja.png', "There's no ninja in that color"])

    return jsonify(image=result[0], message=result[1])


app.run(debug=True)