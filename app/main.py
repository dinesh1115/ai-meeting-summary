from transcription import transcribe_audio
from summarization import summarize_text
from utils import save_file

def main():
    audio_file = "data/audio/meeting.mp3"
    transcript_path = transcribe_audio(audio_file)
    summary = summarize_text(transcript_path)
    print(f"Summary:\n{summary}")

if __name__ == "__main__":
    main()
