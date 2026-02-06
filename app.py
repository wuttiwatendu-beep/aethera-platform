import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. ตั้งค่าหน้าจอ (Wide Mode) เพื่อให้มีพื้นที่วางข้อมูลครบ
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")

# 2. เตรียมข้อมูล (รวมข้อมูลจากทุกแหล่งที่คุณนุให้มา)
total_accumulated_mw = 54.473  #
total_capacity_mw = 2854.56    #
co2_saved, coal_saved, trees_planted = 27.24, 21.79, 680 #

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

# 3. Sidebar Navigation สำหรับสลับโหมด
st.sidebar.title("RMUTI AETHERA")
mode = st.sidebar.radio("เลือกมุมมอง", ["Dashboard หลัก", "ผังการไหลพลังงาน (Flow)"])

# 4. ส่วนหัว (Header Metrics) - มาครบ 4 ค่าหลัก
st.markdown("<h2 style='text-align: center;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real Time Power", f"{df_nodes['kW'].sum():,.2f} kW")
m2.metric("Total Production", f"{total_accumulated_mw} MW")
m3.metric("Total Capacity", f"{total_capacity_mw} MW")
m4.metric("P2P Volume Today", "80.3 kWh")

st.write("---")

# --- โหมดที่ 1: Dashboard หลัก (เน้นข้อมูลครบถ้วน) ---
if mode == "Dashboard หลัก":
    col_left, col_right = st.columns([1.5, 1])
    
    with col_left:
        st.markdown("### 📈 Power Generation Trend")
        # กราฟการผลิตทรงระฆังคว่ำแบบ Solar
        chart_data = pd.DataFrame(np.random.normal(2000, 10, size=(24, 1)), columns=['kW'])
        st.area_chart(chart_data, color="#FFA726", height=300)
        
        st.markdown("### 🗺️ Digital Twin Map")
        st.map(pd.DataFrame({"lat": [14.9922], "lon": [102.1162]}))

    with col_right:
        st.markdown("### 🌿 Environment Benefits")
        ev1, ev2, ev3 = st.columns(3)
        # ใช้ระบบ Try-Except เพื่อกันโปรแกรมล่มหากรูปหาย
        try:
            with ev1: st.image("image_58b625.png", width=70); st.write(f"**{co2_saved} t**")
        except:
            with ev1: st.write(f"☁️ CO2\n**{co2_saved} t**")
        with ev2: st.write(f"🪨 Coal\n**{coal_saved} t**")
        with ev3: st.write(f"🌳 Trees\n**{trees_planted}**")

        st.write("---")
        st.markdown("### 📋 Station Details (10 Stations)")
        # แสดงตาราง 10 อาคารให้ครบถ้วน
        st.dataframe(df_nodes.sort_values("kW", ascending=False), hide_index=True, use_container_width=True)

# --- โหมดที่ 2: ผังการไหลพลังงาน (Zero Export) ---
elif mode == "ผังการไหลพลังงาน (Flow)":
    st.markdown("### ⚡ Energy Flow Visualization")
    # ผังการไหลแบบที่คุณนุต้องการ (Solar + Grid เข้ามหาลัย)
    fig = go.Figure(data=[go.Sankey(
        node = dict(pad=15, thickness=20, label=["Solar PV", "PEA Grid", "RMUTI Load"], color=["gold", "red", "#004a7c"]),
        link = dict(source=[0, 1], target=[2, 2], value=[df_nodes['kW'].sum(), 500])
    )])
    st.plotly_chart(fig, use_container_width=True)
    st.info("ระบบจำกัดการไหลออก (Zero Export): พลังงานถูกใช้ภายในวิทยาเขตทั้งหมด")
