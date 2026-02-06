import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# 1. ตั้งค่าหน้าจอ (Wide Mode)
st.set_page_config(page_title="RMUTI AETHERA Executive", layout="wide")

# --- CSS Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stApp { margin-top: -45px; }
    .stat-card {
        background-color: white;
        padding: 12px 25px;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: space-between;
        border: 1px solid #dee2e6;
    }
    .stat-label { color: #666; font-size: 0.9rem; font-weight: bold; }
    .stat-value { color: #004a7c; font-size: 1.6rem; font-weight: 800; }
    .stat-unit { color: #004a7c; font-size: 1rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลสถานี (Nodes Data) - ปรับเป็น 10 สถานีตามที่ระบุ
df_nodes = pd.DataFrame([
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168},
    {"อาคาร": "Sports Complex", "kW": 200.00, "Zone": "ศูนย์กลาง", "Lat": 14.9940, "Lon": 102.1140},
    {"อาคาร": "อาคารปฏิบัติการไฟฟ้า", "kW": 180.00, "Zone": "หนองระเวียง", "Lat": 14.9450, "Lon": 102.2150},
    {"อาคาร": "โรงอาหารหนองระเวียง", "kW": 170.00, "Zone": "หนองระเวียง", "Lat": 14.9420, "Lon": 102.2135}
])

# --- การคำนวณค่าต่างๆ ---
realtime_sum = df_nodes['kW'].sum()  # รวมค่าผลิตจริง ณ ปัจจุบัน
total_accumulated = 54.473          # ค่าผลิตสะสม (MW)
total_capacity_fixed = 2854.56      # ค่าคงที่กำลังการติดตั้งรวม (MW)

# --- ข้อมูลกราฟเทรนด์ ---
times = [(datetime.now() - timedelta(minutes=30*i)).strftime("%H:%M") for i in range(24)][::-1]
gen_values = [realtime_sum/12 + (realtime_sum/20 * np.sin(i/3)) + np.random.normal(0, 10) for i in range(24)]
df_trend = pd.DataFrame({"Time": times, "Power (kW)": gen_values})

# --- UI Header ---
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI Smart Grid Management System</h2>", unsafe_allow_html=True)
st.write("")

# --- ส่วนที่ 1: Top Bar (3 Major Metrics) ---
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""<div class='stat-card'><div><span class='stat-label'>Real Time Power</span><br>
    <span class='stat-value'>{realtime_sum:,.3f}</span> <span class='stat-unit'>kW</span></div>
    <div style='font-size: 2.2rem;'>⚡</div></div>""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""<div class='stat-card'><div><span class='stat-label'>Total Production (Accumulated)</span><br>
    <span class='stat-value'>{total_accumulated:,.3f}</span> <span class='stat-unit'>MW</span></div>
    <div style='font-size: 2.2rem;'>🔋</div></div>""", unsafe_allow_html=True)

with c3:
    st.markdown(f"""<div class='stat-card'><div><span class='stat-label'>Total Capacity (10 Nodes)</span><br>
    <span class='stat-value'>{total_capacity_fixed:,.3f}</span> <span class='stat-unit'>MW</span></div>
    <div style='font-size: 2.2rem;'>🏢</div></div>""", unsafe_allow_html=True)

st.write("---")

# --- ส่วนที่ 2: Dashboard Content (กราฟ แผนที่ และ ตาราง) ---
left, right = st.columns([1.7, 1])

with left:
    st.markdown("### 📈 Power Generation Trend")
    fig_line = px.area(df_trend, x="Time", y="Power (kW)", color_discrete_sequence=['#E85D04'])
    fig_line.update_layout(height=280, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("### 🌐 Digital Twin Map")
    fig_map = px.scatter_mapbox(df_nodes, lat="Lat", lon="Lon", color="Zone", size="kW",
                                zoom=11.2, height=350, mapbox_style="carto-positron",
                                color_discrete_map={"หนองระเวียง": "#00A8E8", "ศูนย์กลาง": "#E85D04"})
    fig_map.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig_map, use_container_width=True)

with right:
    st.markdown("### 🌿 Environment Summary")
    e1, e2, e3 = st.columns(3)
    with e1: st.image("CO2.png", use_container_width=True)
    with e2: st.image("Coal.png", use_container_width=True)
    with e3: st.image("Tree.png", use_container_width=True)
    
    st.markdown("### 📊 Station Breakdown")
    st.dataframe(df_nodes[["อาคาร", "kW", "Zone"]].sort_values("kW", ascending=False), 
                 hide_index=True, use_container_width=True, height=520)

st.caption("RMUTI Smart Grid Platform | Data Finalized for Executive Review")
