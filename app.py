import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="AETHERA COMMAND PLATFORM", layout="wide")

st.markdown("""
    <style>
    /* พื้นหลังโทนสว่าง */
    .main { background-color: #f8fafc; }
    
    .platform-header { font-size: 1.8rem; font-weight: 700; color: #1e3a8a; margin-bottom: 0px; }
    .project-title { font-size: 2.2rem; font-weight: 800; color: #b43d8b; line-height: 1.2; }
    .location-title { font-size: 1.4rem; font-weight: 600; color: #1e40af; }
    
    /* กล่องสภาพอากาศสไตล์ใหม่ */
    .weather-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }

    /* ✅ ปรับไอคอน ESG ให้ใหญ่ขึ้น 2 เท่า และตัวเลขให้เด่น */
    .esg-card {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        background: #ffffff;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
    }
    .esg-value { font-size: 2.5rem !important; font-weight: 800; color: #1e293b; margin-top: 10px; }
    .esg-label { font-size: 1.1rem; color: #64748b; font-weight: 500; }
    </style>
    """, unsafe_allow_html=True)

# 2. Weather Data
def get_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=14.97&longitude=102.10&current=temperature_2m,relative_humidity_2m"
        return requests.get(url).json()['current']
    except: return {"temperature_2m": 33.3, "relative_humidity_2m": 40}

w = get_weather()

# 3. Header Section
h1, h2, h3 = st.columns([1, 4, 1.8])

with h1:
    st.image("rmut.png", width=140)

with h2:
    st.markdown('<p class="platform-header">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="project-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p class="location-title">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

with h3:
    st.image("NetZero platform 1.png", width=240)
    st.markdown(f"""
    <div class="weather-box">
        <small style='color: #64748b;'>📍 Nakhon Ratchasima Weather</small><br>
        <b style='font-size: 1.8rem; color: #0f172a;'>{w['temperature_2m']}°C</b><br>
        <small style='color: #94a3b8;'>Humidity: {w['relative_humidity_2m']}% | Wind: 5.6 km/h</small>
    </div>
    """, unsafe_allow_html=True)

# 4. ESG Metrics: Large Icons & Centered Numbers
st.write("")
btn_col, c1, c2, c3 = st.columns([1, 1.5, 1.5, 1.5])

with btn_col:
    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
    st.button("ESG Metrics", use_container_width=True)

with c1:
    st.markdown("<div class='esg-card'>", unsafe_allow_html=True)
    st.image("CO2.png", width=120) # ขยายใหญ่ขึ้น 2 เท่า
    st.markdown("<div class='esg-value'>27.24 T</div>", unsafe_allow_html=True)
    st.markdown("<div class='esg-label'>CO2 Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='esg-card'>", unsafe_allow_html=True)
    st.image("Coal.png", width=120) # ขยายใหญ่ขึ้น 2 เท่า
    st.markdown("<div class='esg-value'>21.79 T</div>", unsafe_allow_html=True)
    st.markdown("<div class='esg-label'>Coal Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='esg-card'>", unsafe_allow_html=True)
    st.image("Tree.png", width=120) # ขยายใหญ่ขึ้น 2 เท่า
    st.markdown("<div class='esg-value'>680</div>", unsafe_allow_html=True)
    st.markdown("<div class='esg-label'>Trees Planted</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Performance Metrics
st.markdown("### 3: Performance Metrics")
m = st.columns(6)
metrics_data = [
    ("Real-Time (kW)", "2,854.56"), ("Total Yield (MW)", "54.47"),
    ("Peak Capacity (kW)", "2,854.56"), ("Daily Yield (MW)", "28.80"),
    ("Solar Capacity (kW)", "10"), ("P2P Volume Today", "80.3")
]
for i, (label, val) in enumerate(metrics_data):
    m[i].metric(label, val)

# 6. Graphs & Station Details (Full Data Restored)
st.divider()
col_left, col_right = st.columns([1.6, 1])

with col_left:
    st.subheader("⚡ 24-Hour Solar Production (kW)")
    fig1 = go.Figure(go.Scatter(x=list(range(24)), y=np.random.normal(1500, 500, 24), fill='tozeroy', line_color='#f59e0b'))
    st.plotly_chart(fig1, use_container_width=True)
    
    st.subheader("📊 Today Power Mix (kW)")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(y=np.random.normal(40, 5, 24), name="Load", fill='tozeroy', line_color='#ef4444'))
    fig2.add_trace(go.Scatter(y=np.random.normal(20, 3, 24), name="Solar", fill='tozeroy', line_color='#3b82f6'))
    st.plotly_chart(fig2, use_container_width=True)

with col_right:
    st.subheader("✅ Station Details")
    df = pd.DataFrame({
        "อาคาร (Station)": ["สนง.วิชาการฯ (35)", "บริหารธุรกิจ (32)", "อาคาร A (สำรอง)", "อาคาร B (สำรอง)", "เครื่องกล (G)", "เรียนรวม 7", "วิทยบริการฯ (4)", "หอประชุม (2)"],
        "kW": [485.76, 400.00, 380.00, 365.00, 354.56, 314.24, 280.00, 250.00]
    })
    st.table(df)
