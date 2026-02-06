import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# 1. Advanced Page Setup
st.set_page_config(page_title="RMUTI AETHERA | Analytics", layout="wide")

st.markdown("""
    <style>
    /* ขยายฟอนต์ให้ใหญ่สมดุลกับพื้นที่ */
    html, body, [class*="css"] { font-size: 1.15rem; }
    [data-testid="stMetricValue"] { font-size: 3.5rem !important; font-weight: 800 !important; color: #1e3a8a; }
    [data-testid="stMetricLabel"] { font-size: 1.3rem !important; font-weight: 600 !important; }
    h1 { font-size: 3.2rem !important; font-weight: 800; color: #1e3a8a; }
    h3 { font-size: 1.8rem !important; font-weight: 700; border-left: 5px solid #f59e0b; padding-left: 15px; }
    .stTable { font-size: 1.2rem !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (เน้นอาคาร G หนองระเวียง 354.56 kW)
df_stations = pd.DataFrame([
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง"}
])

# 3. Header Section (โลโก้ + ชื่อระบบ)
head_l, head_r = st.columns([1, 4])
with head_l:
    try: st.image("rmut.png", width=180)
    except: st.title("🏛️")
with head_r:
    st.markdown("<h1 style='margin-bottom:0;'>RMUTI AETHERA PLATFORM</h1>", unsafe_allow_html=True)
    st.markdown("### Smart Grid Management & Monthly Revenue")

st.divider()

# 4. Main Analytics Layout (แบ่ง 2 ฝั่งเหมือนภาพตัวอย่าง)
left_col, right_col = st.columns([1, 1])

with left_col:
    st.markdown("### ⚡ Today Energy Mix (kW)")
    # กราฟแสดงการใช้ไฟฟ้าวันนี้เทียบระหว่าง Solar และ Grid
    fig_today = go.Figure()
    fig_today.add_trace(go.Scatter(x=list(range(24)), y=np.random.normal(40, 5, 24), name="Consumed", fill='tozeroy', line_color='#ef4444'))
    fig_today.add_trace(go.Scatter(x=list(range(24)), y=np.random.normal(15, 3, 24), name="Solar Gen", fill='tozeroy', line_color='#3b82f6'))
    fig_today.update_layout(height=400, margin=dict(l=0,r=0,t=20,b=0), legend=dict(orientation="h", y=1.1))
    st.plotly_chart(fig_today, use_container_width=True)
    
    # สรุปตัวเลขวันนี้
    c1, c2 = st.columns(2)
    c1.metric("Today Solar", "2,854.56 kW", "Peak")
    c2.metric("Grid Usage", "500.00 kW", "15.2%")

with right_col:
    st.markdown("### 📊 Monthly Production (MW)")
    # กราฟแท่งรายเดือนเลียนแบบ Revenue ในภาพตัวอย่าง
    days = [f"{i+1:02d}" for i in range(28)]
    # จำลองค่า MW รายวัน (01-06 มีข้อมูลเยอะ, 07-28 ยังไม่มี)
    yield_data = [80, 235, 255, 270, 245, 165] + [0]*22 
    
    fig_monthly = go.Figure(data=[
        go.Bar(x=days, y=yield_data, marker_color='#a855f7', text=[f"{v}" if v>0 else "" for v in yield_data], textposition='outside')
    ])
    fig_monthly.update_layout(height=400, margin=dict(l=0,r=0,t=20,b=0), yaxis_title="Daily Yield (MW)")
    st.plotly_chart(fig_monthly, use_container_width=True)
    
    st.markdown(f"<p style='text-align:right; font-weight:bold;'>Total Production 2026-02: <span style='color:purple; font-size:1.5rem;'>1.26K MW</span></p>", unsafe_allow_html=True)

st.divider()

# 5. Bottom Section: Details & ESG
b_left, b_mid, b_right = st.columns([1.5, 0.8, 1.2])

with b_left:
    st.markdown("### 📊 Station Breakdown")
    st.table(df_stations)

with b_mid:
    st.markdown("### 🌿 ESG")
    try:
        st.image("CO2.png", width=90); st.write("**27.24 T**")
        st.image("Tree.png", width=90); st.write("**680 Trees**")
    except: st.info("Check Image Files")

with b_right:
    st.markdown("### 🤝 P2P Trading")
    st.success("Admin ⚡ Hall(2): 12.5 kWh")
    st.success("Bus(32) ⚡ Lib(4): 25.0 kWh")
    st.info("Market Status: Active (3.8 - 4.0 ฿)")
