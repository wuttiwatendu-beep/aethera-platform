import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go # สำหรับทำ Sankey Diagram (Energy Flow)

# 1. ตั้งค่า Page และ Sidebar
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")

# สร้าง Sidebar สำหรับเลือกหน้า
st.sidebar.image("https://www.rmuti.ac.th/main/wp-content/uploads/2019/11/logo-rmuti-1.png", width=100)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard Overview", "P2P Trading", "Smart Energy Flow"])

# 2. ข้อมูลอาคาร (9-10 อาคารที่คุณนุต้องการให้เห็นครบ)
df_nodes = pd.DataFrame([
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "Sports Complex", "kW": 200.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "อาคารปฏิบัติการไฟฟ้า", "kW": 180.00, "Zone": "หนองระเวียง"},
    {"อาคาร": "โรงอาหารหนองระเวียง", "kW": 170.00, "Zone": "หนองระเวียง"}
])

# --- หน้าที่ 1: Dashboard Overview (อ้างอิงจาก image_58c223.png) ---
if page == "Dashboard Overview":
    st.markdown("## 🏛️ RMUTI Smart Grid Overview")
    # (โค้ดส่วน Metric และ Environment Benefits ที่คุณนุใช้ล่าสุด)
    st.info("หน้านี้แสดงภาพรวม 10 อาคาร และค่า CO2/Trees/Coal")

# --- หน้าที่ 2: P2P Trading (อ้างอิงจาก image_591b9b.png) ---
elif page == "P2P Trading":
    st.markdown("## 🤝 Peer-to-Peer Energy Market")
    # (โค้ดส่วนตารางซื้อขายและกราฟราคา Market Price)
    st.success("หน้านี้สำหรับบริหารจัดการการซื้อขายไฟระหว่างอาคารในศูนย์กลาง")

# --- หน้าที่ 3: Smart Energy Flow (หน้าใหม่ที่คุณนุต้องการ) ---
elif page == "Smart Energy Flow":
    st.markdown("## ⚡ Interactive Energy Flow (Solar vs Grid)")
    
    # ทำ Sankey Diagram แสดงการไหลของไฟ
    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 15, thickness = 20,
          label = ["Solar Rooftop", "PEA Grid", "Main Transformer", "Central Campus", "Nong Rawiang"],
          color = ["#FFD700", "#FF4B4B", "#333333", "#004a7c", "#004a7c"]
        ),
        link = dict(
          source = [0, 1, 2, 2], # แหล่งจ่าย (Solar, Grid -> Transformer -> Campus)
          target = [2, 2, 3, 4], 
          value = [2854, 1200, 2500, 1554] # ปริมาณ kW ที่ไหล
      ))])
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    **คำอธิบายกราฟิก:**
    * เส้นสีเหลืองแทนพลังงานจาก **Solar Rooftop**
    * เส้นสีแดงแทนการรับไฟจาก **การไฟฟ้า (PEA Grid)**
    * ความหนาของเส้นแสดงปริมาณพลังงาน (kW) ที่ใช้งานจริงในแต่ละโซน
    """)
