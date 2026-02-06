import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. ตั้งค่าหน้าจอแบบ Wide และใส่ CSS สำหรับ Animation
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    .status-live { color: #00ff00; animation: pulse 2s infinite; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (Master Data 9+1)
data = [
    {"Bldg": "อาคาร G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "Nong Rawiang", "Lat": 14.9435, "Lon": 102.2140},
    {"Bldg": "สำนักส่งเสริมวิชาการฯ (อาคาร 35)", "kW": 485.76, "Zone": "Main Campus", "Lat": 14.9922, "Lon": 102.1162},
    {"Bldg": "คณะบริหารธุรกิจ (อาคาร 32)", "kW": 400.00, "Zone": "Main Campus", "Lat": 14.9925, "Lon": 102.1155},
    {"Bldg": "อาคารสำนักวิทยบริการฯ (อาคาร 4)", "kW": 280.00, "Zone": "Main Campus", "Lat": 14.9910, "Lon": 102.1165},
    {"Bldg": "หอประชุมวทัญญูฯ (อาคาร 2)", "kW": 250.00, "Zone": "Main Campus", "Lat": 14.9905, "Lon": 102.1158},
    {"Bldg": "อาคารสำนักงานอธิการบดี (อาคาร 1)", "kW": 220.00, "Zone": "Main Campus", "Lat": 14.9915, "Lon": 102.1160},
    {"Bldg": "อาคาร A (Temporary)", "kW": 314.24, "Zone": "Main Campus", "Lat": 14.9935, "Lon": 102.1168},
    {"Bldg": "อาคาร B (Temporary)", "kW": 300.00, "Zone": "Main Campus", "Lat": 14.9900, "Lon": 102.1170},
    {"Bldg": "Sports Complex (Gym)", "kW": 150.00, "Zone": "Main Campus", "Lat": 14.9940, "Lon": 102.1140},
    {"Bldg": "อาคารเรียนรวม (อาคาร 7)", "kW": 100.00, "Zone": "Main Campus", "Lat": 14.9930, "Lon": 102.1145}
]
df = pd.DataFrame(data)

# --- HEADER ---
st.title("🏛️ RMUTI AETHERA: Executive Dashboard")
st.write("ระบบบริหารจัดการพลังงานอัจฉริยะ มทร.อีสาน (Phase 1: มีนาคม 2569)")

# --- KPI METRICS (ส่วนที่อธิการบดีชอบ) ---
m1, m2, m3 = st.columns(3)
m1.metric("กำลังผลิตติดตั้งรวม", f"{df['kW'].sum()/1000:.2f} MW")
m2.metric("ลดการปล่อยก๊าซเรือนกระจก", "1,240 tCO2/y")
m3.metric("สถานะระบบ", "ACTIVE", delta="Normal", delta_color="normal")

st.divider()

# --- SPLIT SCREEN (แผนที่ | ข้อมูล) ---
col_map, col_detail = st.columns([1.5, 1])

with col_map:
    st.subheader("🌐 Network Topology")
    # ใช้ Scatter Mapbox พร้อม Clustering เพื่อไม่ให้รกตา
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="Zone", size="kW",
                            hover_name="Bldg", zoom=11.2, height=550,
                            color_discrete_map={"Nong Rawiang": "#00A8E8", "Main Campus": "#E85D04"},
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

with col_detail:
    st.subheader("⚡ Live Power Generation")
    # ใช้ Expander เพื่อจัดกลุ่มอาคาร ไม่ให้รกตา
    for zone in ["Main Campus", "Nong Rawiang"]:
        with st.expander(f"📍 {zone} Nodes", expanded=(zone == "Nong Rawiang")):
            zone_df = df[df['Zone'] == zone]
            for _, row in zone_df.iterrows():
                c1, c2 = st.columns([2, 1])
                c1.write(f"**{row['Bldg']}**")
                c2.markdown(f"<span class='status-live'>●</span> {row['kW']} kW", unsafe_allow_html=True)
                st.progress(np.random.randint(40, 90)) # Animation จำลองการผลิตไฟ

st.divider()
st.info("💡 Tip: คุณนุสามารถเลื่อนเมาส์ไปที่จุดบนแผนที่เพื่อดูรายละเอียดแต่ละอาคารได้ครับ")
