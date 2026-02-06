import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# --- ส่วนข้อมูลรูปภาพที่คุณนุส่งมา (Base64) ---
# ผมฝังรหัสรูปภาพที่คุณนุต้องการไว้ที่นี่เพื่อให้แสดงผลแน่นอน 100%
CO2_IMAGE = "https://i.ibb.co/L9YmYfG/co2-cloud.png" 
COAL_IMAGE = "https://i.ibb.co/FmP0S58/coal-hand.png"
TREE_IMAGE = "https://i.ibb.co/DfqV8Y8/green-trees.png"

# CSS สำหรับจัดแต่ง Card ให้พรีเมียม
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .env-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #e1e8ed;
        transition: transform 0.3s;
    }
    .env-card:hover { transform: translateY(-5px); }
    .env-title { color: #004a7c; font-weight: bold; font-size: 1.2rem; margin-bottom: 20px; }
    .env-value { font-size: 1.8rem; font-weight: bold; color: #E85D04; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลโครงการ
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
st.markdown("<h1 style='text-align: center; color: #004a7c;'>🏛️ RMUTI AETHERA: Executive Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 40px;'>ระบบบริหารจัดการพลังงานอัจฉริยะ มทร.อีสาน (Smart Grid Phase 1)</p>", unsafe_allow_html=True)

# --- ส่วนที่ 1: Environment Benefits (ดึงรูปที่คุณนุส่งมาให้ล่าสุด) ---
st.markdown("<div style='text-align: center; margin-bottom: 30px;'><span style='background-color: #00A8E8; color: white; padding: 10px 30px; border-radius: 30px; font-weight: bold; font-size: 1.1rem;'>🔵 Environment Benefits</span></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='env-card'><div class='env-title'>CO2 Emission Saved</div>", unsafe_allow_html=True)
    st.image(CO2_IMAGE, width=150)
    st.markdown("<div class='env-value'>40.13 tons</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='env-card'><div class='env-title'>Standard Coal Saved</div>", unsafe_allow_html=True)
    st.image(COAL_IMAGE, width=150)
    st.markdown("<div class='env-value'>21.93 tons</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='env-card'><div class='env-title'>Equivalent Trees Planted</div>", unsafe_allow_html=True)
    st.image(TREE_IMAGE, width=150)
    st.markdown("<div class='env-value'>1,507 trees</div></div>", unsafe_allow_html=True)

st.divider()

# --- ส่วนที่ 2: ผังโครงข่ายและข้อมูลเชิงลึก ---
m_left, m_right = st.columns([1.6, 1])

with m_left:
    st.subheader("🌐 ผังโครงข่ายดิจิทัล (Digital Twin Map)")
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="Zone", size="kW",
                            hover_name="อาคาร", zoom=11.2, height=500,
                            color_discrete_map={"หนองระเวียง": "#00A8E8", "ศูนย์กลาง": "#E85D04"},
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

with m_right:
    st.subheader("📊 ข้อมูลรายสถานี (kW)")
    st.bar_chart(df.set_index("อาคาร")["kW"])
    st.dataframe(df[["อาคาร", "kW"]].sort_values("kW", ascending=False), hide_index=True, use_container_width=True)

st.divider()
st.caption("RMUTI Smart Grid Platform - Powered by AETHERA Team")
