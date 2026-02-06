import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Setup & Data
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")

# ข้อมูลจากระบบของคุณนุ
total_capacity_kw = 2854.56
solar_gen_now = 2854.56  # สมมติผลิตได้เต็มที่
pea_grid_now = 500.0     # ดึงไฟหลวงมาช่วย
total_load = solar_gen_now + pea_grid_now

# ข้อมูล 10 อาคาร
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

# 2. Header Metrics (ระบุหน่วยทุกตัว)
st.markdown("<h2 style='text-align: center;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real Time Power", f"{solar_gen_now:,.2f} kW")
m2.metric("Total Production", "54.473 MW")
m3.metric("Total Capacity", f"{total_capacity_kw:,.2f} MW")
m4.metric("P2P Volume Today", "80.3 kWh")

st.write("---")

# 3. Layout: Energy Flow (แบบเข้าใจง่าย) และ Environment
col_flow, col_env = st.columns([1.5, 1])

with col_flow:
    st.markdown("### ⚡ Energy Flow Diagram (Zero Export Mode)")
    # สร้าง Sankey Diagram ที่เน้นการไหลจากแหล่งจ่ายไปที่ Load
    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 30, thickness = 30,
          label = [f"☀️ Solar PV ({solar_gen_now:,.0f} kW)", 
                   f"🔌 PEA Grid ({pea_grid_now:,.0f} kW)", 
                   f"🏫 RMUTI Total Load ({total_load:,.0f} kW)"],
          color = ["#FBC02D", "#E57373", "#0288D1"]
        ),
        link = dict(
          source = [0, 1], # จาก Solar และ Grid
          target = [2, 2], # ไปที่ Load มหาวิทยาลัยอย่างเดียว
          value = [solar_gen_now, pea_grid_now],
          color = ["rgba(251, 192, 45, 0.4)", "rgba(229, 115, 115, 0.4)"]
      ))])
    
    fig.update_layout(height=400, font_size=14, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)
    st.caption("หมายเหตุ: ระบบทำงานแบบ Zero Export ไม่มีการไหลย้อนกลับสู่การไฟฟ้า (PEA)")

with col_env:
    st.markdown("### 🌿 Environment Benefits")
    # แสดงรูปภาพที่คุณนุอัปโหลดไว้
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("CO2.png", use_container_width=True)
        st.markdown(f"<p style='text-align:center'><b>27.24 Tons</b><br><small>CO2 Saved</small></p>", unsafe_allow_html=True)
    with c2:
        st.image("Coal.png", use_container_width=True)
        st.markdown(f"<p style='text-align:center'><b>21.79 Tons</b><br><small>Coal Saved</small></p>", unsafe_allow_html=True)
    with c3:
        st.image("Tree.png", use_container_width=True)
        st.markdown(f"<p style='text-align:center'><b>680 Trees</b><br><small>Planted</small></p>", unsafe_allow_html=True)

st.write("---")

# 4. Power Trend และ Station Details
col_trend, col_table = st.columns([1, 1])

with col_trend:
    st.markdown("### 📈 Power Generation Trend (kW)")
    # กราฟแกน X เป็นเวลา แกน Y เป็น kW
    hours = [f"{h:02d}:00" for h in range(24)]
    gen_data = [np.sin(np.pi * (h-7)/10.5) * solar_gen_now if 7 <= h <= 17.5 else 0 for h in range(24)]
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=hours, y=gen_data, fill='tozeroy', line_color='#FFA726', name='Solar (kW)'))
    fig_line.update_layout(xaxis_title="Time (Hour)", yaxis_title="Power (kW)", height=350)
    st.plotly_chart(fig_line, use_container_width=True)

with col_table:
    st.markdown("### 📊 Station Details (kW)")
    st.dataframe(df_stations.sort_values("kW", ascending=False), hide_index=True, use_container_width=True, height=350)
