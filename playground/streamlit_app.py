# playground/streamlit_app.py
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/generate"

st.title("Dynamic URL RAG Playground")

url = st.text_input("Paste Web URL")
query = st.text_area("Ask a question")

strategy = st.sidebar.selectbox(
    "Decoding Strategy",
    ["greedy", "top_k", "top_p", "beam"]
)

temperature = st.sidebar.slider("Temperature", 0.1, 2.0, 1.0)
top_k = st.sidebar.slider("Top K", 1, 50, 10)
top_p = st.sidebar.slider("Top P", 0.1, 1.0, 0.9)
repetition_penalty = st.sidebar.slider("Repetition Penalty", 1.0, 2.0, 1.1)
num_beams = st.sidebar.slider("Beam Width", 1, 8, 4)
max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 200)

if st.button("Generate"):
    response = requests.post(API_URL, json={
        "url": url,
        "query": query,
        "strategy": strategy,
        "temperature": temperature,
        "top_k": top_k,
        "top_p": top_p,
        "repetition_penalty": repetition_penalty,
        "max_tokens": max_tokens,
        "num_beams": num_beams
    })

    st.write(response.json()["answer"])
