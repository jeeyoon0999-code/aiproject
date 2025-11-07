import streamlit as st
import folium
from streamlit.components.v1 import html

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="서울 관광지도", page_icon="🗺️", layout="wide")

st.title("🗺️ 외국인이 좋아하는 서울 관광지 TOP 10")
st.write("서울의 인기 관광 명소를 지도 위에서 한눈에 살펴봐요!")

# --- 관광지 데이터 ---
places = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579617, "lon": 126.977041, "desc": "조선의 대표 궁궐 🇰🇷"},
    {"name": "명동 (Myeongdong)", "lat": 37.563757, "lon": 126.982688, "desc": "쇼핑 천국 🛍️"},
    {"name": "남산타워 (N Seoul Tower)", "lat": 37.551169, "lon": 126.988227, "desc": "서울의 야경 명소 🌃"},
    {"name": "인사동 (Insadong)", "lat": 37.574009, "lon": 126.984820, "desc": "전통과 현대의 만남 🏮"},
    {"name": "홍대 (Hongdae)", "lat": 37.556327, "lon": 126.922651, "desc": "젊음과 예술의 거리 🎨"},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983998, "desc": "한옥이 모여 있는 아름다운 마을 🏠"},
    {"name": "청계천 (Cheonggyecheon Stream)", "lat": 37.569722, "lon": 126.977222, "desc": "도심 속 힐링 산책로 🌊"},
    {"name": "롯데월드 (Lotte World)", "lat": 37.511000, "lon": 127.098000, "desc": "도심 속 놀이공원 🎢"},
    {"name": "잠실 롯데타워 (Lotte Tower)", "lat": 37.513068, "lon": 127.102574, "desc": "한국에서 가장 높은 빌딩 🏙️"},
    {"name": "이태원 (Itaewon)", "lat": 37.534713, "lon": 126.994675, "desc": "다양한 문화와 음식의 거리 🍴"},
]

# --- 지도 생성 ---
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

for p in places:
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=f"<b>{p['name']}</b><br>{p['desc']}",
        tooltip=p["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# --- 지도 표시 ---
folium_html = m._repr_html_()
html(folium_html, height=600)

st.markdown("---")
st.write("📍 서울의 명소를 클릭해보세요!")
st.caption("데이터 출처: Visit Seoul, TripAdvisor 등 (2024년 기준)")
