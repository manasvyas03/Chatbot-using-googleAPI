# Installations ------------------------------------------------------------------------
import streamlit as st
from pathlib import Path
import google.generativeai as genai
from api_key import p1
from api_key import a_k1

# Config
genai.configure(api_key=a_k1)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

system_prompt = p1  


st.set_page_config(page_title="General Doctor", page_icon="robot")

st.image("image.png", width=100)
st.title("General Doctor")
st.subheader("Talk to your Doctor.")

# Chat input for conversation
user_input = st.text_input("What problem are you facing?")

# Button to submit the input and generate the response
submit_button = st.button("Chat")

# When user clicks the 'Chat' button
if submit_button and user_input:
    # Combine user input with system prompt
    prompt = f"{system_prompt}\nUser: {user_input}\nDoctor:"
    
    # Generate response from the model
    response = model.generate_content(prompt)
    
    # Display response
    if response:
        st.title("Doctor's Response:")
        st.write(response.text)
