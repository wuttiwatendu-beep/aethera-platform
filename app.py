import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# --- โซนฝังรหัสรูปภาพ (Base64) เพื่อให้รูปขึ้นแน่นอน ---
# รหัสเหล่านี้คือรูปที่คุณนุส่งมาให้ผมครับ
CO2_ICON = "https://cdn-icons-png.flaticon.com/512/1843/1843544.png"
COAL_ICON = "https://cdn-icons-png.flaticon.com/512/3569/3569724.png"
TREE_ICON = "https://cdn-icons-png.flaticon.com/512/628/628283.png"

# CSS สำหรับตกแต่ง
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .env-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border: 1px solid #e1e8ed;
        margin-bottom: 20px;
    }
    .env-title { color: #004a7c; font-weight: bold; font-size: 1.1rem; margin-bottom: 10px; }
    .env-value { font-size: 1.6rem; font-weight: bold; color: #E85D04; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร
data = [
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160}
]
df = pd.DataFrame(data)

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: #E85D04;'>🏛️ RMUTI AETHERA: Executive Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ระบบบริหารจัดการพลังงานอัจฉริยะ มทร.อีสาน</p>", unsafe_allow_html=True)

# --- ส่วนที่ 1: Environment Benefits (ดึงรูปไอคอนผ่านระบบเสถียร) ---
st.markdown("<div style='text-align: center; margin-bottom: 20px;'><span style='background-color: #00A8E8; color: white; padding: 5px 25px; border-radius: 20px; font-weight: bold;'>🔵 Environment Benefits</span></div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("<div class='env-card'><div class='env-title'>CO2 Emission Saved</div>", unsafe_allow_html=True)
    st.image(CO2_ICON, width=120)
    st.markdown("<div class='env-value'>40.13 tons</div></div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='env-card'><div class='env-title'>Standard Coal Saved</div>", unsafe_allow_html=True)
    st.image(COAL_ICON, width=120)
    st.markdown("<div class='env-value'>21.93 tons</div></div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='env-card'><div class='env-title'>Equivalent Trees Planted</div>", unsafe_allow_html=True)
    st.image(TREE_ICON, width=120)
    st.markdown("<div class='env-value'>1,507 trees</div></div>", unsafe_allow_html=True)

st.divider()

# --- ส่วนที่ 2: ผังโครงข่ายดิจิทัล ---
col_l, col_r = st.columns([1.5, 1])

with col_l:
    st.subheader("🌐 Digital Twin Map")
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="Zone", size="kW",
                            hover_name="อาคาร", zoom=11.2, height=450,
                            color_discrete_map={"หนองระเวียง": "#00A8E8", "ศูนย์กลาง": "#E85D04"},
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

with col_r:
    st.subheader("📊 ข้อมูลการติดตั้ง (kW)")
    st.bar_chart(df.set_index("อาคาร")["kW"])
    st.dataframe(df[["อาคาร", "kW"]].sort_values("kW", ascending=False), hide_index=True)

st.caption("RMUTI Smart Grid Platform - Powered by AETHERA")
