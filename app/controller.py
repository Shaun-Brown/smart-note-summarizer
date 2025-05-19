from flask import render_template, request
from app import app
from app.summarizer import summarize_text

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ''
    if request.method == 'POST':
        note = request.form['note']
        summary = summarize_text(note)
    return render_template('summarizer.html', summary=summary)