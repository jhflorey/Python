from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html',all=True)

@app.route('/ninja/<ninja_color>')
def ninja_color(ninja_color):
    ninja_dict ={'blue':'/static/image/leonardo.jpg',
                 'orange':'/static/image/michelangelo.jpg',
                 'red':'/static/image/raphael.jpg',
                 'purple':'/static/image/donatello.jpg',
                 }

    return render_template('ninja.html',image_src=ninja_dict.get(ninja_color,'/static/image/notapril.jpg'), all=False)

app.run(debug=True)
