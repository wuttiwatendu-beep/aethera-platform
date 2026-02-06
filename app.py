import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. ตั้งค่าหน้าจอ (โทนสว่าง Professional)
st.set_page_config(page_title="RMUTI AETHERA Dashboard", layout="wide")

# CSS สำหรับตกแต่ง Card และ Icons
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .env-card {
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #e2e8f0;
    }
    .stMetric { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 10px; 
        border-top: 5px solid #E85D04;
    }
    h1 { color: #E85D04 !important; font-weight: 800; text-align: center; }
    h3 { color: #006699 !important; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลโครงการ (9+1 Nodes)
data = [
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล (หนองระเวียง)", "kW": 354.56, "กลุ่ม": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (อาคาร 35)", "kW": 485.76, "กลุ่ม": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (อาคาร 32)", "kW": 400.00, "กลุ่ม": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "สำนักวิทยบริการฯ (อาคาร 4)", "kW": 280.00, "กลุ่ม": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (อาคาร 2)", "kW": 250.00, "กลุ่ม": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (อาคาร 1)", "kW": 220.00, "กลุ่ม": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160},
    {"อาคาร": "Sports Complex (Gym)", "kW": 150.00, "กลุ่ม": "ศูนย์กลาง", "Lat": 14.9940, "Lon": 102.1140},
    {"อาคาร": "อาคารเรียนรวม (อาคาร 7)", "kW": 100.00, "กลุ่ม": "ศูนย์กลาง", "Lat": 14.9930, "Lon": 102.1145},
    {"อาคาร": "อาคาร A (New Install)", "kW": 314.24, "กลุ่ม": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168},
    {"อาคาร": "อาคาร B (New Install)", "kW": 300.00, "กลุ่ม": "ศูนย์กลาง", "Lat": 14.9900, "Lon": 102.1170},
]
df = pd.DataFrame(data)

# --- HEADER ---
st.title("🏛️ RMUTI AETHERA: Smart University Grid")
st.markdown("<p style='text-align: center;'>ระบบบริหารจัดการพลังงานอัจฉริยะ มทร.อีสาน (Phase 1: มีนาคม 2569)</p>", unsafe_allow_html=True)

# --- ส่วนที่ 1: Environment Benefits (Icons & Stats) ---
st.markdown("<h3 style='text-align: center;'>🔵 Environment Benefits</h3>", unsafe_allow_html=True)
col_env1, col_env2, col_env3 = st.columns(3)

with col_env1:
    st.markdown("""
        <div class='env-card'>
            <p style='font-weight: bold; color: #64748b;'>CO2 Emission Saved</p>
            <img src='https://cdn-icons-png.flaticon.com/512/1843/1843544.png' width='70'>
            <h2 style='color: #22c55e;'>40.13 <span style='font-size: 16px; color: #94a3b8;'>tons</span></h2>
        </div>
    """, unsafe_allow_html=True)

with col_env2:
    st.markdown("""
