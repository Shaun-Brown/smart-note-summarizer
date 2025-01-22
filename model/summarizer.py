from transformers import pipeline

# Initialize the summarizer pipeline (you can choose T5 or BART)
summarizer = pipeline("summarization")

def summarize_text(text: str) -> str:
    """
    Summarize the provided text using Hugging Face's model.
    """
    try:
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return str(e)
