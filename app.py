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
        margin-bottom: 35px !important; 
        letter-spacing: 2px;
    }
    .project-title { font-size: 2.2rem !important; font-weight: 800; color: #b43d8b; line-height: 1.2; }
    .location-title { font-size: 1.5rem !important; font-weight: 600; color: #1e40af; }
    
    .weather-card {
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        color: white;
        border-radius: 12px;
        padding: 12px;
        text-align: left;
    }
    
    /* จัดการ Container ของ ESG ให้ขยับรูปไปทางขวาตรงกับตัวเลข */
    .esg-item {
        display: flex;
        flex-direction: column;
        align-items: center; /* จัดกึ่งกลางแนวตั้ง */
        padding-left: 20px;  /* ขยับกลุ่มทั้งหมดไปทางขวาตามคุณนุสั่ง */
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Weather API (Korat)
def get_korat_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=14.97&longitude=102.10&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        res = requests.get(url).json()
        return res['current']
    except: return None

w = get_korat_weather()

# 3. Header Section
h1, h2, h3 = st.columns([1, 4, 1.8])

with h1:
    st.image("rmut.png", width=150)

with h2:
    st.markdown("<div style='height: 55px;'></div>", unsafe_allow_html=True)
    st.markdown('<p class="platform-header">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="project-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p class="location-title">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

with h3:
    # ใช้ไฟล์โลโก้ใหม่ที่คุณนุเพิ่งส่งมา
    st.markdown("<div style='text-align: right; margin-bottom: 10px;'>", unsafe_allow_html=True)
    st.image("NetZero platform 1.png", width=220)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # หน้าต่างสภาพอากาศโคราช
    if w:
        st.markdown(f"""
        <div class="weather-card">
            <small>📍 Nakhon Ratchasima Weather</small><br>
            <b style='font-size:1.6rem;'>{w['temperature_2m']}°C</b><br>
            <small>Humidity: {w['relative_humidity_2m']}% | Wind: {w['wind_speed_10m']} km/h</small>
        </div>
        """, unsafe_allow_html=True)

# 4. Row 1: ESG Metrics (3 Columns - Fixed Alignment)
st.write("")
st.write("")
e_label, e_co2, e_coal, e_tree = st.columns([1.2, 1, 1, 1])

with e_label:
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    st.button("ESG Metrics", disabled=True)

with e_co2:
    st.markdown("<div class='esg-item'>", unsafe_allow_html=True)
    st.image("CO2.png", width=70) #
    st.markdown("<div style='text-align:center;'><b>27.24 T</b><br><small>CO2 Saved</small></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with e_coal:
    st.markdown("<div class='esg-item'>", unsafe_allow_html=True)
    st.image("Coal.png", width=70) #
    st.markdown("<div style='text-align:center;'><b>21.79 T</b><br><small>Coal Saved</small></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with e_tree:
    st.markdown("<div class='esg-item'>", unsafe_allow_html=True)
    st.image("Tree.png", width=70) #
    st.markdown("<div style='text-align:center;'><b>680</b><br><small>Trees Planted</small></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Row 2: Performance Metrics
st.divider()
m1, m2, m3, m4, m5, m6 = st.columns(6)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("Daily Yield (MW)", "28.80")
m5.metric("Solar Capacity (kW)", "10")
m6.metric("P2P Volume Today", "80.3")

# 6. Row 3: Charts & Station Details
c_left, c_right = st.columns([1.5, 1])

with c_left:
    st.subheader("⚡ 24-Hour Solar Production (kW)")
    hours = [f"{i:02d}:00" for i in range(24)]
    gen_val = [5,5,10,50,200,800,1600,2400,2854,2700,2200,1500,800,300,50,10,5,5,5,5,5,5,5,5]
    fig = go.Figure(go.Scatter(x=hours, y=gen_val, fill='tozeroy', line_color='#f59e0b'))
    st.plotly_chart(fig, use_container_width=True)

with c_right:
    st.subheader("📋 Station Details")
    df = pd.DataFrame({
        "อาคาร (Station)": ["สนง.วิชาการฯ (35)", "บริหารธุรกิจ (32)", "อาคาร A (สำรอง)", "อาคาร B (สำรอง)", "เครื่องกล (G)", "เรียนรวม 7"],
        "kW": [485.76, 400.00, 380.00, 365.00, 354.56, 314.24]
    })
    st.dataframe(df, use_container_width=True)
