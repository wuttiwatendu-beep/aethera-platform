import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# CSS สำหรับจัดการ Layout ของ Environment Benefits ให้สวยเหมือนในรูปตัวอย่าง
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    .env-card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #e1e8ed;
    }
    .env-title { color: #004a7c; font-weight: bold; font-size: 18px; margin-bottom: 10px; }
    .env-value { font-size: 24px; font-weight: bold; color: #333; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลโครงการ
df = pd.DataFrame([
    {"Bldg": "อาคาร G (หนองระเวียง)", "kW": 354.56, "Zone": "Nong Rawiang", "Lat": 14.9435, "Lon": 102.2140},
    {"Bldg": "อาคาร 35 (ทะเบียน)", "kW": 485.76, "Zone": "Main Campus", "Lat": 14.9922, "Lon": 102.1162},
    {"Bldg": "อาคาร 32 (บริหาร)", "kW": 400.00, "Zone": "Main Campus", "Lat": 14.9925, "Lon": 102.1155},
    {"Bldg": "อาคาร 4 (วิทยบริการ)", "kW": 280.00, "Zone": "Main Campus", "Lat": 14.9910, "Lon": 102.1165},
    {"Bldg": "อาคาร 2 (หอประชุม)", "kW": 250.00, "Zone": "Main Campus", "Lat": 14.9905, "Lon": 102.1158},
    {"Bldg": "อาคาร 1 (อธิการบดี)", "kW": 220.00, "Zone": "Main Campus", "Lat": 14.9915, "Lon": 102.1160},
    {"Bldg": "Sports Complex", "kW": 150.00, "Zone": "Main Campus", "Lat": 14.9940, "Lon": 102.1140},
    {"Bldg": "อาคารเรียนรวม 7", "kW": 100.00, "Zone": "Main Campus", "Lat": 14.9930, "Lon": 102.1145},
    {"Bldg": "อาคาร A", "kW": 314.24, "Zone": "Main Campus", "Lat": 14.9935, "Lon": 102.1168},
    {"Bldg": "อาคาร B", "kW": 300.00, "Zone": "Main Campus", "Lat": 14.9900, "Lon": 102.1170}
])

# --- ส่วนหัวข้อ ---
st.markdown("<h1 style='text-align: center; color: #E85D04;'>🏛️ RMUTI AETHERA: Executive Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ระบบบริหารจัดการพลังงานอัจฉริยะ มทร.อีสาน (Phase 1)</p>", unsafe_allow_html=True)

# --- ส่วนที่ 1: Environment Benefits (ใช้รูปภาพที่คุณนุส่งมา) ---
st.markdown("<div style='text-align: center; margin-bottom: 20px;'><span style='background-color: #00a8e8; color: white; padding: 5px 20px; border-radius: 20px;'>🔵 Environment Benefits</span></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='env-card'><div class='env-title'>CO2 Emission Saved</div>", unsafe_allow_html=True)
    # ใช้รูป CO2 Cloud
    st.image("https://i.ibb.co/L9YmYfG/co2-cloud.png", use_container_width=True)
    st.markdown("<div class='env-value'>40.13 tons</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='env-card'><div class='env-title'>Standard Coal Saved</div>", unsafe_allow_html=True)
    # ใช้รูป Coal in Hand
    st.image("https://i.ibb.co/FmP0S58/coal-hand.png", use_container_width=True)
    st.markdown("<div class='env-value'>21.93 tons</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='env-card'><div class='env-title'>Equivalent Trees Planted</div>", unsafe_allow_html=True)
    # ใช้รูป Green Trees
    st.image("https://i.ibb.co/DfqV8Y8/green-trees.png", use_container_width=True)
    st.markdown("<div class='env-value'>1,507 trees</div></div>", unsafe_allow_html=True)

st.divider()

# --- ส่วนที่ 2: แผนที่และรายละเอียด (2 คอลัมน์) ---
m_left, m_right = st.columns([1.5, 1])

with m_left:
    st.subheader("🌐 ผังโครงข่ายดิจิทัล (Digital Twin)")
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="Zone", size="kW",
                            hover_name="Bldg", zoom=11.2, height=450,
                            color_discrete_map={"Nong Rawiang": "#00A8E8", "Main Campus": "#E85D04"},
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

with m_right:
    st.subheader("📊 ข้อมูลการติดตั้ง")
    st.bar_chart(df.set_index("Bldg")["kW"])
    st.dataframe(df[["Bldg", "kW"]], hide_index=True)

st.divider()
st.caption("RMUTI Smart Grid Platform - Powered by AETHERA")
