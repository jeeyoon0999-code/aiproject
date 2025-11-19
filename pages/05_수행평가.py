import streamlit as st

st.set_page_config(page_title="오늘 뭐 먹지? 🍽️", page_icon="🍴")

st.title("🍴 오늘 뭐 먹지? 메뉴 추천기")
st.write("카테고리를 고르면 두 가지 맛있는 메뉴를 골라줄게! 😎✨")

# 카테고리별 음식 데이터
foods = {
    "한식": {
        "추천": ["불고기", "비빔밥"],
        "인기": "김치찌개"
    },
    "양식": {
        "추천": ["파스타", "스테이크"],
        "인기": "피자"
    },
    "분식": {
        "추천": ["떡볶이", "김밥"],
        "인기": "떡볶이"
    },
    "중식": {
        "추천": ["짜장면", "마라탕"],
        "인기": "짬뽕"
    },
    "디저트": {
        "추천": ["마카롱", "티라미수"],
        "인기": "아이스크림"
    }
}

category = st.selectbox("🍽️ 어떤 종류로 먹을래?", list(foods.keys()))

if category:
    st.subheader(f"✨ {category} 추천 메뉴!")
    st.write(f"👉 **{foods[category]['추천'][0]}**")
    st.write(f"👉 **{foods[category]['추천'][1]}**")

    st.subheader("🔥 제일 인기 많은 메뉴는?")
    st.write(f"⭐ **{foods[category]['인기']}** 가 제일 인기 많아! 😋")
