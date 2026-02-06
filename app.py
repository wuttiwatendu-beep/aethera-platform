import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 1. ข้อมูลพื้นฐาน
total_accumulated_mw = 54.473 
total_capacity_mw = 2854.56   
total_accumulated_kwh = total_accumulated_mw * 1000

# คำนวณค่าสิ่งแวดล้อม
co2_saved = total_accumulated_kwh * 0.50 / 1000
coal_saved = total_accumulated_kwh * 0.40 / 1000
trees_planted = int(total_accumulated_kwh / 80)

# ข้อมูลสถานีและ P2P
df_nodes = pd.DataFrame([
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168}
])
realtime_sum = df_nodes['kW'].sum()

# 2. แสดงผลหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid & P2P", layout="wide")
st.markdown("<h2 style='text-align: center;'>🏛️ RMUTI AETHERA: Full Smart Management</h2>", unsafe_allow_html=True)

# Metric Bar
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Real Time Power", f"{realtime_sum:,.2f} kW")
with m2: st.metric("Total Production", f"{total_accumulated_mw:,.3f} MW")
with m3: st.metric("Total Capacity", f"{total_capacity_mw:,.2f} MW")
with m4: st.metric("P2P Volume Today", "80.3 kWh", delta="15%")

st.write("---")

# 3. การจัดวาง Layout 3 ส่วน (ซ้าย-กลาง-ขวา)
col_left, col_mid, col_right = st.columns([1.2, 1, 0.8])

with col_left:
    st.markdown("### 🌐 Digital Twin & P2P Network")
    fig_map = px.scatter_mapbox(df_nodes, lat="Lat", lon="Lon", color="kW", size="kW", zoom=11.5, height=400, mapbox_style="carto-positron")
    st.plotly_chart(fig_map, use_container_width=True)
    
    st.markdown("### 🌿 Environment Benefits")
    e1, e2, e3 = st.columns(3)
    with e1: st.write(f"☁️ CO2: **{co2_saved:,.1f} t**")
    with e2: st.write(f"🪨 Coal: **{coal_saved:,.1f} t**")
    with e3: st.write(f"🌳 Trees: **{trees_planted:,}**")

with col_mid:
    st.markdown("### 📈 Power & Price Trend")
    # รวมกราฟการผลิตและกราฟราคาไว้ใน Tab เพื่อประหยัดพื้นที่
    tab1, tab2 = st.tabs(["Generation", "P2P Price"])
    with tab1:
        hours = [f"{h:02d}:00" for h in range(24)]
        curve = [np.sin(np.pi * (h-7)/10.5) * realtime_sum if 7 <= h <= 17.5 else 0 for h in range(24)]
        st.plotly_chart(px.area(x=hours, y=curve, color_discrete_sequence=['#FF9100'], height=300), use_container_width=True)
    with tab2:
        p_price = [4.5, 4.3, 4.1, 3.8, 3.7, 3.7, 3.9, 4.2, 4.4, 4.5]
        st.plotly_chart(px.line(x=hours[8:18], y=p_price, height=300), use_container_width=True)

with col_right:
    st.markdown("### 🤝 P2P Live Transactions")
    st.caption("Latest deals in Central Campus")
    st.success("Admin ⚡ Conf: 12.5 kWh @ 3.8฿")
    st.success("Bus ⚡ Lib: 25.0 kWh @ 4.0฿")
    
    st.write("---")
    st.markdown("### 📊 Station Details")
    st.dataframe(df_nodes[["อาคาร", "kW"]], hide_index=True, use_container_width=True)
