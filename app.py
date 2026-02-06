import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. ตั้งค่าหน้าจอแบบเต็มความกว้าง
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")

# 2. ข้อมูลอาคารทั้ง 10 แห่งและตัวเลขสถิติเดิม (ล็อคค่าตามไฟล์ภาพ)
total_accumulated_mw = 54.473
total_capacity_mw = 2854.56
co2_val, coal_val, tree_val = 27.24, 21.79, 680

df_stations = pd.DataFrame([
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

# 3. ส่วนหัว (Header Metrics) มาครบ 4 ค่าหลัก
st.markdown("<h2 style='text-align: center; color: #01579b;'>🏛️ RMUTI Smart Grid & P2P Management</h2>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real Time Power", "2,854.56 kW")
m2.metric("Total Production", f"{total_accumulated_mw} MW")
m3.metric("Total Capacity", f"{total_capacity_mw} MW")
m4.metric("P2P Volume Today", "80.3 kWh", delta="15% vs Yesterday")

st.write("---")

# 4. การจัดวางข้อมูลแบบ 3 คอลัมน์ (เพื่อให้เห็นครบทุกส่วนในระนาบเดียว)
col_graph, col_env, col_table = st.columns([1.2, 0.8, 1.2])

with col_graph:
    st.markdown("#### 📈 Power Generation Trend")
    # กราฟการผลิตแบบเดิม
    chart_data = pd.DataFrame(np.random.normal(2000, 10, size=(24, 1)), columns=['kW'])
    st.area_chart(chart_data, color="#ff9800", height=250)
    
    st.markdown("#### ⚡ Energy Flow (Zero Export)")
    # แสดงการไหลของไฟ PV + Grid เข้าสู่ Load
    fig = go.Figure(data=[go.Sankey(
        node = dict(pad=10, thickness=15, label=["PV", "Grid", "RMUTI"], color=["gold", "red", "#01579b"]),
        link = dict(source=[0, 1], target=[2, 2], value=[2854, 450])
    )])
    fig.update_layout(height=180, margin=dict(l=5, r=5, t=5, b=5))
    st.plotly_chart(fig, use_container_width=True)

with col_env:
    st.markdown("#### 🌿 Environment Benefits")
    # ปรับรูปแบบการแสดงผล CO2/Coal/Trees ให้ชัดเจน
    st.info(f"☁️ **CO2 Saved**\n\n{co2_val} Tons")
    st.success(f"🪨 **Coal Saved**\n\n{coal_val} Tons")
    st.warning(f"🌳 **Trees Planted**\n\n{tree_val} Trees")
    
    st.write("---")
    st.markdown("#### 🤝 Live P2P Status")
    # ข้อมูลการเทรดเดิม
    st.write("✅ Admin ⚡ Conf: 12.5 kWh")
    st.write("✅ Bus (32) ⚡ Lib (4): 25.0 kWh")

with col_table:
    st.markdown("#### 📋 Station Details (10 Stations)")
    # แสดงตารางข้อมูลอาคารให้ครบและกว้างขึ้น
    st.dataframe(df_stations.sort_values("kW", ascending=False), 
                 hide_index=True, use_container_width=True, height=480)

# 5. ฟังก์ชันเสริม Digital Twin Map ในแถบ Sidebar
if st.sidebar.checkbox("เปิดแผนที่ Digital Twin Map"):
    st.markdown("#### 🗺️ Digital Twin Network")
    st.map(pd.DataFrame({"lat": [14.9922], "lon": [102.1162]}))
