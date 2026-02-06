import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. การตั้งค่าหน้าจอและสไตล์ (Theme)
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

st.markdown("""
    <style>
    .reportview-container { background: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    h1 { color: #E85D04; font-family: 'Sarabun', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (อ้างอิงตามเอกสารสำรวจของคุณนุ)
data = [
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล (หนองระเวียง)", "kW": 354.56, "Group": "Group 1: หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (อาคาร 35)", "kW": 485.76, "Group": "Group 2: Academic Core", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (อาคาร 32)", "kW": 400.00, "Group": "Group 2: Academic Core", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "สำนักวิทยบริการฯ (อาคาร 4)", "kW": 280.00, "Group": "Group 2: Academic Core", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (อาคาร 2)", "kW": 250.00, "Group": "Group 2: Academic Core", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (อาคาร 1)", "kW": 220.00, "Group": "Group 2: Academic Core", "Lat": 14.9915, "Lon": 102.1160},
    {"อาคาร": "อาคาร A (New)", "kW": 314.24, "Group": "Group 2: Academic Core", "Lat": 14.9935, "Lon": 102.1168},
    {"อาคาร": "อาคาร B (New)", "kW": 300.00, "Group": "Group 2: Academic Core", "Lat": 14.9900, "Lon": 102.1170},
    {"อาคาร": "Sports Complex (Gym)", "kW": 150.00, "Group": "Group 2: Academic Core", "Lat": 14.9940, "Lon": 102.1140},
    {"อาคาร": "อาคารเรียนรวม (อาคาร 7)", "kW": 100.00, "Group": "Group 2: Academic Core", "Lat": 14.9930, "Lon": 102.1145}
]
df = pd.DataFrame(data)

# --- ส่วนที่ 1: Header สำหรับอธิการบดี ---
st.markdown("<h1 style='text-align: center;'>🏛️ RMUTI AETHERA: Smart University Grid</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem;'>โครงการบริหารจัดการพลังงานสะอาด ระยะที่ 1 (เริ่มดำเนินการ มีนาคม 2569)</p>", unsafe_allow_html=True)

# --- ส่วนที่ 2: สรุปผลประโยชน์ (Key Results) ---
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric("กำลังการผลิตติดตั้งรวม", f"{(df['kW'].sum()/1000):.2f} MW", "Phase 1")
col_m2.metric("คาดการณ์การลดค่าไฟ", "4.2 ล้านบาท/ปี", "ROI 4.5 ปี")
col_m3.metric("ลดการปล่อย CO2", "1,240 ตัน/ปี", "เทียบเท่าปลูกต้นไม้ 5หมื่นต้น")
col_m4.metric("จำนวนอาคารที่ติดตั้ง", "10 อาคาร", "2 วิทยาเขต")

st.divider()

# --- ส่วนที่ 3: ผังโครงข่ายและการจัดการ Node (Split Screen) ---
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("🌐 แผนที่โครงข่ายอัจฉริยะ (Real-time Topology)")
    # ใช้ Mapbox Clustering เพื่อให้ดูไม่รก
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="Group", size="kW",
                            hover_name="อาคาร", zoom=11.2, height=550,
                            color_discrete_map={"Group 1: หนองระเวียง": "#00A8E8", "Group 2: Academic Core": "#E85D04"},
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("📊 ข้อมูลเชิงลึกรายอาคาร")
    # ใช้ Tabs แยกข้อมูลเพื่อให้ดูสะอาดตา
    tab1, tab2 = st.tabs(["⚡ ขนาดการติดตั้ง (kW)", "🤝 ระบบ P2P Trading"])
    
    with tab1:
        st.bar_chart(df.set_index('อาคาร')['kW'])
        st.dataframe(df[['อาคาร', 'kW']].sort_values('kW', ascending=False), hide_index=True)
        
    with tab2:
        st.info("จำลองการไหลของพลังงานระหว่างอาคารภายในศูนย์กลางฯ")
        # แสดงสถานะการเทรดแบบ Animation สั้นๆ (ใช้ Table จำลอง)
        trading_data = {
            "จาก (แหล่งผลิต)": ["อาคาร 35", "อาคาร G", "อาคาร 32"],
            "ไปยัง (ผู้ใช้)": ["อธิการบดี", "อาคาร 4", "หอประชุม"],
            "ปริมาณ (kWh)": [45, 120, 60],
            "สถานะ": ["✅ ส่งมอบ", "✅ ส่งมอบ", "🔄 กำลังจับคู่"]
        }
        st.table(pd.DataFrame(trading_data))

st.divider()
st.
