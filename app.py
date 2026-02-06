import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, time

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI AETHERA Executive", layout="wide")

# --- CSS แบบเสถียร ---
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

# 2. ข้อมูลสถานี 10 Nodes
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

# --- ค่าคงที่ตามโจทย์ ---
total_capacity_fixed = 2854.56  # ข้อ 3: MW
total_accumulated = 54.473      # ข้อ 2: MW
realtime_sum = df_nodes['kW'].sum() # ข้อ 1: รวม kW ปัจจุบัน

# --- 3. สร้างข้อมูลกราฟ (07:00 - 17:30) ---
hours = np.linspace(0, 23.5, 48) # ทุกๆ 30 นาที
powers = []

for h in hours:
    if 7.0 <= h <= 17.5:
        # จำลองโค้ง Solar พีคตอนเที่ยง
        normalized = (h - 7.0) / (17.5 - 7.0)
        val = np.sin(np.pi * normalized) * realtime_sum
        powers.append(max(0, val * np.random.uniform(0.98, 1.02)))
    else:
        powers.append(0)

df_trend = pd.DataFrame({
    "Time": [f"{int(h):02d}:{int((h%1)*60):02d}" for h in hours],
    "Power (kW)": powers
})

# --- UI Layout ---
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)
st.write("")

# Metric Cards
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='stat-card'><div><span class='stat-label'>Real Time Power</span><br><span class='stat-value'>{realtime_sum:,.2f}</span> <span class='stat-unit'>kW</span></div><div style='font-size: 2rem;'>⚡</div></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='stat-card'><div><span class='stat-label'>Total Production</span><br><span class='stat-value'>{total_accumulated:,.3f}</span> <span class='stat-unit'>MW</span></div><div style='font-size: 2rem;'>🔋</div></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='stat-card'><div><span class='stat-label'>Total Capacity</span><br><span class='stat-value'>{total_capacity_fixed:,.2f}</span> <span class='stat-unit'>MW</span></div><div style='font-size: 2rem;'>🏢</div></div>", unsafe_allow_html=True)

st.write("---")

col_left, col_right = st.columns([1.7, 1])

with col_left:
    st.markdown("### 📈 Power Generation Trend (07:00 - 17:30)")
    fig_line = px.area(df_trend, x="Time", y="Power (kW)", color_discrete_sequence=['#FF9100'])
    fig_line.update_layout(
        height=320, 
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis=dict(tickmode='linear', dtick=4) # แสดง label ทุกๆ 2 ชั่วโมงให้อ่านง่าย
    )
    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("### 🌐 Digital Twin Map")
    fig_map = px.scatter_mapbox(df_nodes, lat="Lat", lon="Lon", color="Zone", size="kW",
                                zoom=11.2, height=350, mapbox_style="carto-positron")
    fig_map.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig_map, use_container_width=True)

with col_right:
    st.markdown("### 🌿 Environment Benefits")
    e1, e2, e3 = st.columns(3)
    with e1: st.image("CO2.png", use_container_width=True)
    with e2: st.image("Coal.png", use_container_width=True)
    with e3: st.image("Tree.png", use_container_width=True)
    
    st.markdown("### 📊 Station Details (kW)")
    st.dataframe(df_nodes[["อาคาร", "kW", "Zone"]].sort_values("kW", ascending=False), 
                 hide_index=True, use_container_width=True, height=520)

st.caption("RMUTI Smart Grid Platform | Fixed Error & Optimized Curve")
