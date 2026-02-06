import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
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
    .project-title { font-size: 2.4rem !important; font-weight: 800; color: #b43d8b; line-height: 1.2; }
    .location-title { font-size: 1.6rem !important; font-weight: 600; color: #1e40af; }
    
    /* สไตล์ Card สำหรับ ESG และ Weather */
    .grid-card {
        background-color: #f8fafc;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        border: 1px solid #e2e8f0;
        height: 100%;
    }
    .weather-box {
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        color: white;
        border-radius: 12px;
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Function: Get Korat Weather Data (API)
def get_weather():
    try:
        # ใช้ API จาก Open-Meteo (ฟรี ไม่ต้องใช้ Key) สำหรับพิกัดโคราช
        url = "https://api.open-meteo.com/v1/forecast?latitude=14.97&longitude=102.10&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
        res = requests.get(url).json()
        return res['current']
    except:
        return None

weather = get_weather()

# 3. Header: Logo | Project Titles | NetZero Logo
h_col1, h_col2, h_col3 = st.columns([1, 4, 1.2])

with h_col1:
    st.image("rmut.png", width=160)

with h_col2:
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    st.markdown('<p class="platform-header">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="project-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p class="location-title">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

with h_col3:
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    # ใส่ชื่อ NetZero Platform 1 ตามที่คุณนุส่งมา
    st.markdown("<p style='text-align:right; font-weight:bold; font-size:1.1rem;'>NetZero_Platform 1</p>", unsafe_allow_html=True)
    
    # เพิ่มหน้าต่างสภาพอากาศ จ.นครราชสีมา
    if weather:
        st.markdown(f"""
        <div class="weather-box">
            <small>📍 Nakhon Ratchasima</small><br>
            <b style='font-size:1.4rem;'>{weather['temperature_2m']}°C</b><br>
            <small>Humidity: {weather['relative_humidity_2m']}% | Wind: {weather['wind_speed_10m']} km/h</small>
        </div>
        """, unsafe_allow_html=True)

# 4. Row 1: ESG Cards (5 Columns)
st.write("")
ec1, ec2, ec3, ec4, ec5 = st.columns(5)
with ec1:
    st.markdown("<div class='grid-card'><img src='https://cdn-icons-png.flaticon.com/128/1690/1690916.png' width='40'><br><b>CO2</b></div>", unsafe_allow_html=True)
with ec2:
    st.markdown("<div class='grid-card'>☁️<br><b>27.24 T</b><br><small>CO2 Saved</small></div>", unsafe_allow_html=True)
with ec3:
    st.markdown("<div class='grid-card'>⛰️<br><b>21.79 T</b><br><small>Coal Saved</small></div>", unsafe_allow_html=True)
with ec4:
    st.markdown("<div class='grid-card'>🌳<br><b>680</b><br><small>Trees Planted</small></div>", unsafe_allow_html=True)
with ec5:
    st.markdown("<div class='grid-card'>🌳<br><b>680</b><br><small>Trees Planted</small></div>", unsafe_allow_html=True)

# 5. Row 2: Stats Grid (6 Columns)
st.write("")
m1, m2, m3, m4, m5, m6 = st.columns(6)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("Total Yield (MW)", "28.80")
m5.metric("Peak Capacity (kW)", "10")
m6.metric("P2P Volume Today", "80.3")

# 6. Row 3: Main Charts (Production & Power Mix)
st.write("")
c_left, c_right = st.columns(2)

with c_left:
    st.subheader("⚡ 24-Hour Details 00 (kW)")
    # ใช้รูปกราฟที่คุณนุส่งมาเป็นต้นแบบ
    hours = [f"{i:02d}:00" for i in range(24)]
    gen_data = [5, 5, 5, 10, 50, 200, 800, 1500, 2300, 2800, 2854, 2700, 2200, 1400, 600, 150, 40, 5, 5, 5, 5, 5, 5, 5]
    fig = go.Figure(go.Scatter(x=hours, y=gen_data, fill='tozeroy', line_color='#f59e0b', name="Solar Production"))
    st.plotly_chart(fig, use_container_width=True)

with c_right:
    st.subheader("📊 Today Power Mix (kW)") #
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 4, 24), name="Load", fill='tozeroy', line_color='#ef4444'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(22, 2, 24), name="Solar", fill='tozeroy', line_color='#3b82f6'))
    st.plotly_chart(fig_mix, use_container_width=True)

# 7. Row 4: Station Details & Monthly
st.divider()
b_left, b_right = st.columns([1.2, 1])

with b_left:
    st.subheader("📋 Station Details (Corrected)")
    # ตารางข้อมูลครบทั้ง 10 สถานีที่คุณนุอัปโหลดไฟล์มา
    df = pd.DataFrame({
        "อาคาร": ["สำนักส่งเสริมวิชาการฯ (35)", "คณะบริหารธุรกิจ (32)", "อาคาร A (สำรอง)", "อาคาร B (สำรอง)", "G กลุ่มวิชาชีพเครื่องกล", "อาคารเรียนรวม 7", "สำนักวิทยบริการฯ (4)", "หอประชุมวชิราลงกรณ (2)", "สำนักงานอธิการบดี (1)", "Sports Complex"],
        "kW": [485.76, 400.00, 380.00, 365.00, 354.56, 314.24, 280.00, 250.00, 220.00, 200.00],
        "Zone": ["ศูนย์กลาง"] * 9 + ["หนองระเวียง"]
    })
    st.table(df)

with b_right:
    st.subheader("📅 Monthly Generation (MW)") #
    fig_m = go.Figure(go.Bar(x=[f"{i+1:02d}" for i in range(28)], y=[80, 235, 255, 270, 245, 165]+[0]*22, marker_color='#a855f7'))
    st.plotly_chart(fig_m, use_container_width=True)
