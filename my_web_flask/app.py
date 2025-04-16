# app.py
from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            return render_template('index.html')
    return render_template('index.html')

@app.route('/outputs/<filename>')
def output_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)