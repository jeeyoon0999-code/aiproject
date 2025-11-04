import streamlit as st
st.title('내 첫번째 웹앱')
name=st.text_input('이름을 입력해주세요')
st.selectbox('좋아하는 음식을 선택해주세요',['두부김치','김치찌개','김치찜'])
if st.button('인사말생성'):
  st.write(name+'님! 안녕하세요!')
