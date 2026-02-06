import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI AETHERA Pro", layout="wide")

# --- CSS ตกแต่งให้เหมือน Dashboard ระดับอุตสาหกรรม ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f5; }
    .stApp { margin-top: -50px; }
    .metric-box {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border-left: 6px solid #004a7c;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .metric-label { font-size: 0.9rem; color: #555; font-weight: bold; }
    .metric-value { font-size: 1.6rem; color: #004a7c; font-weight: 800; }
    .env-box {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #e1e8ed;
    }
    .env-val { color: #E85D04; font-weight: bold; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลจำลอง (Simulated Data)
# ข้อมูลอาคาร
df_nodes = pd.DataFrame([
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "อาคาร A", "kW": 314.24, "Zone": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168},
    {"อาคาร": "อาคาร B", "kW": 300.00, "Zone": "ศูนย์กลาง", "Lat": 14.9900, "Lon": 102.1170}
])

# ข้อมูลกราฟเส้น (24 ชม. ล่าสุด)
times = [(datetime.now() - timedelta(hours=i)).strftime("%H:%M") for i in range(24)][::-1]
power_values = [30 + (20 * np.sin(i/3)) + np.random.normal(0, 2) for i in range(24)]
df_graph = pd.DataFrame({"Time": times, "Power (kW)": power_values})

# --- HEADER ---
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI AETHERA: Smart Grid Dashboard</h2>", unsafe_allow_html=True)

# --- ส่วนที่ 1: Top Metrics (ตามรูปที่คุณนุส่งมา) ---
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(f"""<div class='metric-box'><div><div class='metric-label'>Real Time Power</div><div class='metric-value'>35.926 kW</div></div><div style='font-size: 2.5rem;'>⚡</div></div>""", unsafe_allow_html=True)
with m2:
    st.markdown(f"""<div class='metric-box'><div><div class='metric-label'>Total Production</div><div class='metric-value'>54.473 MW</div></div><div style='font-size: 2.5rem;'>🔋</div></div>""", unsafe_allow_html=True)
with m3:
    st.markdown(f"""<div class='metric-box'><div><div class='metric-label'>Total Capacity</div><div class='metric-value'>313.86 kW</div></div><div style='font-size: 2.5rem;'>🏢</div></div>""", unsafe_allow_html=True)

st.write("")

# --- ส่วนที่ 2: การจัดวาง Grid ใหญ่ (ซ้าย-ขวา) ---
col_left, col_right = st.columns([1.8, 1])

with col_left:
    # กราฟ Real-time (Area Chart)
    st.markdown("### 📈 Power Generation Trend (24h)")
    fig_line = px.area(df_graph, x="Time", y="Power (kW)", color_discrete_sequence=['#00A8E8'])
    fig_line.update_layout(height=280, margin=dict(l=0, r=0, t=0, b=0), xaxis_title=None)
    st.plotly_chart(fig_line, use_container_width=True)
    
    # แผนที่ Digital Twin
    st.markdown("### 🌐 Digital Twin Map")
    fig_map = px.scatter_mapbox(df_nodes, lat="Lat", lon="Lon", color="Zone", size="kW",
                                zoom=11.5, height=300, mapbox_style="carto-positron")
    fig_map.update_layout(margin=dict(l=0, r=0, t=0, b=0), showlegend=False)
    st.plotly_chart(fig_map, use_container_width=True)

with col_right:
    # Environment Benefits (แบบ Compact)
    st.markdown("### 🌿 Environment")
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown("<div class='env-box'>", unsafe_allow_html=True)
        st.image("CO2.png", use_container_width=True)
        st.markdown("<div class='env-val'>40.1 t</div></div>", unsafe_allow_html=True)
    with e2:
        st.markdown("<div class='env-box'>", unsafe_allow_html=True)
        st.image("Coal.png", use_container_width=True)
        st.markdown("<div class='env-val'>21.9 t</div></div>", unsafe_allow_html=True)
    with e3:
        st.markdown("<div class='env-box'>", unsafe_allow_html=True)
        st.image("Tree.png", use_container_width=True)
        st.markdown("<div class='env-val'>1,507</div></div>", unsafe_allow_html=True)
    
    # ตารางข้อมูลสถานี
    st.write("")
    st.markdown("### 📊 Station Details")
    st.dataframe(df_nodes[["อาคาร", "kW"]].sort_values("kW", ascending=False), 
                 hide_index=True, use_container_width=True, height=430)

st.caption("RMUTI Smart Grid Live Dashboard | Powered by AETHERA")
