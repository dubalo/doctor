# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import OpenAI
import streamlit as st 

llm = OpenAI()
st.title("내과 전문의")
content = st.text_input("증상을 알려 주세요.")

if st.button("진료 요청하기"):
    with st.spinner("진료 중..."):
        result = llm.invoke(content + "증상에 대해 진료해주세요.")
        st.write(result)
