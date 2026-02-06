import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

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

# 2. ตั้งค่าหน้าจอและ Sidebar
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")
st.sidebar.title("🛠️ Menu Control")
view_mode = st.sidebar.radio("เลือกการแสดงผล", ["ภาพรวม & การผลิต", "ผังการไหลพลังงาน (Flow)", "P2P Trading"])

# 3. ส่วนหัวข้อหลัก (Header)
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Real Time Power", f"{realtime_sum:,.2f} kW")
with m2: st.metric("Total Production", f"{total_accumulated_mw} MW")
with m3: st.metric("Total Capacity", f"{total_capacity_mw} MW")
with m4: st.metric("P2P Volume Today", "80.3 kWh")

st.write("---")

# --- Logic การแสดงผลตามเมนู ---
if view_mode == "ภาพรวม & การผลิต":
    col1, col2 = st.columns([1.6, 1])
    with col1:
        st.markdown("### 📈 Power Generation Trend")
        # กราฟการผลิตแบบที่คุณนุใช้งาน
        chart_data = pd.DataFrame(np.random.normal(realtime_sum, 15, size=(24, 1)), columns=['kW'])
        st.area_chart(chart_data, color="#FFA726", height=320)
        
    with col2:
        st.markdown("### 🌿 Environment Benefits")
        ev1, ev2, ev3 = st.columns(3)
        # แก้ปัญหาไฟล์ภาพหายด้วย Try-Except
        try:
            with ev1: st.image("image_58b625.png", width=70); st.write(f"**{co2_saved} t**")
        except:
            with ev1: st.markdown(f"☁️ **CO2**\n\n**{co2_saved} t**")
        with ev2: st.markdown(f"🪨 **Coal**\n\n**{coal_saved} t**")
        with ev3: st.markdown(f"🌳 **Trees**\n\n**{trees_planted}**")
        
        st.write("---")
        st.markdown("### 📊 Station Details (10 Stations)")
        st.dataframe(df_nodes.sort_values("kW", ascending=False), hide_index=True, height=250)

elif view_mode == "ผังการไหลพลังงาน (Flow)":
    st.markdown("### ⚡ Smart Energy Flow (Zero Export Logic)")
    # Logic: ใช้ PV ก่อน ไม่พอค่อย Grid และไม่มี Feed-out
    load_val = 3200.0
    pv_val = realtime_sum
    grid_val = max(0, load_val - pv_val)
    
    fig = go.Figure(data=[go.Sankey(
        node = dict(pad=15, thickness=20, label=["Solar PV", "PEA Grid", "RMUTI Campus"], color=["gold", "red", "#004a7c"]),
        link = dict(source=[0, 1], target=[2, 2], value=[pv_val, grid_val], color=["rgba(255,215,0,0.4)", "rgba(255,0,0,0.2)"])
    )])
    st.plotly_chart(fig, use_container_width=True)
    st.info(f"💡 ระบบทำงานในโหมด Zero Export: ใช้แสงอาทิตย์ช่วยลดการดึงไฟหลวงได้ { (pv_val/load_val)*100 :.1f}%")

elif view_mode == "P2P Trading":
    st.markdown("### 🤝 P2P Trading Market")
    # รายละเอียดการซื้อขาย
    st.success("Admin (1) ⚡ Conf: 12.5 kWh @ 3.8฿")
    st.success("Bus (32) ⚡ Lib (4): 25.0 kWh @ 4.0฿")
    st.write("---")
    st.markdown("### 🗺️ Digital Twin Map")
    st.map(pd.DataFrame({"lat": [14.9922], "lon": [102.1162]}))
