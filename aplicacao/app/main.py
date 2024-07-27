import streamlit as st
from openai import OpenAI
import os
from streamlit_chat import message
os.environ["OPENAI_API_KEY"] = "sk-proj-UU0ryLRcyswapiok1j5QT3BlbkFJ1wFEn2YlJBRSeQoRyxZP"
client = OpenAI()
model = "gpt-3.5-turbo"


st.title("Assistente pessoal")
st.write("Este é seu assistente pessoal para informações, pergunte a ele qualquer coisa")
if 'historico' not in st.session_state:
    st.session_state.historico = []

pergunta = st.text_input("De qual informação vc precisa ?")
enviar = st.button("Enviar")
if enviar:
    st.session_state.historico.append({"role": "user", "content": pergunta})
    resposta = client.chat.completions.create(
                model=model,
                messages=st.session_state.historico,
                max_tokens=500,
                n=1
            )
    st.session_state.historico.append({"role": "assistant", "content": resposta.choices[0].message.content})

if len(st.session_state.historico) > 0:
    for i in range(len(st.session_state.historico)):
        if i % 2 == 0:
            message(st.session_state.historico[i]["content"], is_user=True)
        else:
            message(st.session_state.historico[i]["content"])
