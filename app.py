import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'm4a'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    name = request.form.get('name')
    file = request.files.get('file')
    if name and file and allowed_file(file.filename):
        filename = secure_filename(f"{name}_{file.filename}")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f"感謝 {name} 上傳成功！"
    return "上傳失敗，請檢查輸入。"

@app.route('/teacher')
def teacher():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('teacher.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)