import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 1. ข้อมูลพื้นฐาน (อ้างอิงจากภาพของคุณนุ)
total_accumulated_mw = 54.473  #
total_capacity_mw = 2854.56    #
total_accumulated_kwh = total_accumulated_mw * 1000

# สูตรคำนวณสิ่งแวดล้อม
co2_saved = 27.24  # Tons
coal_saved = 21.79 # Tons
trees_planted = 680 # Trees

# ข้อมูล 10 อาคาร (ตรวจสอบให้ครบตามภาพ image_58c223.png)
df_nodes = pd.DataFrame([
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160},
    {"อาคาร": "Sports Complex", "kW": 200.00, "Zone": "ศูนย์กลาง", "Lat": 14.9940, "Lon": 102.1140},
    {"อาคาร": "อาคารปฏิบัติการไฟฟ้า", "kW": 180.00, "Zone": "หนองระเวียง", "Lat": 14.9450, "Lon": 102.2150},
    {"อาคาร": "โรงอาหารหนองระเวียง", "kW": 170.00, "Zone": "หนองระเวียง", "Lat": 14.9420, "Lon": 102.2135}
])
realtime_sum = df_nodes['kW'].sum()

# 2. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid & P2P", layout="wide")
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI AETHERA: Smart Grid Management</h2>", unsafe_allow_html=True)

# Metric Bar
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Real Time Power", f"{realtime_sum:,.2f} kW")
with m2: st.metric("Total Production", f"{total_accumulated_mw:,.3f} MW")
with m3: st.metric("Total Capacity", f"{total_capacity_mw:,.2f} MW")
with m4: st.metric("P2P Volume Today", "80.3 kWh", delta="15%")

st.write("---")

# 3. จัด Layout เป็น 2 คอลัมน์หลัก
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.markdown("### 🌐 Digital Twin & Trading Map")
    fig_map = px.scatter_mapbox(df_nodes, lat="Lat", lon="Lon", color="Zone", size="kW", 
                                zoom=11.5, height=450, mapbox_style="carto-positron")
    st.plotly_chart(fig_map, use_container_width=True)
    
    st.markdown("### 📈 Power Generation Trend")
    hours = [f"{h:02d}:00" for h in range(24)]
    curve = [np.sin(np.pi * (h-7)/10.5) * realtime_sum if 7 <= h <= 17.5 else 0 for h in range(24)]
    fig_line = px.area(x=hours, y=curve, color_discrete_sequence=['#FF9100'], height=300)
    st.plotly_chart(fig_line, use_container_width=True)

with col_right:
    # --- ส่วนรูปภาพ Environment ที่คุณนุอัปโหลด ---
    st.markdown("### 🌿 Environment Benefits")
    ev1, ev2, ev3 = st.columns(3)
    with ev1:
        st.image("CO2.png", use_container_width=True) # ตรวจสอบชื่อไฟล์ให้ตรงกับที่คุณนุเก็บไว้
        st.write(f"**{co2_saved} Tons**")
    with ev2:
        st.image("Coal.png", use_container_width=True)
        st.write(f"**{coal_saved} Tons**")
    with ev3:
        st.image("Tree.png", use_container_width=True)
        st.write(f"**{trees_planted} Trees**")
    
    st.write("---")
    
    # --- รายละเอียดการเทรด P2P ---
    st.markdown("### 🤝 Live P2P Transactions (Central Campus)")
    st.success("Admin (1) ⚡ Conf: 12.5 kWh @ 3.8฿")
    st.success("Bus (32) ⚡ Lib (4): 25.0 kWh @ 4.0฿")
    
    st.write("---")
    
    # --- ข้อมูลอาคารทั้ง 10 แห่ง ---
    st.markdown("### 📊 Station Details (kW)")
    st.dataframe(df_nodes[["อาคาร", "kW", "Zone"]].sort_values("kW", ascending=False), 
                 hide_index=True, use_container_width=True, height=350)
