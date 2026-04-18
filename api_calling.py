import google.genai as genai
from dotenv import load_dotenv
import os,io
import streamlit as st
from gtts import gTTS


load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)

def text_generator(text):
    
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=text,
    )

    return(response.text)


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


def quiz_generator(images,difficulty):
    
    prompt=f"""Generate three quizes based on {difficulty},
    make sure to add markdown to differnetiate the options,
    user can select the answer and after selecting the answer ,
    you should show the correct answer so that user can justify his selected answer"""
    response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images,prompt],
   )
    return response.text