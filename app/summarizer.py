from transformers import pipeline

# Load model once
summarizer_model = pipeline('summarization', model='facebook/bart-large-cnn')

def summarize_text(text):
    if len(text.strip()) == 0:
        return "Please enter some text."
    try:
        summary = summarizer_model(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error summarizing: {str(e)}"