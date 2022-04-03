import os
from flask import Flask, render_template, request, url_for, redirect
from pred import check

app = Flask(__name__, static_folder="static")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/exames')
def exames():
    return "exames"

@app.route('/home')
def forms():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

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

    status = check(filename)

    return render_template('resultado.html', image_name=filename, pred=status)

if __name__ == "main":
    app.run(debug=True)
