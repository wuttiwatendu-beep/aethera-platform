import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import numpy as np

# --- 1. SETTINGS & STYLES ---
st.set_page_config(page_title="AETHERA COMMAND PLATFORM", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .main { background-color: #f1f5f9; }
    
    /* Header Styles */
    .title-area { padding: 20px 0px; }
    .platform-label { font-size: 1.2rem; font-weight: 600; color: #64748b; letter-spacing: 1px; }
    .project-main-title { font-size: 2.5rem; font-weight: 800; color: #1e3a8a; margin: 5px 0; line-height: 1.1; }
    .location-sub { font-size: 1.4rem; font-weight: 500; color: #475569; }

    /* ✅ Professional ESG Cards */
    .st-emotion-cache-12w0qpk { gap: 1rem; } /* Streamlit column gap */
    .esg-card {
        background: white;
        padding: 30px 20px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        text-align: center;
        transition: transform 0.2s;
    }
    .esg-card:hover { transform: translateY(-5px); }
    .esg-value { font-size: 2.8rem; font-weight: 800; color: #0f172a; margin: 15px 0 5px 0; }
    .esg-unit { font-size: 1.1rem; color: #64748b; font-weight: 600; }

    /* Weather Box */
    .weather-card {
        background: white;
        border-radius: 16px;
        padding: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA PROCESSING ---
def get_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=14.97&longitude=102.10&current=temperature_2m,relative_humidity_2m"
        data = requests.get(url).json()['current']
        return data
    except: return {"temperature_2m": 33.3, "relative_humidity_2m": 40}

weather = get_weather()

# --- 3. HEADER SECTION ---
header_l, header_m, header_r = st.columns([1, 4, 2])

with header_l:
    st.image("rmut.png", width=160)

with header_m:
    st.markdown("""
        <div class="title-area">
            <div class="platform-label">AETHERA COMMAND PLATFORM</div>
            <div class="project-main-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</div>
            <div class="location-sub">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</div>
        </div>
    """, unsafe_allow_html=True)

with header_r:
    st.image("NetZero platform 1.png", width=260)
    st.markdown(f"""
        <div class="weather-card">
            <div style="color: #64748b; font-size: 0.9rem; font-weight: 600;">📍 Nakhon Ratchasima Weather</div>
            <div style="font-size: 2rem; font-weight: 800; color: #2563eb;">{weather['temperature_2m']}°C</div>
            <div style="color: #94a3b8; font-size: 0.85rem;">Humidity: {weather['relative_humidity_2m']}% | Wind: 5.6 km/h</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# --- 4. ESG METRICS (Professional Alignment) ---
# สร้าง Grid ที่สมดุล
label_col, c1, c2, c3 = st.columns([1, 2, 2, 2])

with label_col:
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    st.button("ESG Metrics", use_container_width=True, type="primary")

# ฟังก์ชันแสดงผล Card เพื่อความเป๊ะของตำแหน่ง
def esg_block(col, img_file, value, label):
    with col:
        st.markdown(f"""<div class='esg-card'>""", unsafe_allow_html=True)
        st.image(img_file, width=130) # ขนาดใหญ่ชัดเจนกึ่งกลาง
        st.markdown(f"""
            <div class='esg-value'>{value}</div>
            <div class='esg-unit'>{label}</div>
        </div>""", unsafe_allow_html=True)

esg_block(c1, "CO2.png", "27.24 T", "CO2 Saved")
esg_block(c2, "Coal.png", "21.79 T", "Coal Saved")
esg_block(c3, "Tree.png", "680", "Trees Planted")

# --- 5. PERFORMANCE METRICS GRID ---
st.write("")
st.subheader("📊 3: Performance Metrics")
m_cols = st.columns(6)
m_data = [
    ("Real-Time (kW)", "2,854.56"), ("Total Yield (MW)", "54.47"),
    ("Peak Capacity (kW)", "2,854.56"), ("Daily Yield (MW)", "28.80"),
    ("Solar Capacity (kW)", "10"), ("P2P Volume Today", "80.3")
]
for i, (label, val) in enumerate(m_data):
    with m_cols[i]:
        st.markdown(f"""
            <div style="background: white; padding: 15px; border-radius: 12px; border-left: 5px solid #2563eb; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <div style="color: #64748b; font-size: 0.85rem; font-weight: 600;">{label}</div>
                <div style="font-size: 1.4rem; font-weight: 800; color: #1e293b;">{val}</div>
            </div>
        """, unsafe_allow_html=True)

# --- 6. CHARTS & STATION DETAILS (RELOADED) ---
st.write("")
st.divider()
chart_col, table_col = st.columns([1.7, 1])

with chart_col:
    # กราฟที่ 1: การผลิตไฟ
    st.markdown("### ⚡ 24-Hour Solar Production (kW)")
    x_hours = [f"{i:02d}:00" for i in range(24)]
    y_vals = [5,5,10,60,200,800,1800,2500,2854,2700,2100,1200,500,100,20,5,5,5,5,5,5,5,5,5]
    fig_main = go.Figure(go.Scatter(x=x_hours, y=y_vals, fill='tozeroy', line_color='#f59e0b', fillcolor='rgba(245, 158, 11, 0.2)'))
    fig_main.update_layout(margin=dict(l=0, r=0, t=20, b=0), height=300, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_main, use_container_width=True)

    # กราฟที่ 2: Power Mix
    st.markdown("### 📊 Today Power Mix (kW)")
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 2, 24), name="Grid Load", fill='tozeroy', line_color='#ef4444'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(25, 2, 24), name="Solar Generation", fill='to
