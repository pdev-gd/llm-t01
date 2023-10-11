from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('AI 작사')

content = st.text_input('작사할 노래의 주제를 입력하세요')

if st.button('노래 가사 작성 요청하기'):
    with st.spinner('작사 중...'):
        result = chat_model.predict(content + "에 대한 노래 가사를 써줘")
        st.write(result)
        
#streamlit run main.py