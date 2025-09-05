Voice to Text Converter

This Gradio application allows you to transcribe speech from audio files (WAV or MP3) into text using Google's Web Speech API. It provides a user-friendly interface for uploading audio and displays the recognized text, along with an option to download the transcription as a text file.

Features

Audio Upload: Easily upload .wav or .mp3 audio files.

Speech Recognition: Transcribes spoken words into written text.

Text Output: Displays the recognized text directly in the application.

Transcript Download: Provides a downloadable .txt file of the transcription.

Technologies Used

Gradio: For creating the interactive web interface.

SpeechRecognition: A Python library for performing speech recognition, utilizing various APIs including Google Web Speech API.

Python: The core programming language.

Setup and Installation

Clone the Repository (or create the file):
If you have a GitHub repository, clone it:

code
Bash
download
content_copy
expand_less

git clone <your-repository-url>
cd <your-repository-name>

Otherwise, save the provided Python code as app.py (or any other .py file name).

Create a Virtual Environment (Recommended):

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

Install Dependencies:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
pip install gradio SpeechRecognition
How to Run

Start the Gradio Application:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python app.py

Access the Interface:
Once the application starts, it will provide a local URL (e.g., http://127.0.0.1:7860). Open this URL in your web browser.

Usage

Upload Audio: Click on the "Upload Audio (.wav/.mp3)" box and select an audio file from your computer.

View Recognized Text: After the file is uploaded and processed, the transcribed text will appear in the "Recognized Text" box.

Download Transcript: A "Download Transcript (.txt)" link will appear, allowing you to download the transcribed text as a file.

Example

Here's a visual example of the application in action:
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/5a15925e-6c4f-4fea-8c13-7dd2cb56b64e" />
