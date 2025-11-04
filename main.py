import streamlit as st 
import google.generativeai as genai 
from mykey import api_key 
 
genai.configure(api_key=api_key) 
 
st.title("💬 Gemini Chatbot") 
user_input = st.text_input("You: ", "") 
 
if user_input: 
    model = genai.GenerativeModel("models/gemini-2.0-flash") 
    response = model.generate_content(user_input) 
    st.write("🤖 Gemini:", response.text) 
  
