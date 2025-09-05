import gradio as gr
import speech_recognition as sr

def recognize_from_file(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio)

            # Save transcription to a txt file
            with open("transcript.txt", "w") as f:
                f.write(text)

            return text, "transcript.txt"
        except:
            return "Sorry, could not recognize speech.", None

iface = gr.Interface(
    fn=recognize_from_file,
    inputs=gr.Audio(type="filepath", label="Upload Audio (.wav/.mp3)"),
    outputs=[
        gr.Textbox(label="Recognized Text"),
        gr.File(label="Download Transcript (.txt)")
    ],
    title="Voice to Text (Upload File)",
    description="Upload an audio file to transcribe speech into text."
)

iface.launch()


