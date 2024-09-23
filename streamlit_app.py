from st_audiorec import st_audiorec
import streamlit as  st

import whisper
import time


wav_audio_data = st_audiorec()



uploaded_audio = st.file_uploader("Upload an audio file", type=['mp3', 'wav', 'ogg'])
if uploaded_audio:
    file_path = uploaded_audio.name
    # Load the 'tiny' model to ensure compatibility with Streamlit Cloud
    model = whisper.load_model("tiny")
    
    start = time.time()
    result = model.transcribe(file_path)
    end = time.time()
    st.write(end-start)
    
    st.write(result['text'])
