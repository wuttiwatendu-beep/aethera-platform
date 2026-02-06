import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import numpy as np

# --- 1. CORE CONFIG & CLEAN STYLE ---
st.set_page_config(page_title="AETHERA COMMAND PLATFORM", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8fafc; }

    /* Header Styling */
    .main-title { font-size: 2.2rem !important; font-weight: 800; color: #1e3a8a; line-height: 1.2; }
    .sub-title { font-size: 1.1rem; font-weight: 600; color: #b43d8b; }

    /* ✅ ลบสี่เหลี่ยมว่างออก และจัดกลุ่มไอคอน+ตัวเลขให้สวยงาม */
    .esg-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 10px;
    }
    .esg-value { font-size: 3rem !important; font-weight: 800; color: #0f172a; margin-top: 15px; line-height: 1; }
    .esg-label { font-size: 1.1rem; color: #64748b; font-weight: 600; margin-top: 5px; }

    /* Metric Box for Row 3 */
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. WEATHER API ---
def get_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=14.97&longitude=102.10&current=temperature_2m,relative_humidity_2m"
        return requests.get(url, timeout=5).json()['current']
    except: return {"temperature_2m": 33.3, "relative_humidity_2m": 40}

w = get_weather()

# --- 3. HEADER SECTION ---
h_left, h_mid, h_right = st.columns([1, 4, 2])

with h_left:
    st.image("rmut.png", width=150)

with h_mid:
    st.markdown('<p class="sub-title">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#475569; font-weight:500;">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

with h_right:
    st.image("NetZero platform 1.png", width=260)
    st.markdown(f"""
        <div style="background: linear-gradient(90deg, #2563eb, #1d4ed8); color: white; padding: 15px; border-radius: 15px; margin-top: 10px;">
            <small>📍 NAKHON RATCHASIMA</small><br>
            <b style="font-size: 1.8rem;">{w['temperature_2m']}°C</b><br>
            <small>Humidity: {w['relative_humidity_2m']}% | Wind: 5.6 km/h</small>
        </div>
    """, unsafe_allow_html=True)

# --- 4. ESG METRICS (Clean & Large) ---
st.write("")
st.write("")
# จัดวาง 4 คอลัมน์ (ปุ่ม + 3 ไอคอน)
b_col, c1, c2, c3 = st.columns([1.2, 2, 2, 2])

with b_col:
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    st.button("ESG Metrics", use_container_width=True, type="primary")

# ฟังก์ชันแสดงผลแบบ Professional ไม่มีกล่องว่างกวนใจ
def display_esg(col, img, val, label):
    with col:
        st.markdown('<div class="esg-container">', unsafe_allow_html=True)
        st.image(img, width=140) # ขยายรูปไอคอนให้ใหญ่เด่น
        st.markdown(f'<div class="esg-value">{val}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="esg-label">{label}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

display_esg(c1, "CO2.png", "27.24 T", "CO2 Saved")
display_esg(c2, "Coal.png", "21.79 T", "Coal Saved")
display_esg(c3, "Tree.png", "680", "Trees Planted")

# --- 5. PERFORMANCE METRICS ---
st.write("")
st.markdown("### 📊 3: Performance Metrics")
m_cols = st.columns(6)
m_labels = [("Real-Time (kW)", "2,854.56"), ("Total Yield (MW)", "54.47"), ("Peak Capacity (kW)", "2,854.56"), ("Daily Yield (MW)", "28.80"), ("Solar Capacity (kW)", "10"), ("P2P Volume Today", "80.3")]

for i, (lab, val) in enumerate(m_labels):
    with m_cols[i]:
        st.markdown(f'<div class="metric-card"><small style="color:#64748b; font-weight:600;">{lab}</small><br><b style="font-size:1.4rem; color:#1e293b;">{val}</b></div>', unsafe_allow_html=True)

# --- 6. ANALYTICS & DETAILS (Restored) ---
st.write("")
st.divider()
left, right = st.columns([1.8, 1])

with left:
    st.markdown("### ⚡ 24-Hour Solar Production (kW)")
    # กราฟหลัก
    fig1 = go.Figure(go.Scatter(x=list(range(24)), y=np.random.normal(1800, 300, 24), fill='tozeroy', line_color='#f59e0b', fillcolor='rgba(245, 158, 11, 0.1)'))
    fig1.update_layout(height=280, margin=dict(l=0,r=0,t=10,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("### 📊 Today Power Mix (kW)")
    # กราฟ Power Mix
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(y=np.random.normal(45, 2, 24), name="Load", fill='tozeroy', line_color='#ef4444', fillcolor='rgba(239, 68, 68, 0.1)'))
    fig2.add_trace(go.Scatter(y=np.random.normal(25, 2, 24), name="Solar", fill='tozeroy', line_color='#3b82f6', fillcolor='rgba(59, 130, 246, 0.1)'))
    fig2.update_layout(height=280, margin=dict(l=0,r=0,t=10,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)

with right:
    # ตารางสถานี 8 แห่ง
    st.markdown("### ✅ Station Details")
    df = pd.DataFrame({
        "อาคาร (Station)": ["สนง.วิชาการฯ (35)", "บริหารธุรกิจ (32)", "อาคาร A (สำรอง)", "อาคาร B (สำรอง)", "เครื่องกล (G)", "เรียนรวม 7", "วิทยบริการฯ (4)", "หอประชุม (2)"],
        "kW": [485.76, 400.00, 380.00, 365.00, 354.56, 314.24, 280.00, 250.00]
    })
    st.table(df)
