import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI AETHERA Executive", layout="wide")

# --- CSS แบบปลอดภัย (Safe Styling) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stat-card {
        background-color: white;
        padding: 15px 25px;
        border-radius: 50px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: space-between;
        border: 1px solid #dee2e6;
        margin-bottom: 10px;
    }
    .stat-label { color: #666; font-size: 0.9rem; font-weight: bold; }
    .stat-value { color: #004a7c; font-size: 1.6rem; font-weight: 800; }
    .stat-unit { color: #004a7c; font-size: 1rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลสถานี (Node Data)
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

# --- การคำนวณค่าคงที่และ Real-time ---
realtime_sum = df_nodes['kW'].sum() 
total_accumulated = 54.473 # MW (ค่าจากข้อ 2)
total_capacity_fixed = 2854.56 # MW (ค่าจากข้อ 3)

# 3. ข้อมูลกราฟ (สัมพันธ์กับ Real-time Sum ในข้อ 1)
times = [(datetime.now() - timedelta(hours=i)).strftime("%H:00") for i in range(24, -1, -1)]
# สร้าง Curve เลียนแบบ Solar โดยให้ค่า Peak ใกล้เคียงกับ realtime_sum
base_values = [np.sin(np.pi * (i/24)) * realtime_sum if 6 <= i <= 18 else 0 for i in range(25)]
df_trend = pd.DataFrame({"Time": times, "Power (kW)": base_values})

# --- ส่วนแสดงผล UI ---
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)
st.write("")

# Top Bar Metrics (ใช้ HTML String แบบธรรมดาเพื่อลดความเสี่ยง Syntax Error)
c1, c2, c3 = st.columns(3)

with c1:
    content1 = f"<div class='stat-card'><div><span class='stat-label'>Real Time Power</span><br><span class='stat-value'>{realtime_sum:,.2f}</span> <span class='stat-unit'>kW</span></div><div style='font-size: 2rem;'>⚡</div></div>"
    st.markdown(content1, unsafe_allow_html=True)

with c2:
    content2 = f"<div class='stat-card'><div><span class='stat-label'>Total Production</span><br><span class='stat-value'>{total_accumulated:,.3f}</span> <span class='stat-unit'>MW</span></div><div style='font-size: 2rem;'>🔋</div></div>"
    st.markdown(content2, unsafe_allow_html=True)

with c3:
    content3 = f"<div class='stat-card'><div><span class='stat-label'>Total Capacity</span><br><span class='stat-value'>{total_capacity_fixed:,.2f}</span> <span class='stat-unit'>MW</span></div><div style='font-size: 2rem;'>🏢</div></div>"
    st.markdown(content3, unsafe_allow_html=True)

st.write("---")

# Main Dashboard Content
col_left, col_right = st.columns([1.7, 1])

with col_left:
    st.markdown("### 📈 Power Generation Trend (Real-time Output)")
    fig_line = px.area(df_trend, x="Time", y="Power (kW)", color_discrete_sequence=['#FF9100'])
    fig_line.update_layout(height=300, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("### 🌐 Digital Twin Map")
    fig_map = px.scatter_mapbox(df_nodes, lat="Lat", lon="Lon", color="Zone", size="kW",
                                zoom=11.2, height=350, mapbox_style="carto-positron")
    fig_map.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig_map, use_container_width=True)

with col_right:
    st.markdown("### 🌿 Environment Benefits")
    e1, e2, e3 = st.columns(3)
    # แสดงรูปภาพ (ตรวจสอบว่ามีไฟล์ใน Repo)
    with e1: st.image("CO2.png", use_container_width=True)
    with e2: st.image("Coal.png", use_container_width=True)
    with e3: st.image("Tree.png", use_container_width=True)
    
    st.markdown("### 📊 Station Details (kW)")
    st.dataframe(df_nodes[["อาคาร", "kW"]].sort_values("kW", ascending=False), 
                 hide_index=True, use_container_width=True, height=500)

st.caption("RMUTI Smart Grid Platform | Stabilized Version")
