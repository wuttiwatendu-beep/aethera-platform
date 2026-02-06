import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np  # เพิ่มเพื่อแก้ Error ในหน้าภาพรวม

# 1. ตั้งค่าหน้าจอและ Sidebar
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")

st.sidebar.title("🏛️ RMUTI AETHERA")
page = st.sidebar.radio("เมนูการใช้งาน", ["สรุปภาพรวมระบบ", "ผังการไหลพลังงาน (Flow)", "P2P Trading"])

# 2. ข้อมูลคงที่ (อ้างอิงจากภาพของคุณนุ)
total_accumulated_mw = 54.473  #
total_capacity_mw = 2854.56    #
co2_saved, coal_saved, trees_planted = 27.24, 21.79, 680 #

# ข้อมูล 10 อาคาร
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
realtime_sum = df_nodes['kW'].sum()

# --- หน้าที่ 1: สรุปภาพรวมระบบ (โทนสว่าง) ---
if page == "สรุปภาพรวมระบบ":
    st.markdown("## 📊 Smart Grid Overview")
    
    # Metric Cards
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Real Time Power", f"{realtime_sum:,.2f} kW")
    with m2: st.metric("Total Production", f"{total_accumulated_mw} MW")
    with m3: st.metric("Total Capacity", f"{total_capacity_mw} MW")
    
    st.write("---")
    
    col_left, col_right = st.columns([1.5, 1])
    with col_left:
        st.markdown("### 📈 Power Generation Trend")
        # สร้างกราฟการผลิตจำลองที่ดูสวยงาม
        chart_data = pd.DataFrame(np.random.normal(realtime_sum, 50, size=(24, 1)), columns=['kW'])
        st.area_chart(chart_data, color="#FFA726")
        
    with col_right:
        st.markdown("### 🌿 Environment Benefits")
        # ใช้ Emoji แทนรูปภาพชั่วคราวเพื่อให้รันได้ทันที
        c1, c2, c3 = st.columns(3)
        with c1: st.write(f"☁️ **CO2**\n{co2_saved} Tons")
        with c2: st.write(f"🪨 **Coal**\n{coal_saved} Tons")
        with c3: st.write(f"🌳 **Trees**\n{trees_planted} Trees")
        
        st.write("---")
        st.markdown("### 📋 Details (10 Stations)")
        st.dataframe(df_nodes[["อาคาร", "kW"]].sort_values("kW", ascending=False), hide_index=True, use_container_width=True)

# --- หน้าที่ 2: ผังการไหลพลังงาน (Zero Export Logic) ---
elif page == "ผังการไหลพลังงาน (Flow)":
    st.markdown("## ⚡ Interactive Energy Flow (Zero Export)")
    
    # Logic: Solar เป็นตัวจ่ายหลัก ถ้าไม่พอค่อยดึง Grid เข้ามาเสริม
    total_load = 3200.0 # สมมติ Load รวมมหาวิทยาลัย
    solar_gen = realtime_sum
    grid_pull = max(0, total_load - solar_gen)
    
    # กราฟิกการไหล (Sankey Diagram)
    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 15, thickness = 20,
          label = ["☀️ Solar PV", "🔌 PEA Grid", "🏛️ RMUTI Load"],
          color = ["#FBC02D", "#E57373", "#0288D1"]
        ),
        link = dict(
          source = [0, 1], # จาก Solar และ Grid
          target = [2, 2], # ไปที่ Load มหาวิทยาลัยอย่างเดียว (ไม่มีย้อนกลับ)
          value = [solar_gen, grid_pull]
      ))])
    
    st.plotly_chart(fig, use_container_width=True)
    st.info(f"💡 ขณะนี้มหาวิทยาลัยใช้พลังงานจากแสงอาทิตย์คิดเป็น { (solar_gen/total_load)*100 :.1f}% ของ Load ทั้งหมด")

# --- หน้าที่ 3: P2P Trading ---
elif page == "P2P Trading":
    st.markdown("## 🤝 P2P Energy Market")
    st.success("ระบบตลาดซื้อขายไฟฟ้าภายในวิทยาเขตศูนย์กลาง")
    st.write("Deal 1: สำนักงานอธิการบดี ⚡ หอประชุมวทัญญูฯ | 12.5 kWh")
