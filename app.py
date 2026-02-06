import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")

# 2. ข้อมูลอาคาร (ลบอาคารหนองระเวียงส่วนเกินออกตามสั่ง)
df_stations = pd.DataFrame([
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"}, # เหลืออาคารเดียวตามสั่ง
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "Sports Complex", "kW": 200.00, "Zone": "ศูนย์กลาง"},
])

# ตัวเลข Metric หลัก
solar_now = 2854.56  #
grid_now = 500.0
total_load = solar_now + grid_now

# 3. Header Metrics (ใส่หน่วยชัดเจน)
st.markdown("<h2 style='text-align: center; color: #01579b;'>🏛️ RMUTI Smart Grid Management</h2>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real Time Power", f"{solar_now:,.2f} kW")
m2.metric("Total Production", "54.473 MW")
m3.metric("Total Capacity", "2,854.56 MW")
m4.metric("P2P Volume Today", "80.3 kWh")

st.write("---")

# 4. Layout ส่วนกลาง: Energy Flow และ Environment
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.markdown("### ⚡ Energy Flow Diagram (kW) - Zero Export Mode")
    # ปรับปรุง Sankey ให้ดูง่าย มีระบุหน่วยชัดเจน
    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 40, thickness = 20,
          label = [f"☀️ Solar PV\n({solar_now:,.0f} kW)", 
                   f"🔌 PEA Grid\n({grid_now:,.0f} kW)", 
                   f"🏫 RMUTI Load\n({total_load:,.0f} kW)"],
          color = ["#FFD700", "#FF4B4B", "#004A7C"]
        ),
        link = dict(
          source = [0, 1], target = [2, 2],
          value = [solar_now, grid_now],
          color = ["rgba(255, 215, 0, 0.4)", "rgba(255, 75, 75, 0.3)"]
      ))])
    fig.update_layout(height=400, font_size=16)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("### 🌿 Environment Benefits")
    # เปลี่ยนมาใช้รูปภาพที่คุณนุอัปโหลดไว้
    e1, e2, e3 = st.columns(3)
    with e1:
        st.image("CO2.png", caption="CO2 Saved")
        st.markdown("<h4 style='text-align: center;'>27.24 t</h4>", unsafe_allow_html=True)
    with e2:
        st.image("Coal.png", caption="Coal Saved")
        st.markdown("<h4 style='text-align: center;'>21.79 t</h4>", unsafe_allow_html=True)
    with e3:
        st.image("Tree.png", caption="Trees Planted")
        st.markdown("<h4 style='text-align: center;'>680</h4>", unsafe_allow_html=True)

st.write("---")

# 5. ส่วนล่าง: กราฟ Trend และ ตาราง Station
c_trend, c_table = st.columns([1, 1])

with c_trend:
    st.markdown("### 📈 Power Generation Trend (kW)")
    # กราฟระบุแกนชัดเจน
    trend_data = pd.DataFrame({"Hour": range(24), "Power (kW)": np.random.normal(2000, 10, 24)})
    st.line_chart(trend_data.set_index("Hour"), color="#FF9800")

with c_table:
    st.markdown("### 📊 Station Details (10 Stations)")
    # ตารางที่ผ่านการกรองข้อมูลหนองระเวียงแล้ว
    st.dataframe(df_stations, hide_index=True, use_container_width=True, height=300)
