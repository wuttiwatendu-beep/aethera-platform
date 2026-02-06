import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# CSS แบบง่าย ป้องกัน Error ตอนวาง
st.markdown("<style>.main {background-color: #f8fafc;} .stMetric {border-top: 5px solid #E85D04;}</style>", unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (9+1 Nodes)
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

# --- HEADER ---
st.title("🏫 RMUTI AETHERA: Smart University Grid")
st.write("ระบบบริหารจัดการพลังงาน Phase 1 (มีนาคม 2569)")

# --- ส่วนที่ 1: Environment Benefits (ใส่ไอคอนแบบใช้ฟังก์ชันมาตรฐานของ Streamlit เพื่อความเสถียร) ---
st.subheader("🔵 Environment Benefits")
e1, e2, e3 = st.columns(3)

with e1:
    st.image("https://cdn-icons-png.flaticon.com/512/1843/1843544.png", width=60)
    st.metric("CO2 Emission Saved", "40.13 tons", delta="Target met")

with e2:
    st.image("https://cdn-icons-png.flaticon.com/512/3569/3569724.png", width=60)
    st.metric("Standard Coal Saved", "21.93 tons", delta="Resource saving")

with e3:
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=60)
    st.metric("Equivalent Trees Planted", "1,507 trees", delta="Green project")

st.divider()

# --- ส่วนที่ 2: แผนที่และกราฟ ---
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("🌐 Digital Twin Map")
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="Zone", size="kW",
                            hover_name="Bldg", zoom=11, height=450,
                            color_discrete_map={"Nong Rawiang": "#00A8E8", "Main Campus": "#E85D04"},
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("📊 Generation Details")
    st.bar_chart(df.set_index("Bldg")["kW"])
    st.dataframe(df[["Bldg", "kW"]].sort_values("kW", ascending=False), hide_index=True)

# --- ส่วนที่ 3: P2P Trading ---
st.divider()
st.subheader("🤝 Smart P2P Trading (Simulation)")
t_col1, t_col2 = st.columns(2)
with t_col1:
    st.table(pd.DataFrame({
        "Seller": ["อาคาร 35", "อาคาร G", "อาคาร 32"],
        "Buyer": ["อธิการบดี", "อาคาร 4", "หอประชุม"],
        "Amount": ["45.2 kWh", "122.5 kWh", "60.0 kWh"]
    }))
with t_col2:
    st.success("ROI Estimation: 4.5 Years")
    st.write("Current Status: Surveying")
    st.progress(25)

st.caption("RMUTI Smart Grid Platform by AETHERA")
