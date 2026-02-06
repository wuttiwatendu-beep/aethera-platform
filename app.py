import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="RMUTI AETHERA | Smart Grid", layout="wide")

# Custom CSS เพื่อความว้าว (Shadow, Border Radius, Font)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    div[data-testid="stImage"] { border-radius: 15px; transition: 0.3s; }
    div[data-testid="stImage"]:hover { transform: scale(1.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. Clean Data (ลบข้อมูลส่วนเกินหนองระเวียงออกแล้ว)
df_stations = pd.DataFrame([
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "Sports Complex", "kW": 200.00, "Zone": "ศูนย์กลาง"}
])

# 3. Header: Premium Glass Metrics
st.markdown("<h1 style='text-align: center; color: #1e3a8a; margin-bottom: 30px;'>🏛️ RMUTI AETHERA PLATFORM</h1>", unsafe_allow_html=True)

top1, top2, top3, top4 = st.columns(4)
with top1: st.metric("Real-Time Solar", "2,854.56 kW", "Active")
with top2: st.metric("Total Yield", "54.473 MW", "Cumulative")
with top3: st.metric("Grid Independence", "85%", "High")
with top4: st.metric("P2P Daily Volume", "80.3 kWh", "15% vs Yesterday")

st.markdown("---")

# 4. Main Dashboard Layout
left_col, right_col = st.columns([1.8, 1])

with left_col:
    # --- ส่วนที่ 1: Energy Flow (Zero Export Mode) ---
    st.subheader("⚡ Smart Energy Flow Control")
    # Sankey แบบมืออาชีพ ระบุหน่วยชัดเจน
    fig_flow = go.Figure(data=[go.Sankey(
        node = dict(pad=25, thickness=20, 
                   label=["Solar PV Source", "PEA Grid Supply", "RMUTI Smart Load"],
                   color=["#fbbf24", "#ef4444", "#1e3a8a"]),
        link = dict(source=[0, 1], target=[2, 2], value=[2854.56, 500],
                   color=["rgba(251, 191, 36, 0.4)", "rgba(239, 68, 68, 0.2)"])
    )])
    fig_flow.update_layout(height=350, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_flow, use_container_width=True)

    # --- ส่วนที่ 2: Power Generation Trend ---
    st.subheader("📈 Generation Performance (kW)")
    # กราฟ Gradient Area แบบโมเดิร์น
    chart_data = pd.DataFrame({"Time": [f"{i}:00" for i in range(24)], "kW": [0,0,0,0,0,100,800,1800,2500,2800,2854,2800,2500,1800,800,100,0,0,0,0,0,0,0,0]})
    fig_trend = px.area(chart_data, x="Time", y="kW", color_discrete_sequence=['#fbbf24'])
    fig_trend.update_layout(height=300, xaxis_title=None, yaxis_title="Power (kW)")
    st.plotly_chart(fig_trend, use_container_width=True)

with right_col:
    # --- ส่วนที่ 3: Environment Card (ใช้รูปคุณนุ) ---
    st.subheader("🌿 ESG Impact")
    e1, e2, e3 = st.columns(3)
    # แสดงรูปภาพที่คุณนุอัปโหลด (CO2, Coal, Tree)
    with e1: st.image("CO2.png"); st.markdown("**27.24 t**<br><small>CO2 Saved</small>", unsafe_allow_html=True)
    with e2: st.image("Coal.png"); st.markdown("**21.79 t**<br><small>Coal Saved</small>", unsafe_allow_html=True)
    with e3: st.image("Tree.png"); st.markdown("**680**<br><small>Trees</small>", unsafe_allow_html=True)

    st.write("")
    
    # --- ส่วนที่ 4: Live P2P Trading Status ---
    st.subheader("🤝 Live Market")
    with st.expander("View Active Trades", expanded=True):
        st.success("✅ Admin → Hall (2) | 12.5 kWh @ 3.8฿")
        st.success("✅ Bus (32) → Lib (4) | 25.0 kWh @ 4.0฿")
    
    # --- ส่วนที่ 5: Station Details (แบบสะอาดตา) ---
    st.subheader("📊 Station Breakdown")
    st.dataframe(df_stations, hide_index=True, use_container_width=True, height=280)

# Footer
st.markdown("<p style='text-align: center; color: gray;'>Designed for RMUTI Smart Campus | Real-time Analytics Enabled</p>", unsafe_allow_html=True)
