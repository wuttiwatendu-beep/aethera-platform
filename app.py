import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os

# 1. Page Configuration
st.set_page_config(page_title="AETHERA COMMAND PLATFORM", layout="wide")

st.markdown("""
    <style>
    /* ปรับแต่ง Header ให้มีช่องไฟตามที่คุณนุต้องการ */
    .header-section { margin-bottom: 30px; }
    .platform-title {
        font-size: 1.8rem !important;
        font-weight: 700;
        color: #1e3a8a;
        letter-spacing: 2px;
        margin-bottom: 30px !important; /* เว้นระยะห่างตามที่สั่ง */
    }
    .project-name {
        font-size: 2.4rem !important;
        font-weight: 800;
        color: #b43d8b;
        line-height: 1.2;
    }
    .location-name {
        font-size: 1.6rem !important;
        font-weight: 600;
        color: #1e40af;
    }

    /* สไตล์ Card สำหรับ Metric แถวบนสุด (ESG) */
    .metric-card-top {
        background-color: #f8fafc;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        border: 1px solid #e2e8f0;
    }

    /* สไตล์ Card สำหรับตัวเลขสถิติ (Real-Time) */
    .stat-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        border-bottom: 4px solid #1e3a8a;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Top Navigation Bar (Logo | Titles | NetZero)
col_l, col_m, col_r = st.columns([1, 4, 1.2])

with col_l:
    st.image("rmut.png", width=150)

with col_m:
    # รักษาระดับแนวเส้นใต้ และเพิ่มช่องไฟระหว่างบรรทัด
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    st.markdown('<p class="platform-title">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="project-name">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p class="location-name">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

with col_r:
    st.markdown("<div style='height: 90px;'></div>", unsafe_allow_html=True)
    if os.path.exists("NetZero_Platform_1.png"):
        st.image("NetZero_Platform_1.png", width=180)
    else:
        st.markdown("<p style='text-align:right; font-weight:bold;'>NetZero_Platform 1</p>", unsafe_allow_html=True)

# 3. Row 1: ESG & Environment Cards (5 Columns Style)
st.write("")
ec1, ec2, ec3, ec4, ec5 = st.columns(5)
with ec1:
    st.markdown("<div class='metric-card-top'>☀️<br><b>CO2</b></div>", unsafe_allow_html=True)
with ec2:
    st.markdown("<div class='metric-card-top'>☁️<br><b>27.24 T</b><br><small>CO2 Saved</small></div>", unsafe_allow_html=True)
with ec3:
    st.markdown("<div class='metric-card-top'>⛰️<br><b>21.79 T</b><br><small>Coal Saved</small></div>", unsafe_allow_html=True)
with ec4:
    st.markdown("<div class='metric-card-top'>🌳<br><b>Trees</b><br><small>Planted</small></div>", unsafe_allow_html=True)
with ec5:
    st.markdown("<div class='metric-card-top'>🌳<br><b>Trees</b><br><small>Planted</small></div>", unsafe_allow_html=True)

# 4. Row 2: Statistics Metrics Grid (6 Columns Style)
st.write("")
m1, m2, m3, m4, m5, m6 = st.columns(6)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("Total Yield (MW)", "28.80")
m5.metric("Peak Capacity (kW)", "10")
m6.metric("P2P Volume Today", "80.3")

# 5. Row 3: Main Charts (Production & Power Mix)
st.write("")
c_left, c_right = st.columns(2)

with c_left:
    st.subheader("⚡ 24-Hour Details 00 (kW)")
    # กราฟเหลือง/ส้ม ตามรูปตัวอย่าง
    hours = [f"{i:02d}:00" for i in range(24)]
    gen_data = [5, 5, 5, 10, 20, 100, 500, 1200, 2200, 2800, 2854, 2700, 2300, 1500, 800, 200, 50, 10, 5, 5, 5, 5, 5, 5]
    fig_gen = go.Figure(go.Scatter(x=hours, y=gen_data, fill='tozeroy', line_color='#f59e0b', name="Today Power Mix"))
    fig_gen.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10))
    st.plotly_chart(fig_gen, use_container_width=True)

with c_right:
    st.subheader("⚡ Today Power Mix (kW)")
    # กราฟเส้นเปรียบเทียบ
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 3, 24), name="Load", line_color='#ef4444'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(25, 2, 24), name="Solar", line_color='#3b82f6'))
    fig_mix.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10))
    st.plotly_chart(fig_mix, use_container_width=True)

# 6. Row 4: Station Details & Monthly
st.write("")
b_left, b_right = st.columns([1.2, 1])

with b_left:
    st.subheader("📋 Station Details")
    # ตาราง 10 สถานีตามรูปภาพ
    df_stations = pd.DataFrame({
        "อาคาร": ["สำนักส่งเสริมวิชาการฯ (35)", "คณะบริหารธุรกิจ (32)", "อาคารเรียนรวม 7", "สำนักวิทยบริการฯ (4)", "หอประชุมวชิราลงกรณ (2)", "สำนักงานอธิการบดี (1)", "Sports Complex", "อาคาร A (สำรอง)", "อาคาร B (สำรอง)", "G กลุ่มวิชาชีพเครื่องกล"],
        "Zone": ["ศูนย์กลาง"] * 9 + ["หนองระเวียง"],
        "kW": [485.76, 400.00, 314.24, 280.00, 250.00, 220.00, 200.00, 180.00, 170.00, 354.56]
    })
    st.dataframe(df_stations, use_container_width=True, hide_index=True)

with b_right:
    st.subheader("📅 Monthly Generation (MW)")
    # กราฟแท่งสีม่วง
    months = [f"{i+1:02d}" for i in range(28)]
    monthly_vals = [80, 235, 255, 270, 245, 165, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fig_month = go.Figure(go.Bar(x=months, y=monthly_vals, marker_color='#a855f7'))
    fig_month.update_layout(height=320, margin=dict(t=10, b=10))
    st.plotly_chart(fig_month, use_container_width=True)
