from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("Note summary & Quiz generator")
st.markdown("Upload upto 3 images to genarate note summary and quizess")
st.divider()

with st.sidebar:
        st.header("Controls")
        images = st.file_uploader(
            "Upload a image",
            type=["jpg","jpeg","png"],
            accept_multiple_files=True
            )   
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
            st.subheader("Your note")
            st.text("Note will be shown here")
            
        # audio
        with st.container(border=True):
            st.subheader("Audio")
            st.text("Note will be shown here")
            
        # quiz
        with st.container(border=True):
            # st.subheader(f "Quiz ({selected_option})")
            st.subheader(f"Quiz ({selected_option})")
            st.text("Note will be shown here")
            
            
            
        

