import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Page Configuration & Custom Theme
st.set_page_config(page_title="RMUTI AETHERA Platform", layout="wide")

st.markdown("""
    <style>
    .header-box {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    .main-title {
        color: #1e3a8a;
        font-family: 'Inter', sans-serif;
        margin-left: 20px;
        font-weight: 800;
    }
    .stMetric {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border-bottom: 4px solid #f59e0b;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (เหลืออาคาร G หนองระเวียงแห่งเดียวตามสั่ง)
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

# 3. ส่วนหัวพร้อมโลโก้มหาวิทยาลัย
with st.container():
    col_logo, col_title = st.columns([1, 5])
    with col_logo:
        # พยายามโหลดไฟล์ rmut.png ถ้าไม่มีให้ข้ามเพื่อกัน Error
        try:
            st.image("rmut.png", width=120)
        except:
            st.write("🏛️ RMUTI")
    with col_title:
        st.markdown("<h1 class='main-title'>RMUTI AETHERA : Smart Grid Management System</h1>", unsafe_allow_html=True)

# 4. KPI Metrics (ระบุหน่วยชัดเจน)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time Generation", "2,854.56 kW", "☀️ Solar")
m2.metric("Accumulated Yield", "54.473 MW", "Cumulative")
m3.metric("System Capacity", "2,854.56 kW", "Peak")
m4.metric("P2P Volume", "80.3 kWh", "Today")

st.markdown("---")

# 5. Main Content: Flow & ESG & Details
left_col, mid_col, right_col = st.columns([1.5, 1, 1])

with left_col:
    st.subheader("⚡ Energy Flow Visualization (kW)")
    # กราฟแท่งเปรียบเทียบแหล่งพลังงาน (เสถียรกว่า Sankey และดูง่าย)
    fig_flow = go.Figure(data=[
        go.Bar(name='Solar Energy', x=['Load Balance'], y=[2854.56], marker_color='#f59e0b', text="2,854 kW", textposition='auto'),
        go.Bar(name='PEA Grid', x=['Load Balance'], y=[500], marker_color='#ef4444', text="500 kW", textposition='auto')
    ])
    fig_flow.update_layout(barmode='stack', height=400, margin=dict(t=0, b=0), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig_flow, use_container_width=True)
    st.caption("Mode: Zero Export (No power feedback to grid)")

with mid_col:
    st.subheader("🌿 Environment ESG")
    # ใช้รูปที่คุณนุอัปโหลด (CO2, Coal, Tree)
    try:
        st.image("CO2.png", width=100)
        st.write("**27.24 Tons** CO2 Saved")
        st.image("Coal.png", width=100)
        st.write("**21.79 Tons** Coal Saved")
        st.image("Tree.png", width=100)
        st.write("**680 Trees** Planted")
    except:
        st.info("💡 กรุณาตรวจสอบชื่อไฟล์รูปภาพสิ่งแวดล้อม")

with right_col:
    st.subheader("📊 Station Details (kW)")
    st.dataframe(df_stations.sort_values("kW", ascending=False), hide_index=True, use_container_width=True, height=450)

# 6. P2P Transaction Log (ด้านล่างสุด)
st.markdown("---")
st.subheader("🤝 Live P2P Trading History")
c1, c2 = st.columns(2)
with c1: st.success("✅ Admin → Hall (อาคาร 2) : 12.5 kWh | 3.8฿")
with c2: st.success("✅ Business (32) → Lib (4) : 25.0 kWh | 4.0฿")
