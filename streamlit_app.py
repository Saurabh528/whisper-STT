from st_audiorec import st_audiorec
import streamlit as  st

import whisper
import time


wav_audio_data = st_audiorec()



if wav_audio_data:
    file_path = 'save_recorded_audio.wav'
    
    # Save the audio file as .wav
    with open(file_path, "wb") as f:
        f.write(wav_audio_data)
    
    st.success(f"WAV file saved successfully as {file_path}")




# Load the 'tiny' model to ensure compatibility with Streamlit Cloud
model = whisper.load_model("tiny")

start = time.time()
result = model.transcribe("save_recorded_audio.wav")
end = time.time()
st.write(end-start)

st.write(result['text'])
