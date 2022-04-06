import os
from flask import Flask, render_template, request
from pred import *

app = Flask(__name__, static_folder="static")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def forms():
    return render_template('form.html', title="Formularios")

@app.route('/exames')
def exames():
    return render_template("exames.html", title="Exames")

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html', title="Equipe")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    target = os.path.join(APP_ROOT, 'static/images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        print(filename)
        dest = '/'.join([target, filename])
        print(dest)
        file.save(dest)
        output = predict(filename)
        return render_template("exames.html", label=output, imagesource=filename)


if __name__ == "main":
    app.run(debug=True)
