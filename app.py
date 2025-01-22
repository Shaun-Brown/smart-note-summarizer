from flask import Flask, request, jsonify
from model.summarizer import summarize_text  # Import the summarize function

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Smart Note Summarizer API!"

@app.route('/summarize', methods=['POST'])
def summarize():
    # Check if a file is provided in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        # Read the file content (assuming text-based files)
        content = file.read().decode('utf-8')
        
        # Use the summarizer to process the content
        summary = summarize_text(content)
        
        return jsonify({"summary": summary})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
