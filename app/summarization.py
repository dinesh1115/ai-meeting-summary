from transformers import pipeline

def summarize_text(transcript_path):
    with open(transcript_path, "r") as f:
        text = f.read()
    
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']
