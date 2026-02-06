import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# 1. ตั้งค่าพื้นฐาน
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")

# 2. ข้อมูลคงที่จากที่คุณนุอัปโหลด
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

# 3. Sidebar - ใช้สำหรับเปิด/ปิด รายละเอียดเจาะลึก
st.sidebar.title("🛠️ Control Panel")
show_p2p = st.sidebar.checkbox("Show P2P Transactions", value=True)
show_flow = st.sidebar.checkbox("Show Energy Flow Diagram", value=False)

# 4. ส่วนแสดงผลหลัก (Main Dashboard)
st.markdown("<h2 style='text-align: center;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)

# Top Metric Bar
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Real Time Power", f"{realtime_sum:,.2f} kW")
with m2: st.metric("Total Production", f"{total_accumulated_mw} MW")
with m3: st.metric("Total Capacity", f"{total_capacity_mw} MW")
with m4: st.metric("P2P Volume", "80.3 kWh")

st.write("---")

# แถวที่ 1: กราฟการผลิต และ Environment Benefits
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.markdown("### 📈 Power Generation Trend")
    # กราฟการผลิต
    chart_data = pd.DataFrame(np.random.normal(realtime_sum, 20, size=(24, 1)), columns=['kW'])
    st.area_chart(chart_data, color="#FFA726", height=300)

with col_right:
    st.markdown("### 🌿 Environment Benefits")
    # ดึงรูปภาพที่คุณนุอัปโหลดมาแสดง (ตรวจสอบชื่อไฟล์ให้ตรง)
    c1, c2, c3 = st.columns(3)
    with c1: 
        st.image("image_58b625.png", width=80) # หรือใช้ emoji แทนถ้าไฟล์ไม่อยู่: st.write("☁️")
        st.write(f"**{co2_saved} Tons**")
    with c2:
        st.write("🪨") # แทนรูปถ่านหิน
        st.write(f"**{coal_saved} Tons**")
    with c3:
        st.write("🌳") # แทนรูปต้นไม้
        st.write(f"**{trees_planted} Trees**")

st.write("---")

# แถวที่ 2: Energy Flow (ถ้าเปิดใช้งาน) และ Details
if show_flow:
    st.markdown("### ⚡ Smart Energy Flow (Zero Export)")
    # กราฟิกการไหลที่คุณนุชอบ
    fig = go.Figure(data=[go.Sankey(
        node = dict(pad=15, thickness=20, label=["Solar PV", "PEA Grid", "RMUTI Campus"], color=["gold", "red", "blue"]),
        link = dict(source=[0, 1], target=[2, 2], value=[realtime_sum, 500])
    )])
    st.plotly_chart(fig, use_container_width=True)

col_bot_left, col_bot_right = st.columns([1, 1])

with col_bot_left:
    st.markdown("### 📊 Station Details (10 Stations)")
    st.dataframe(df_nodes.sort_values("kW", ascending=False), hide_index=True, use_container_width=True)

with col_bot_right:
    if show_p2p:
        st.markdown("### 🤝 Live P2P Transactions")
        # แสดงรายการซื้อขาย
        st.success("Admin ⚡ Conf: 12.5 kWh @ 3.8฿")
        st.success("Bus (32) ⚡ Lib (4): 25.0 kWh @ 4.0฿")
        st.info("Market Status: **Active**")
