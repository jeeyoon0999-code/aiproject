import streamlit as st
import folium
from folium import IFrame
from streamlit.components.v1 import html

# --- 페이지 설정 ---
st.set_page_config(page_title="서울 관광지도", page_icon="🗺️", layout="wide")

st.title("🗺️ 외국인이 좋아하는 서울 관광지 TOP 10")
st.write("서울의 대표 명소들을 한눈에 살펴보고, 각 장소의 매력과 교통 접근성도 함께 알아봐요!")

# --- 관광지 데이터 ---
places = [
    {
        "name": "경복궁 (Gyeongbokgung Palace)",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선의 대표 궁궐로, 외국인들에게 한국 전통 건축과 왕실 문화를 체험할 수 있는 명소예요 🇰🇷",
        "station": "경복궁역 (3호선)"
    },
    {
        "name": "명동 (Myeongdong)",
        "lat": 37.563757,
        "lon": 126.982688,
        "desc": "쇼핑, 화장품, 길거리 음식으로 유명한 서울의 중심가예요. 젊은 관광객에게 특히 인기 많아요 🛍️",
        "station": "명동역 (4호선)"
    },
    {
        "name": "남산타워 (N Seoul Tower)",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 전경을 한눈에 볼 수 있는 전망 명소로, '사랑의 자물쇠'로도 유명해요 🌃",
        "station": "명동역 (4호선)"
    },
    {
        "name": "인사동 (Insadong)",
        "lat": 37.574009,
        "lon": 126.984820,
        "desc": "한국의 전통 찻집, 공예품, 갤러리들이 모여 있어 외국인들이 한국 감성을 느끼기에 좋은 거리예요 🏮",
        "station": "안국역 (3호선)"
    },
    {
        "name": "홍대 (Hongdae)",
        "lat": 37.556327,
        "lon": 126.922651,
        "desc": "젊음과 자유로운 분위기가 가득한 거리로, 버스킹과 예술문화의 중심지예요 🎨",
        "station": "홍대입구역 (2호선)"
    },
    {
        "name": "북촌한옥마을 (Bukchon Hanok Village)",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥이 모여 있는 마을로, 외국인 관광객에게 인기 있는 사진 명소예요 🏠",
        "station":

