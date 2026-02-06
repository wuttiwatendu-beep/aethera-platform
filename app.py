import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import numpy as np
import os

# 1. Page Configuration
st.set_page_config(page_title="AETHERA COMMAND PLATFORM", layout="wide")

st.markdown("""
    <style>
    .platform-header {
        font-size: 1.8rem !important;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 35px !important; /* ช่องไฟตามที่คุณนุสั่ง */
        letter-spacing: 2px;
    }
    .project-title { font-size: 2.2rem !important; font-weight: 800; color: #b43d8b; line-height: 1.2; }
    .location-title { font-size: 1.5rem !important; font-weight: 600; color: #1e40af; }
    
    /* Grid Card สำหรับรูปที่คุณนุโหลดไว้ */
    .icon-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    /* หน้าต่างสภาวะอากาศ (Weather Box) */
    .weather-card {
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        color: white;
        border-radius: 12px;
        padding: 12px;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Function: Get Korat Weather Data
def get_korat_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=14.97&longitude=102.10&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        res = requests.get(url).json()
        return res['current']
    except: return None

w = get_korat_weather()

# 3. Header Section: Logo | Titles | Weather & NetZero
h1, h2, h3 = st.columns([1, 4, 1.5])

with h1:
    st.image("rmut.png", width=150)

with h2:
    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
    st.markdown('<p class="platform-header">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="project-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p class="location-title">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

with h3:
    # แสดงรูป NetZero Platform 1
    if os.path.exists("NetZero_Platform_1.png"):
        st.image("NetZero_Platform_1.png", width=180)
    else:
        st.markdown("<p style='text-align:right; font-weight:bold;'>NetZero_Platform 1</p>", unsafe_allow_html=True)
    
    # แสดงหน้าต่างสภาวะอากาศ จ.นครราชสีมา
    if w:
        st.markdown(f"""
        <div class="weather-card">
            <small>📍 Nakhon Ratchasima</small><br>
            <b style='font-size:1.5rem;'>{w['temperature_2m']}°C</b><br>
            <small>Humidity: {w['relative_humidity_2m']}% | Wind: {w['wind_speed_10m']} km/h</small>
        </div>
        """, unsafe_allow_html=True)

# 4. Row 1: ESG Cards using your uploaded images
st.write("")
e1, e2, e3, e4, e5 = st.columns(5)
with e1:
    st.markdown("<div class='icon-card'><b>ESG Metrics</b></div>", unsafe_allow_html=True)
with e2:
    st.image("CO2.png", width=60) # ใช้รูปที่คุณนุโหลดไว้
    st.markdown("<div style='text-align:center;'><b>27.24 T</b><br><small>CO2 Saved</small></div>", unsafe_allow_html=True)
with e3:
    st.image("Coal.png", width=60) # ใช้รูปที่คุณนุโหลดไว้
    st.markdown("<div style='text-align:center;'><b>21.79 T</b><br><small>Coal Saved</small></div>", unsafe_allow_html=True)
with e4:
    st.image("Tree.png", width=60) # ใช้รูปที่คุณนุโหลดไว้
    st.markdown("<div style='text-align:center;'><b>680</b><br><small>Trees Planted</small></div>", unsafe_allow_html=True)
with e5:
    st.image("Tree.png", width=60)
    st.markdown("<div style='text-align:center;'><b>680</b><br><small>Trees Planted</small></div>", unsafe_allow_html=True)

# 5. Row 2: Stats Grid
st.write("")
m1, m2, m3, m4, m5, m6 = st.columns(6)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("Total Yield (MW)", "28.80")
m5.metric("Peak Capacity (kW)", "10")
m6.metric("P2P Volume Today", "80.3")

# 6. Row 3: Charts (Fixed NameError)
st.write("")
c_l, c_r = st.columns(2)

with c_l:
    st.subheader("⚡ 24-Hour Details 00 (kW)")
    hours = [f"{i:02d}:00" for i in range(24)]
    # กราฟสีส้มทองตามรูป
    gen_val = [5,5,5,10,60,250,900,1600,2400,2800,2854,2700,2100,1300,500,100,20,5,5,5,5,5,5,5]
    fig_solar = go.Figure(go.Scatter(x=hours, y=gen_val, fill='tozeroy', line_color='#f59e0b'))
    st.plotly_chart(fig_solar, use_container_width=True)

with c_r:
    st.subheader("📊 Today Power Mix (kW)")
    # แก้ไข Error: ตรวจสอบการสร้าง fig_mix ใหม่ทั้งหมด
    fig_mix_new = go.Figure()
    fig_mix_new.add_trace(go.Scatter(y=np.random.normal(45, 4, 24), name="Load", fill='tozeroy', line_color='#ef4444'))
    fig_mix_new.add_trace(go.Scatter(y=np.random.normal(22, 2, 24), name="Solar", fill='tozeroy', line_color='#3b82f6'))
    st.plotly_chart(fig_mix_new, use_container_width=True)

# 7. Row 4: Station Details
st.subheader("📋 Station Details (Corrected)")
df_fix = pd.DataFrame({
    "อาคาร": ["สำนักส่งเสริมวิชาการฯ (35)", "คณะบริหารธุรกิจ (32)", "อาคาร A (สำรอง)", "อาคาร B (สำรอง)", "G กลุ่มวิชาชีพเครื่องกล", "อาคารเรียนรวม 7", "สำนักวิทยบริการฯ (4)", "หอประชุมวชิราลงกรณ (2)"],
    "kW": [485.76, 400.00, 380.00, 365.00, 354.56, 314.24, 280.00, 250.00],
    "Zone": ["ศูนย์กลาง"] * 4 + ["หนองระเวียง"] + ["ศูนย์กลาง"] * 3
})
st.table(df_fix)
