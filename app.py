from flask import Flask, request, redirect, render_template, send_from_directory, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    images = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('index.html', images=images)

@app.route('/', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file and file.filename != '':
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('index'))

@app.route('/uploads/<filename>', endpoint='uploaded_file')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)