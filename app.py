import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าจอแบบ Wide และปรับแต่ง Theme เบื้องต้น
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# --- CSS ตกแต่งให้ข้อมูลอ่านง่ายและชัดเจน ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .metric-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        border-top: 5px solid #004a7c;
        text-align: center;
    }
    .metric-title { color: #555; font-size: 0.9rem; margin-bottom: 5px; font-weight: bold; }
    .metric-value { color: #E85D04; font-size: 1.6rem; font-weight: bold; }
    .stDataFrame { background-color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (Data) - ตรวจสอบว่ามีข้อมูลครบถ้วน
df = pd.DataFrame([
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160},
    {"อาคาร": "Sports Complex", "kW": 150.00, "Zone": "ศูนย์กลาง", "Lat": 14.9940, "Lon": 102.1140},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 100.00, "Zone": "ศูนย์กลาง", "Lat": 14.9930, "Lon": 102.1145},
    {"อาคาร": "อาคาร A", "kW": 314.24, "Zone": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168},
    {"อาคาร": "อาคาร B", "kW": 300.00, "Zone": "ศูนย์กลาง", "Lat": 14.9900, "Lon": 102.1170}
])

total_kw = df['kW'].sum()

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: #004a7c;'>🏛️ RMUTI AETHERA: Executive Dashboard</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size: 1.2rem;'>Total Installed Capacity: <b>{total_kw:,.2f} kW</b></p>", unsafe_allow_html=True)

st.write("---")

# --- การจัดวาง (Layout) ---
# แถวที่ 1: Environment Metrics (รูปที่คุณนุส่งมา + ตัวเลขชัดๆ)
col_e1, col_e2, col_e3 = st.columns(3)

with col_e1:
    st.markdown("<div class='metric-card'><div class='metric-title'>CO2 Emission Saved</div>", unsafe_allow_html=True)
    st.image("CO2.png", width=80)
    st.markdown("<div class='metric-value'>40.13 tons</div></div>", unsafe_allow_html=True)

with col_e2:
    st.markdown("<div class='metric-card'><div class='metric-title'>Standard Coal Saved</div>", unsafe_allow_html=True)
    st.image("Coal.png", width=80)
    st.markdown("<div class='metric-value'>21.93 tons</div></div>", unsafe_allow_html=True)

with col_e3:
    st.markdown("<div class='metric-card'><div class='metric-title'>Equivalent Trees Planted</div>", unsafe_allow_html=True)
    st.image("Tree.png", width=80)
    st.markdown("<div class='metric-value'>1,507 trees</div></div>", unsafe_allow_html=True)

st.write("")

# แถวที่ 2: แผนที่ (ซ้าย) และ ตารางข้อมูล (ขวา) เพื่อให้เห็นข้อมูลอาคารชัดเจน
col_left, col_right = st.columns([1.8, 1])

with col_left:
    st.subheader("🌐 Digital Twin: Node Locations")
    fig = px.scatter_mapbox(
        df, lat="Lat", lon="Lon", 
        color="Zone", 
        size="kW",
        hover_name="อาคาร",
        zoom=11.2,
        height=450,
        color_discrete_map={"หนองระเวียง": "#00A8E8", "ศูนย์กลาง": "#E85D04"},
        mapbox_style="carto-positron"
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("📊 Station Details (kW)")
    # แสดงตารางข้อมูลให้เห็นชัดๆ
    st.dataframe(
        df[["อาคาร", "kW", "Zone"]].sort_values("kW", ascending=False),
        hide_index=True,
        use_container_width=True,
        height=400
    )

st.divider()
st.caption("RMUTI Smart Grid Platform | Updated 2026")
