import streamlit as st
import folium
from folium import IFrame
from streamlit.components.v1 import html

# --- 페이지 설정 ---
st.set_page_config(page_title="서울 관광지도", page_icon="🗺️", layout="wide")

st.title("🗺️ 외국인이 사랑하는 서울 관광지 TOP 10")
st.write("서울을 방문한 외국인들이 가장 많이 찾는 명소들을 지도 위에서 살펴보고, 각각의 매력을 알아봐요! 😄")

# --- 관광지 데이터 ---
places = [
    {
        "name": "경복궁 (Gyeongbokgung Palace)",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선의 대표 궁궐로, 웅장한 건축미와 수문장 교대식이 인상적인 곳이에요.",
        "reason": "한국 전통 문화를 대표하는 장소로 외국인에게 인기가 많아요 🇰🇷",
        "station": "경복궁역 (3호선)"
    },
    {
        "name": "명동 (Myeongdong)",
        "lat": 37.563757,
        "lon": 126.982688,
        "desc": "패션, 화장품, 길거리 음식의 성지! 서울의 쇼핑 거리 중심이에요.",
        "reason": "다양한 브랜드와 맛있는 길거리 음식으로 외국인들이 꼭 들르는 곳이에요 🛍️",
        "station": "명동역 (4호선)"
    },
    {
        "name": "남산타워 (N Seoul Tower)",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울의 중심에 있는 전망 명소로, 사랑의 자물쇠 명소로도 유명해요.",
        "reason": "서울의 야경을 한눈에 볼 수 있어서 커플 여행객에게 인기가 많아요 🌃",
        "station": "명동역 (4호선)"
    },
    {
        "name": "인사동 (Insadong)",
        "lat": 37.574009,
        "lon": 126.984820,
        "desc": "전통 찻집, 도자기 가게, 한지 공예품 등 한국 감성이 가득한 거리예요.",
        "reason": "한국 전통문화 체험을 원하는 외국인들에게 인기가 많아요 🏮",
        "station": "안국역 (3호선)"
    },
    {
        "name": "홍대 (Hongdae)",
        "lat": 37.556327,
        "lon": 126.922651,
        "desc": "젊음과 예술의 거리! 거리공연, 카페, 클럽이 가득해요.",
        "reason": "자유로운 분위기와 스트리트 문화가 매력적이에요 🎨",
        "station": "홍대입구역 (2호선)"
    },
    {
        "name": "북촌한옥마을 (Bukchon Hanok Village)",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥이 모여 있는 아름다운 마을이에요.",
        "reason": "전통과 현대가 조화된 사진 명소로 사랑받고 있어요 🏠",
        "station": "안국역 (3호선)"
    },
    {
        "name": "청계천 (Cheonggyecheon Stream)",
        "lat": 37.569722,
        "lon": 126.977222,
        "desc": "도심 속 시원한 물길, 산책과 야경 감상하기 좋은 곳이에요.",
        "reason": "서울 도심 한복판에서 여유를 느낄 수 있어요 🌊",
        "station": "광화문역 (5호선)"
    },
    {
        "name": "롯데월드 (Lotte World)",
        "lat": 37.511000,
        "lon": 127.098000,
        "desc": "실내외 놀이공원으로 가족 단위 관광객에게 인기가 많아요.",
        "reason": "날씨에 상관없이 즐길 수 있는 최고의 테마파크 🎢",
        "station": "잠실역 (2호선)"
    },
    {
        "name": "잠실 롯데타워 (Lotte Tower)",
        "lat": 37.513068,
        "lon": 127.102574,
        "desc": "대한민국에서 가장 높은 빌딩! 전망대와 쇼핑몰이 인상적이에요.",
        "reason": "서울의 하늘을 가장 높이에서 바라볼 수 있는 곳이에요 🏙️",
        "station": "잠실역 (2호선)"
    },
    {
        "name": "이태원 (Itaewon)",
        "lat": 37.534713,
        "lon": 126.994675,
        "desc": "다양한 나라의 음식과 문화가 공존하는 거리예요.",
        "reason": "다문화 분위기로 외국인들이 가장 편하게 느끼는 지역이에요 🍴",
        "station": "이태원역 (6호선)"
    },
]

# --- 지도 생성 ---
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles="CartoDB positron")

# 마커 색상 다양하게
colors = ["red", "blue", "green", "purple", "orange", "darkred", "cadetblue", "darkgreen", "lightgray", "pink"]

# --- 마커 표시 ---
for i, p in enumerate(places):
    iframe = IFrame(f"""
        <h4>{p['name']}</h4>
        <p>{p['desc']}</p>
        <p><b>✨ 인기 이유:</b> {p['reason']}</p>
        <p><b>🚇 가까운 역:</b> {p['station']}</p>
    """, width=260, height=160)
    popup = folium.Popup(iframe, max_width=250)
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=popup,
        tooltip=p["name"],
        icon=folium.Icon(color=colors[i % len(colors)], icon="star", prefix="fa")
    ).add_to(m)

# 지도 표시
html(m._repr_html_(), height=600)

# --- 관광지 설명 섹션 ---
st.markdown("---")
st.subheader("📖 관광지 상세 설명")

for i, p in enumerate(places, 1):
    st.markdown(f"### {i}. {p['name']}")
    st.write(f"**📝 설명:** {p['desc']}")
    st.write(f"**✨ 인기 이유:** {p['reason']}")
    st.write(f"**🚇 가까운 지하철역:** {p['station']}")
    st.markdown("---")

st.caption("📍 데이터 출처: Visit Seoul, TripAdvisor, Google Travel (2024년 기준)")

