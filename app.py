import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. ตั้งค่าหน้าจอ (Wide Mode) เพื่อใช้พื้นที่ให้คุ้มค่าที่สุด
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")

# 2. ข้อมูลอาคารและตัวเลขหลักจากระบบของคุณนุ
total_accumulated_mw = 54.473
total_capacity_mw = 2854.56
co2_val, coal_val, tree_val = 27.24, 21.79, 680

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

# 3. ส่วนหัว (Header) - แสดงค่าหลัก 4 ช่องตลอดเวลา
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real Time Power", f"{df_nodes['kW'].sum():,.2f} kW")
m2.metric("Total Production", f"{total_accumulated_mw} MW")
m3.metric("Total Capacity", f"{total_capacity_mw} MW")
m4.metric("P2P Volume Today", "80.3 kWh")

st.write("---")

# 4. แบ่งเลย์เอาต์หน้าจอเป็น 2 ฝั่งหลัก
col_left, col_right = st.columns([1.5, 1])

with col_left:
    # ฝั่งซ้าย: กราฟการผลิตและแผนที่
    st.markdown("#### 📈 Power Generation Trend")
    chart_data = pd.DataFrame(np.random.normal(2000, 5, size=(24, 1)), columns=['kW'])
    st.area_chart(chart_data, color="#FFA726", height=250)
    
    st.markdown("#### 🗺️ Digital Twin & Energy Flow")
    # ใช้ Sankey Diagram แทนแผนที่ที่โหลดไม่ขึ้น เพื่อแสดงการไหลของไฟ (Zero Export)
    fig = go.Figure(data=[go.Sankey(
        node = dict(pad=15, thickness=20, label=["Solar PV", "PEA Grid", "RMUTI Load"], color=["gold", "red", "#004a7c"]),
        link = dict(source=[0, 1], target=[2, 2], value=[df_nodes['kW'].sum(), 400])
    )])
    fig.update_layout(height=300, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    # ฝั่งขวา: สิ่งแวดล้อม และ รายละเอียดอาคาร
    st.markdown("#### 🌿 Environment Benefits")
    e1, e2, e3 = st.columns(3)
    # แก้ปัญหา "รูปหาย" ด้วยการใช้ CSS ตกแต่งแทนการโหลดไฟล์
    e1.info(f"☁️ CO2\n\n**{co2_val} t**")
    e2.success(f"🪨 Coal\n\n**{coal_val} t**")
    e3.warning(f"🌳 Trees\n\n**{tree_val}**")
    
    st.write("")
    st.markdown("#### 📊 Station Details (10 Stations)")
    st.dataframe(df_nodes.sort_values("kW", ascending=False), hide_index=True, use_container_width=True, height=400)

# 5. แถบ Sidebar สำหรับฟังก์ชันเสริม (เช่น P2P)
if st.sidebar.checkbox("Show Live P2P Transactions"):
    st.toast("Updating P2P Data...")
    st.sidebar.success("Admin ⚡ Conf: 12.5 kWh")
    st.sidebar.success("Bus (32) ⚡ Lib (4): 25.0 kWh")
