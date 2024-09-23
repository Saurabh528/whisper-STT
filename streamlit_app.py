from st_audiorec import st_audiorec
import streamlit as  st
import os
import whisper
import time


wav_audio_data = st_audiorec()



uploaded_audio = st.file_uploader("Upload an audio file", type=['mp3', 'wav', 'ogg'])
if uploaded_audio:
    file_path = os.path.join("tempDir", uploaded_audio.name)  # You can customize the directory
    
    # Ensure the directory exists
    os.makedirs("tempDir", exist_ok=True)
    
    # Write the file to the temporary directory
    with open(file_path, "wb") as f:
        f.write(uploaded_audio.getbuffer())
    # Load the 'tiny' model to ensure compatibility with Streamlit Cloud
    model = whisper.load_model("tiny")
    
    start = time.time()
    result = model.transcribe(file_path)
    end = time.time()
    st.write(end-start)
    
    st.write(result['text'])
