from google import genai
from dotenv import load_dotenv
import os,io
import streamlit as st
from gtts import gTTS


load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)


def note_generator(images):
    
    prompt=""" summarize the picture in note format at max 100 words, 
    make sure to add neccessary markdown to differntiate different"""
    response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images,prompt],
   )
    return response.text
    
    
def audio_tracription(text):
    speech=gTTS(text,lang="en",slow=False)

    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)
    st.audio(audio_buffer)   
    
    return audio_buffer 