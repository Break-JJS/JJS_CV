from flask import Flask, request, redirect
import cv2
app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask Server for CV'

@app.route('/read/<int:id>')
def read(id):    
    return f'{id}'

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return "GET"
    elif request.method == 'POST':
        return "POST"

print(cv2.__version__)
app.run(debug=True)