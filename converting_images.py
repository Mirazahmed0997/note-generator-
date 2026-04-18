import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image


load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)


images = st.file_uploader(
            "Upload a image",
            type=["jpg","jpeg","png"],
            accept_multiple_files=True
            ) 

#oconterted inage to PIL Image

if images: 
     for img in images:
        converted_image = Image.open(img)
     prompt=""" summarize the picture in note format at max 100 words, 
     make sure to add neccessary markdown to differntiate different"""
     
     response=client.models.generate_content(
     model="gemini-3-flash-preview",
     contents=[converted_image,prompt],
     )
     
     st.text(response.text)
     