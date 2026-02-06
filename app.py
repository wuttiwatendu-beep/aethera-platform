import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI AETHERA P2P", layout="wide")

# 2. ข้อมูล Nodes ทั้งหมด (เพิ่มพิกัดและโซน)
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

# คำนวณค่าหลัก (ต้องทำก่อนแสดงผล m1, m2, m3)
realtime_sum = df_nodes['kW'].sum() 
total_accumulated_mw = 54.473 #
total_capacity_mw = 2854.56   #

# ข้อมูล P2P Trading (จำลองการจับคู่ภายในศูนย์กลาง)
df_p2p = pd.DataFrame([
    {"Time": "11:30", "Seller": "สำนักงานอธิการบดี (1)", "Buyer": "หอประชุมวทัญญูฯ (2)", "Units": "12.5 kWh", "Price": "3.8 ฿"},
    {"Time": "11:45", "Seller": "คณะบริหารธุรกิจ (32)", "Buyer": "สำนักวิทยบริการฯ (4)", "Units": "25.0 kWh", "Price": "4.0 ฿"},
    {"Time": "12:05", "Seller": "สำนักส่งเสริมวิชาการฯ (35)", "Buyer": "อาคารเรียนรวม 7", "Units": "42.8 kWh", "Price": "3.9 ฿"}
])

# 3. ส่วนการแสดงผล UI
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI AETHERA: Smart Grid & P2P Trading</h2>", unsafe_allow_html=True)

# Metric Bar
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Real Time Power", f"{realtime_sum:,.2f} kW")
with m2: st.metric("Total Production", f"{total_accumulated_mw:,.3f} MW")
with m3: st.metric("Total Capacity", f"{total_capacity_mw:,.2f} MW")
with m4: st.metric("P2P Volume Today", "80.3 kWh", delta="15% vs Yesterday")

st.write("---")

# 4. Layout: แบ่งซ้ายขวา
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.markdown("### 🌐 Digital Twin & Trading Network")
    # แผนที่เจาะจงโซนศูนย์กลางที่เทรดกัน
    fig_map = px.scatter_mapbox(df_nodes[df_nodes['Zone']=='ศูนย์กลาง'], lat="Lat", lon="Lon", 
                                color="kW", size="kW", hover_name="อาคาร",
                                zoom=15, height=450, mapbox_style="carto-positron")
    fig_map.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig_map, use_container_width=True)
    
    st.markdown("### 💹 P2P Market Price Trend")
    # กราฟราคาค่าไฟ P2P ระหว่างวัน
    p_time = [f"{h:02d}:00" for h in range(8, 18)]
    p_price = [4.5, 4.3, 4.1, 3.8, 3.7, 3.7, 3.9, 4.2, 4.4, 4.5]
    fig_price = px.line(x=p_time, y=p_price, labels={'x':'Time', 'y':'Price (THB)'}, markers=True)
    fig_price.update_traces(line_color='#2ECC71')
    st.plotly_chart(fig_price, use_container_width=True)

with col_right:
    st.markdown("### 🤝 Live P2P Transactions")
    st.info("Market Status: **Open** (Trading Active)")
    
    # แสดง Transaction Card
    for _, row in df_p2p.iterrows():
        st.markdown(f"""
        <div style="background-color: white; padding: 12px; border-radius: 10px; border-left: 5px solid #2ECC71; margin-bottom: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
            <small style='color:gray;'>{row['Time']}</small><br>
            <b>{row['Seller']}</b> ⚡ <b>{row['Buyer']}</b><br>
            <span style='color:#2ECC71; font-weight:bold;'>{row['Units']}</span> | ราคา <span style='color:#004a7c;'>{row['Price']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 💰 Smart Grid Summary")
    st.write(f"Savings from P2P: **฿1,420.50 Today**")
    st.write(f"Grid Independence: **85%**")

st.caption("RMUTI Smart Campus | Peer-to-Peer Energy Trading System Enabled")
