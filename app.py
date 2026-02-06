import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. ตั้งค่าหน้าจอ (เสถียรที่สุดคือใช้ Layout มาตรฐาน)
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# CSS สำหรับโทนสีสว่าง และหัวข้อสีส้ม RMUTI
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stMetric { 
        background-color: #f8fafc; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #e2e8f0;
    }
    h1, h2, h3 { color: #E85D04 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. เตรียมข้อมูล (ยึดตาม 354.56 kW และ 2.5 MW)
data = [
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล (หนองระเวียง)", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (อาคาร 35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (อาคาร 32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "อาคารสำนักวิทยบริการฯ (อาคาร 4)", "kW": 280.00, "Zone": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (อาคาร 2)", "kW": 250.00, "Zone": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (อาคาร 1)", "kW": 220.00, "Zone": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160},
    {"อาคาร": "Sports Complex (Gym)", "kW": 150.00, "Zone": "ศูนย์กลาง", "Lat": 14.9940, "Lon": 102.1140},
    {"อาคาร": "อาคารเรียนรวม (อาคาร 7)", "kW": 100.00, "Zone": "ศูนย์กลาง", "Lat": 14.9930, "Lon": 102.1145},
    {"อาคาร": "อาคาร A (เพิ่มใหม่)", "kW": 314.24, "Zone": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168},
    {"อาคาร": "อาคาร B (เพิ่มใหม่)", "kW": 300.00, "Zone": "ศูนย์กลาง", "Lat": 14.9900, "Lon": 102.1170},
]
df = pd.DataFrame(data)

# --- ส่วนหัวโปรแกรม ---
st.title("🏫 RMUTI AETHERA: Smart Energy Dashboard")
st.write("ระบบบริหารจัดการพลังงานแสงอาทิตย์ (Phase 1: ติดตั้ง มีนาคม 2569)")

# --- แถบตัวเลขสรุป (Executive Metrics) ---
m1, m2, m3 = st.columns(3)
m1.metric("กำลังผลิตรวมศูนย์กลาง", "2.50 MW", "9 Nodes")
m2.metric("กำลังผลิตหนองระเวียง", "354.56 kW", "อาคาร G")
m3.metric("เป้าหมายการประหยัด", "4.2 ล้านบาท/ปี", "ROI 4.5 ปี")

st.divider()

# --- ส่วนแสดงผลหลัก (Split Screen) ---
col_map, col_table = st.columns([1.5, 1])

with col_map:
    st.subheader("📍 พิกัดโครงข่ายพลังงาน 10 สถานี")
    # ใช้ px.scatter_mapbox ที่เสถียรที่สุดในโทนสีสว่าง
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="Zone", size="kW",
                            hover_name="อาคาร", zoom=11, height=500,
                            color_discrete_map={"หนองระเวียง": "#00A8E8", "ศูนย์กลาง": "#E85D04"},
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
