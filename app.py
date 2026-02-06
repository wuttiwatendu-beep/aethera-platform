import streamlit as st
import pandas as pd
import plotly.express as px

# 1. การตั้งค่าหน้าจอ (Theme สีสว่าง)
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border-top: 5px solid #E85D04;
    }
    h1 { color: #E85D04 !important; font-weight: 800; }
    h3 { color: #334155 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลโครงการ (ยึดตามเอกสารคุณนุ 9+1 Nodes)
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

# --- ส่วนที่ 1: หัวข้อและสรุปตัวเลข (Dashboard Header) ---
st.title("🏛️ RMUTI AETHERA: Smart University Grid")
st.write("ระบบบริหารจัดการพลังงานสะอาด ระยะที่ 1 | เริ่มติดตั้ง มีนาคม 2569")

# Metrics สวยๆ 3 ช่อง
m1, m2, m3 = st.columns(3)
m1.metric("กำลังผลิตรวมศูนย์กลาง", "2.50 MW", "9 อาคารหลัก")
m2.metric("กำลังผลิตหนองระเวียง", "354.56 kW", "อาคารเครื่องกล")
m3.metric("เป้าหมายการประหยัด", "4.2 ล้านบาท/ปี", "ROI 4.5 ปี")

st.divider()

# --- ส่วนที่ 2: การแสดงผลแผนที่และตาราง (Layout 2 ส่วน) ---
left_col, right_col = st.columns([1.5, 1])

with left_col:
    st.subheader("🌐 ผังโครงข่ายดิจิทัล (Digital Twin)")
    # ใช้ Scatter Mapbox แบบสีสว่าง (เสถียรที่สุด)
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="กลุ่ม", size="kW",
                            hover_name="อาคาร", zoom=11.2, height=500,
                            color_discrete_map={"หนองระเวียง": "#00A8E8", "ศูนย์กลาง": "#E85D04"},
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.subheader("📊 ข้อมูลแยกตามจุดติดตั้ง")
    # กราฟแท่งโชว์ศักยภาพรายตึก
    st.bar_chart(df.set_index('อาคาร')['kW'])
    # ตารางรายละเอียดแบบ Clean
    st.dataframe(df[['อาคาร', 'kW']].sort_values(by='kW', ascending=False), 
                 hide_index=True, use_container_width=True)

# --- ส่วนที่ 3: ระบบเทรดจำลอง (P2P Program) ---
st.divider()
st.subheader("🤝 ระบบจำลองการเทรดพลังงาน (Smart P2P Program)")
st.info("จำลองการจับคู่พลังงานส่วนเกินจากแหล่งผลิต (Source) ไปยังอาคารที่มีความต้องการ (Buyer)")

col_t1, col_t2 = st.columns(2)
with col_t1:
    st.success("**Matching Active**")
    trade_df = pd.DataFrame({
        "ผู้ส่งพลังงาน (Seller)": ["อาคาร 35", "อาคาร G", "อาคาร 32"],
        "ผู้รับพลังงาน (Buyer)": ["อธิการบดี", "อาคาร 4", "หอประชุม"],
        "ปริมาณ": ["45.2 kWh", "122.5 kWh", "60.0 kWh"]
    })
    st.table(trade_df)

with col_t2:
    st.write("**สถานะการติดตั้ง (Phase 1)**")
    st.write("📅 เริ่มติดตั้ง: มีนาคม 2569")
    st.write("✅ สำรวจหน้างาน: 100%")
    st.progress(25) # แถบความคืบหน้าโครงการ

st.divider()
st.caption("พัฒนาโดย มทร.อีสาน ร่วมกับ AETHERA Platform")
