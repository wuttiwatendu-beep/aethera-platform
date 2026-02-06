import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# 2. ข้อมูลคงที่และพิกัด (อ้างอิงจากข้อมูลที่คุณนุส่งมา)
total_accumulated_mw = 54.473  # MW
total_capacity_mw = 2854.56    # MW (แก้ไขจุดทศนิยมให้ถูกต้องตามภาพ)
total_accumulated_kwh = total_accumulated_mw * 1000 

# คำนวณค่าสิ่งแวดล้อมอัตโนมัติ
co2_saved = total_accumulated_kwh * 0.50 / 1000  # 27.24 Tons
coal_saved = total_accumulated_kwh * 0.40 / 1000 # 21.79 Tons
trees_planted = int(total_accumulated_kwh / 80) # 680 Trees

# ข้อมูลพิกัดสถานีสำหรับแผนที่
df_nodes = pd.DataFrame([
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160},
    {"อาคาร": "Sports Complex", "kW": 200.00, "Zone": "ศูนย์กลาง", "Lat": 14.9940, "Lon": 102.1140},
    {"อาคาร": "อาคารปฏิบัติการไฟฟ้า", "kW": 180.00, "Zone": "หนองระเวียง", "Lat": 14.9450, "Lon": 102.2150},
    {"อาคาร": "โรงอาหารหนองระเวียง", "kW": 170.00, "Zone": "หนองระเวียง", "Lat": 14.9420, "Lon": 102.2135}
])
realtime_sum = df_nodes['kW'].sum()

# 3. ส่วนการแสดงผล (UI)
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)

# Metric Cards (แก้ไขปัญหา TypeError โดยลบคอมมาในชื่อตัวแปรออก)
m1, m2, m3 = st.columns(3)
with m1: st.metric("Real Time Power", f"{realtime_sum:,.2f} kW")
with m2: st.metric("Total Production", f"{total_accumulated_mw:,.3f} MW")
with m3: st.metric("Total Capacity", f"{total_capacity_mw:,.2f} MW")

st.write("---")

# 4. Main Content Layout
col_left, col_right = st.columns([1.5, 1])

with col_left:
    # กราฟเทรนด์ 07:00 - 17:30
    st.markdown("### 📈 Power Generation Trend")
    hours = [f"{h:02d}:00" for h in range(24)]
    curve = [np.sin(np.pi * (h-7)/10.5) * realtime_sum if 7 <= h <= 17.5 else 0 for h in range(24)]
    df_trend = pd.DataFrame({"Time": hours, "Power (kW)": curve})
    fig_line = px.area(df_trend, x="Time", y="Power (kW)", color_discrete_sequence=['#FF9100'])
    fig_line.update_layout(height=300, margin=dict(l=0, r=0, t=20, b=0))
    st.plotly_chart(fig_line, use_container_width=True)

    # แผนที่ Digital Twin กลับมาแล้วครับ!
    st.markdown("### 🌐 Digital Twin Map")
    fig_map = px.scatter_mapbox(df_nodes, lat="Lat", lon="Lon", color="Zone", size="kW",
                                zoom=11.5, height=350, mapbox_style="carto-positron")
    fig_map.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig_map, use_container_width=True)

with col_right:
    # แสดงค่า Environment Benefits ตามที่คุณนุต้องการ
    st.markdown("### 🌿 Environment Benefits")
    ev1, ev2, ev3 = st.columns(3)
    with ev1:
        st.image("CO2.png", use_container_width=True)
        st.write(f"**{co2_saved:,.2f} Tons**")
    with ev2:
        st.image("Coal.png", use_container_width=True)
        st.write(f"**{coal_saved:,.2f} Tons**")
    with ev3:
        st.image("Tree.png", use_container_width=True)
        st.write(f"**{trees_planted:,.0f} Trees**")
    
    st.write("---")
    # ตารางรายละเอียดสถานี
    st.markdown("### 📊 Station Details (kW)")
    st.dataframe(df_nodes[["อาคาร", "kW", "Zone"]].sort_values("kW", ascending=False), 
                 hide_index=True, use_container_width=True, height=400)
