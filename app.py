from django.shortcuts import redirect
from flask import Flask, render_template, request, url_for, jsonify
from flask_restful import Resource, Api
from matplotlib.pyplot import get

app = Flask(__name__,
            static_url_path='', 
            static_folder='assets',
            template_folder='templates')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ai')
def about():
    return render_template('about.html')

@app.route('/output', methods=['POST', 'GET'])
def output():
    if request.method == 'POST':
        data = request.form.get('data')
        email = request.form.get('email')
        return render_template('output.html', data=data, email=email)
    else:
        return redirect("/ai", code=307)

@app.route('/handledata', methods=['POST'])
def handledata():
    print(request.form.get('data'))
    print(request.form.get('email'))
    # print(request.email)
    return jsonify("ok")

if __name__ == '__main__':
    app.run(debug=True, port=8080)
