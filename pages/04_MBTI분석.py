# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import io

st.set_page_config(page_title="Countries MBTI Explorer", layout="wide")

# ---------- 헬퍼함수: 색상 생성 ----------
def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def interp_color(c1, c2, t):
    r = round(c1[0] + (c2[0] - c1[0]) * t)
    g = round(c1[1] + (c2[1] - c1[1]) * t)
    b = round(c1[2] + (c2[2] - c1[2]) * t)
    return (r, g, b)

def make_blue_gradient(n, light_hex="#dff2ff", dark_hex="#0b61d6"):
    if n <= 0:
        return []
    light = hex_to_rgb(light_hex)
    dark = hex_to_rgb(dark_hex)
    colors = []
    for i in range(n):
        t = i / max(n - 1, 1)  # 0..1
        rgb = interp_color(light, dark, t)
        colors.append(rgb_to_hex(rgb))
    return colors

# ---------- 데이터 로드 ----------
@st.cache_data
def load_data(csv_path="countriesMBTI_16types.csv"):
    df = pd.read_csv(csv_path)
    # 기대: Country 열 + 16 MBTI 컬럼
    df_columns = [c for c in df.columns if c != "Country"]
    return df, df_columns

try:
    df, mbti_cols = load_data()
except FileNotFoundError:
    st.error("`countriesMBTI_16types.csv` 파일을 찾을 수 없습니다. 파일을 앱 디렉토리에 업로드했는지 확인하세요.")
    st.stop()

# ---------- 레이아웃 ----------
st.title("🌍 Countries MBTI Explorer")
st.markdown(
    "국가별 MBTI 분포를 인터랙티브한 Plotly 막대그래프로 확인할 수 있어요. "
    "국가를 선택하면 해당 국가의 16개 MBTI 유형 비율을 보여줍니다."
)

# 사이드바
with st.sidebar:
    st.header("설정")
    country_list = df["Country"].tolist()
    default_country = country_list[0] if len(country_list) > 0 else None
    selected_country = st.selectbox("국가 선택", country_list, index=0 if default_country else None)
    st.write("---")
    st.markdown("💾 CSV 파일 미리보기")
    if st.checkbox("데이터 상위 5행 보기", value=False):
        st.dataframe(df.head(5))

# ---------- 선택 국가 데이터 ----------
row = df[df["Country"] == selected_country]
if row.empty:
    st.warning("선택한 국가의 데이터가 없습니다.")
    st.stop()

# MBTI 값 추출 (원래 순서 유지)
values = [float(row.iloc[0][c]) for c in mbti_cols]
pairs = list(zip(mbti_cols, values))

# 정렬하지 않고 원래 컬럼 순서로 표시 (원하면 정렬 가능)
# 하지만 1등 색을 정하려면 최고값 인덱스 찾기
max_idx = max(range(len(values)), key=lambda i: values[i])

# 색상 생성: 1등은 빨간색, 나머지는 파란 그라데이션
red_hex = "#E10600"  # 1등 색
blue_grad = make_blue_gradient(len(values)-1, light_hex="#dff2ff", dark_hex="#0b61d6")

# build colors list in same order as mbti_cols
colors = []
grad_i = 0
for i in range(len(values)):
    if i == max_idx:
        colors.append(red_hex)
    else:
        colors.append(blue_grad[grad_i])
        grad_i += 1

# ---------- Plotly 그래프 생성 ----------
fig = go.Figure(
    data=[
        go.Bar(
            x=mbti_cols,
            y=values,
            marker=dict(color=colors),
            text=[f"{v:.3f}" for v in values],
            textposition="outside",
            hovertemplate="%{x}<br>비율: %{y:.3f}<extra></extra>",
        )
    ]
)

fig.update_layout(
    title=f"{selected_country} — MBTI 비율",
    yaxis_title="비율 (0~1)",
    xaxis_title="MBTI 유형",
    yaxis=dict(range=[0, max(values)*1.18 + 0.01]),
    template="plotly_white",
    uniformtext_minsize=10,
    uniformtext_mode='hide',
    margin=dict(t=70, b=40, l=40, r=20),
    height=520
)

col1, col2 = st.columns([3,1])
with col1:
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.markdown("### 📌 요약")
    st.write(f"선택 국가: **{selected_country}**")
    top_type = mbti_cols[max_idx]
    top_value = values[max_idx]
    st.write(f"가장 높은 MBTI: **{top_type}** ({top_value:.3f})")
    st.markdown("---")
    st.write("원하는 다른 국가를 선택하면 즉시 그래프가 갱신됩니다.")

# ---------- 코드 보여주기 + 다운로드 ----------
st.markdown("---")
st.subheader("앱 코드 (복사 또는 다운로드)")
with open(__file__, "r", encoding="utf-8") as f:
    code_text = f.read()

st.code(code_text, language="python")

st.download_button(
    label="📥 코드 다운로드 (.py)",
    data=code_text,
    file_name="streamlit_app.py",
    mime="text/x-python"
)

st.caption("Tip: Streamlit Cloud에 배포하려면 이 파일과 CSV, requirements.txt를 동일한 리포지토리에 올리면 됩니다.")
