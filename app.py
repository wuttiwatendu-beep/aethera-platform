import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. ข้อมูลพื้นฐาน (อ้างอิงจากภาพของคุณนุ)
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
realtime_sum = df_nodes['kW'].sum()

# 2. Sidebar Navigation
st.sidebar.title("RMUTI AETHERA")
page = st.sidebar.radio("เมนูหลัก", ["ภาพรวมระบบ", "P2P Trading", "ผังการไหลพลังงาน (Flow)"])

# --- หน้าที่ 1: ภาพรวมระบบ ---
if page == "ภาพรวมระบบ":
    st.markdown("## 🏛️ Smart Grid Overview")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Real Time Power", f"{realtime_sum:,.2f} kW")
    with m2: st.metric("Total Production", f"{total_accumulated_mw} MW")
    with m3: st.metric("Total Capacity", f"{total_capacity_mw} MW")
    
    st.write("---")
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("### 📈 Power Generation Trend")
        # กราฟเส้นแสดงการผลิต
        st.area_chart(pd.DataFrame(np.random.randn(20, 1), columns=['kW'])) 
    with col2:
        st.markdown("### 🌿 Environment Benefits")
        st.write(f"☁️ CO2 Saved: **{co2_saved} Tons**")
        st.write(f"🪨 Coal Saved: **{coal_saved} Tons**")
        st.write(f"🌳 Trees: **{trees_planted} Trees**")
        st.markdown("### 📊 รายละเอียด 10 อาคาร")
        st.dataframe(df_nodes[["อาคาร", "kW"]], hide_index=True)

# --- หน้าที่ 3: Smart Energy Flow (Zero Export Logic) ---
elif page == "ผังการไหลพลังงาน (Flow)":
    st.markdown("## ⚡ Smart Energy Flow (Zero Export)")
    
    # คำนวณ Logic: Solar เป็นหลัก ถ้าไม่พอค่อยดึง Grid
    current_load = 3100.0 # สมมติ Load มหาวิทยาลัย
    solar_gen = realtime_sum
    grid_pull = current_load - solar_gen if current_load > solar_gen else 0
    
    # สร้าง Sankey Diagram
    fig = go.Figure(data=[go.Sankey(
        node = dict(pad=15, thickness=20, label=["Solar PV", "PEA Grid", "RMUTI Load"], color=["gold", "red", "blue"]),
        link = dict(source=[0, 1], target=[2, 2], value=[solar_gen, grid_pull])
    )])
    
    st.plotly_chart(fig, use_container_width=True)
    st.success(f"สถานะ: ใช้ไฟจาก Solar { (solar_gen/current_load)*100 :.1f}% | ไม่มีการจ่ายไฟออกนอกระบบ")

# (หน้า P2P Trading สามารถเพิ่ม Code เดิมลงไปได้ที่นี่)
