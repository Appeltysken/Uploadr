from flask import Flask, request, redirect, render_template, send_from_directory, url_for
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')

def sanitized(filename):
    return os.path.splitext(filename.lower())[1] in ALLOWED_IMAGE_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename:
            filename = file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)

            if sanitized(filename):
                file.save(filepath)
                return redirect(url_for('index'))
            else:
                return "Разрешено загружать только изображения.", 400

    images = sorted([
        f for f in os.listdir(UPLOAD_FOLDER)
        if sanitized(f) and '.py' not in f.lower()
    ])
    return render_template('index.html', images=images)

@app.route('/uploads/<filename>', endpoint='uploaded_file')
def uploaded_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    if ".py" in filename:
        result = subprocess.run(['python3', filepath], capture_output=True, text=True)
        return f"<pre>{result.stdout or result.stderr}</pre>", 200, {'Content-Type': 'text/plain'}

    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
