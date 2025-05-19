from flask import render_template, request
from app import app
from app.summarizer import summarize_text

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ''
    if request.method == 'POST':
        note = request.form['note']
        summary = summarize_text(note)
    return render_template('index.html', summary=summary)

@app.route('/upload')
def upload_form():
    return render_template('upload.html')

@app.route('/summarize', methods=['POST'])
def summarize_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename.endswith('.txt'):
        content = uploaded_file.read().decode('utf-8')
        summary = summarize_text(content)
        return render_template('summarizer.html', summary=summary)
    else:
        return "Only .txt files are supported", 400