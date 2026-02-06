import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# 1. ข้อมูลพื้นฐาน (อ้างอิงจากภาพที่คุณนุส่งมา)
total_accumulated_mw = 54.473  # ค่าผลิตสะสม (MW)
total_capacity_mw = 2854.56    # ค่าคงที่การติดตั้ง (MW)
total_accumulated_kwh = total_accumulated_mw * 1000 # แปลงเป็น kWh เพื่อคำนวณค่าสิ่งแวดล้อม

# --- สูตรคำนวณ Environment Benefits ---
co2_saved = total_accumulated_kwh * 0.50 / 1000  # Tons (0.50 kg/kWh)
coal_saved = total_accumulated_kwh * 0.40 / 1000 # Tons (0.40 kg/kWh)
trees_planted = int(total_accumulated_kwh / 80) # ต้น

# 2. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# --- CSS Styling ---
st.markdown("""
    <style>
    .stat-card {
        background-color: white;
        padding: 10px 20px;
        border-radius: 50px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: space-between;
        border: 1px solid #dee2e6;
    }
    .stat-label { color: #666; font-size: 0.8rem; font-weight: bold; }
    .stat-value { color: #004a7c; font-size: 1.4rem; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# 3. ข้อมูลสถานี (10 Nodes)
df_nodes = pd.DataFrame([
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00},
    {"อาคาร": "Sports Complex", "kW": 200.00},
    {"อาคาร": "อาคารปฏิบัติการไฟฟ้า", "kW": 180.00},
    {"อาคาร": "โรงอาหารหนองระเวียง", "kW": 170.00}
])
realtime_sum = df_nodes['kW'].sum()

# 4. แสดงผล Header และ Metric Cards
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='stat-card'><div><span class='stat-label'>Real Time Power</span><br><span class='stat-value'>{realtime_sum:,.2f} kW</span></div><div style='font-size:1.5rem;'>⚡</div></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='stat-card'><div><span class='stat-label'>Total Production</span><br><span class='stat-value'>{total_accumulated_mw:,.3f} MW</span></div><div style='font-size:1.5rem;'>🔋</div></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='stat-card'><div><span class='stat-label'>Total Capacity</span><br><span class='stat-value'>{total_capacity_mw:,.2f} MW</span></div><div style='font-size:1.5rem;'>🏢</div></div>", unsafe_allow_html=True)

st.write("---")

# 5. แบ่งส่วนเนื้อหาหลัก
col_left, col_right = st.columns([1.7, 1])

with col_left:
    st.markdown("### 📈 Power Generation Trend (07:00 - 17:30)")
    # สร้างข้อมูลกราฟจำลอง
    hours = [f"{h:02d}:00" for h in range(24)]
    curve = [np.sin(np.pi * (h-7)/10.5) * realtime_sum if 7 <= h <= 17.5 else 0 for h in range(24)]
    df_trend = pd.DataFrame({"Time": hours, "Power (kW)": curve})
    fig = px.area(df_trend, x="Time", y="Power (kW)", color_discrete_sequence=['#FF9100'])
    st.plotly_chart(fig, use_container_width=True)

with col_right:
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
    st.markdown("### 📊 Station Details (kW)")
    st.dataframe(df_nodes.sort_values("kW", ascending=False), hide_index=True, use_container_width=True)
