import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# 1. ตั้งค่าหน้าจอ (Wide Mode)
st.set_page_config(page_title="RMUTI AETHERA Executive", layout="wide")

# --- CSS Custom Styling (ปรับให้ดูพรีเมียมขึ้น) ---
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
    .stat-label { color: #666; font-size: 0.85rem; font-weight: bold; text-transform: uppercase; }
    .stat-value { color: #004a7c; font-size: 1.7rem; font-weight: 800; }
    .stat-unit { color: #004a7c; font-size: 0.9rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลสถานี 10 Nodes (ตรวจสอบค่า kW ให้สมดุลกับกราฟ)
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

# --- การคำนวณค่าสำคัญ ---
realtime_sum = df_nodes['kW'].sum()  # ค่ารวมที่จะไปโชว์ในข้อ 1 และเป็น Peak ของกราฟ
total_accumulated = 54.473          # ข้อ 2: สะสม (MW)
total_capacity_fixed = 2854.56      # ข้อ 3: ติดตั้งรวม (MW)

# --- 3. สร้างข้อมูลกราฟให้สัมพันธ์กับค่า Real-time (ข้อ 1) ---
def generate_trend_data(peak_val):
    times = []
    values = []
    now = datetime.now()
    for i in range(24, -1, -1):
        t = now - timedelta(hours=i)
        times.append(t.strftime("%H:00"))
        # จำลอง Curve การผลิตไฟ Solar (พีคช่วงเที่ยง)
        hour = t.hour
        if 6 <= hour <= 18:
            # ใช้สูตร Sine wave จำลองโค้งดวงอาทิตย์ ให้ Peak ใกล้เคียงกับ realtime_sum
            s_val = np.sin(np.pi * (hour - 6) / 12) * peak_val
            # ใส่ noise เล็กน้อยให้ดูสมจริง
            v = s_val * np.random.uniform(0.9, 1.1)
        else:
            v = np.random.uniform(0, 5) # กลางคืนผลิตได้น้อยมาก
        values.append(round(v, 2))
    return pd.DataFrame({"Time": times, "Power (kW)": values})

df_trend = generate_trend_data(realtime_sum)

# --- UI Header ---
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI Smart Grid Management System</h2>", unsafe_allow_html=True)
st.write("")

# --- ส่วนที่ 1: Top Bar (3 Major Metrics) ---
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""<div class='stat-card'><div><span class='stat-label'>Real Time Power (Total)</span><br>
    <span class='stat-value'>{realtime_sum:,.2f}</span> <span class='stat-unit'>kW</span></div>
    <div style='font-size: 2.2rem;'>⚡</div></div>""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""<div class='stat-card'><div><span class='stat-label'>Total Production (Accumulated)</span><br>
    <span class='
