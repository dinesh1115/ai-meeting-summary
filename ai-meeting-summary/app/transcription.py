import whisper
import os

def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    
    transcript_path = "data/transcripts/transcript.txt"
    os.makedirs(os.path.dirname(transcript_path), exist_ok=True)
    with open(transcript_path, "w") as f:
        f.write(result['text'])
    return transcript_path
