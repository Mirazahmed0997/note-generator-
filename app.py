import google as genai
import os
from dotenv import load_dotenv
import streamlit as st
from api_calling import note_generator
from api_calling import audio_tracription
from api_calling import quiz_generator
from api_calling import text_generator
from PIL import Image


load_dotenv()

st.title("Note summary & Quiz generator")
st.markdown("Upload upto 3 images to genarate note summary and quizess")
st.divider()


with st.container(border=True):
        text=st.text_input("Ask anything to Miraz")
        if text:
            ans=text_generator(text)
            st.markdown(ans)



with st.sidebar:
        st.header("Controls")
        
        images = st.file_uploader(
            "Upload a image",
            type=["jpg","jpeg","png"],
            accept_multiple_files=True
            ) 
        
        
        
        converted_images=[]  
        for img in images:
            converted_image=Image.open(img)
            converted_images.append(converted_image)
            
            
            
        if images:
            if len(images)>3:
                st.error("You are uploading more three image")
            else:
                col= st.columns(len(images))
                for i,img in enumerate(images):
                    with col[i]:
                        st.image(img)
            
    
    
    # difficulty
    
        selected_option=st.selectbox("Select the difficulties",("Easy","Medium","Hard"),index=None)
        
        # if not selected_option:
        #     st.error("Select a option")    

        submit_button=st.button("Submit",type="primary")

if submit_button:
    if not images:
        st.error("Need to upload atleast one image")
    if not selected_option:
        st.error("Please select a dificulty option")
    if images and selected_option:
        
        # notes
        with st.container(border=True):
            with st.spinner("Miraz is writting about your image"):
                 notes=note_generator(converted_images)
                 st.markdown(notes)
            
        # audio
        with st.container(border=True):
            st.subheader("Audio")
            with st.spinner("Transforming to audio"):
                notes=notes.replace("#","")
                notes=notes.replace("*","")
                notes=notes.replace("-","")
                notes=notes.replace("''","")
                notes=notes.replace("`","")
                
                
                audio=audio_tracription(notes)
            
        # quiz
        with st.container(border=True):
            # st.subheader(f "Quiz ({selected_option})")
            st.subheader(f"Quiz ({selected_option})")
            with st.spinner("Generating quiz"):
                quizzes = quiz_generator(converted_images,selected_option)
                st.markdown(quizzes)
            
            
            
        

