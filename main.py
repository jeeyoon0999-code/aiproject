import streamlit as st
st.title('내 첫번째 웹앱')
name=st.text_input('이름을 입력해주세요')
if st.button('인사말생성'):
  st.write(name+'님! 안녕하세요!')
