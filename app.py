import os

import gradio as gr
from clipsai import Transcriber
import tempfile


def transcribe_audio(audio_file: str):

    transcriber = Transcriber()

    # Uncomment this line to use CPU and int8 precision. Use this only normally if it crashes on your machine.
    # transcriber = Transcriber(device='cpu', precision='int8')

    transcription = transcriber.transcribe(audio_file_path=audio_file)
    return transcription.text

iface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.File(label="Upload Audio File"),
    outputs="text",
    title="Audio Transcription Service",
    description="Upload your audio file and get the transcription as a text file."
)
if __name__ == "__main__":
    iface.launch(debug=True)
