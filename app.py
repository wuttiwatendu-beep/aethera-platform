import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# CSS สำหรับตกแต่ง Card ให้ดู Professional
st.markdown("""
    <style>
    .env-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border: 1px solid #f0f2f6;
    }
    .env-title { color: #555; font-size: 0.9rem; font-weight: bold; margin-bottom: 10px; }
    .env-value { font-size: 1.5rem; font-weight: bold; color: #E85D04; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร
df = pd.DataFrame([
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160}
])

# --- HEADER ---
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI AETHERA: Executive Dashboard</h2>", unsafe_allow_html=True)

# --- ส่วนที่ 1: Environment Benefits ---
st.markdown("<div style='text-align: center; margin-bottom: 20px;'><span style='background-color: #00A8E8; color: white; padding: 5px 20px; border-radius: 15px; font-weight: bold; font-size: 0.8rem;'>Environment Benefits</span></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# หมายเหตุ: 'co2.png', 'coal.png', 'tree.png' ต้องอยู่บน GitHub ที่เดียวกับไฟล์นี้นะครับ
with col1:
    st.markdown("<div class='env-card'><div class='env-title'>CO2 Emission Saved</div>", unsafe_allow_html=True)
    try: st.image("co2.png", width=100)
    except: st.write("☁️") # ถ้าหารูปไม่เจอจะขึ้น Emoji แทน โค้ดจะไม่พัง
    st.markdown("<div class='env-value'>40.13 tons</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='env-card'><div class='env-title'>Standard Coal Saved</div>", unsafe_allow_html=True)
    try: st.image("coal.png", width=100)
    except: st.write("🪨")
    st.markdown("<div class='env-value'>21.93 tons</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='env-card'><div class='env-title'>Equivalent Trees Planted</div>", unsafe_allow_html=True)
    try: st.image("tree.png", width=100)
    except: st.write("🌳")
    st.markdown("<div class='env-value'>1,507 trees</div></div>", unsafe_allow_html=True)

st.divider()

# --- ส่วนที่ 2: Map & Chart ---
c_left, c_right = st.columns([1.5, 1])

with c_left:
    st.subheader("🌐 Digital Twin Map")
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="Zone", size="kW",
                            zoom=11, height=400, mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

with c_right:
    st.subheader("📊 Generation Details (kW)")
    st.bar_chart(df.set_index("อาคาร")["kW"])
