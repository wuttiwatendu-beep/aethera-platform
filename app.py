import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration & Ultra-Large UI CSS
st.set_page_config(page_title="RMUTI AETHERA | Analytics", layout="wide")

st.markdown("""
    <style>
    /* ขยายขนาดฟอนต์โดยรวม */
    [data-testid="stMetricValue"] { font-size: 3.8rem !important; font-weight: 800 !important; color: #1e3a8a; }
    [data-testid="stMetricLabel"] { font-size: 1.4rem !important; font-weight: 600 !important; }
    
    /* ปรับแต่งหัวข้อส่วนล่างให้เด่นชัด (Section Headers) */
    .section-header {
        font-size: 2.2rem !important;
        font-weight: 700;
        color: #1e3a8a;
        border-left: 8px solid #f59e0b;
        padding-left: 15px;
        margin-bottom: 20px;
    }
    
    /* ขยายขนาดตาราง */
    .stTable { font-size: 1.4rem !important; }
    
    /* ตกแต่ง Card ของ P2P */
    .p2p-card {
        background-color: #f0fdf4;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #22c55e;
        margin-bottom: 10px;
        font-size: 1.3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (คงอาคาร G หนองระเวียงไว้)
df_stations = pd.DataFrame([
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง"}
])

# 3. Header Section (โลโก้ + ชื่อระบบ)
head_l, head_r = st.columns([1, 4])
with head_l:
    try: st.image("rmut.png", width=200)
    except: st.title("🏛️")
with head_r:
    st.markdown("<h1 style='font-size:3.5rem; margin-bottom:0;'>RMUTI AETHERA PLATFORM</h1>", unsafe_allow_html=True)
    st.markdown("### Smart Grid Management System")

st.divider()

# 4. Main Charts (ตามตัวอย่างที่คุณนุชอบ)
col_l, col_r = st.columns(2)
with col_l:
    st.markdown("<div class='section-header'>⚡ Energy Mix Today (kW)</div>", unsafe_allow_html=True)
    # กราฟเทรนด์วันนี้
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(y=np.random.normal(45, 5, 24), name="Consumption", line_color='red', fill='tozeroy'))
    fig_line.add_trace(go.Scatter(y=np.random.normal(15, 2, 24), name="Solar Gen", line_color='blue', fill='tozeroy'))
    fig_line.update_layout(height=350, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig_line, use_container_width=True)

with col_r:
    st.markdown("<div class='section-header'>📊 Monthly Yield (MW)</div>", unsafe_allow_html=True)
    # กราฟแท่งรายเดือน
    fig_bar = go.Figure(go.Bar(x=[f"{i+1:02d}" for i in range(28)], y=[80, 235, 255, 270, 245, 165]+[0]*22, marker_color='#a855f7'))
    fig_bar.update_layout(height=350, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# 5. Adjusted Bottom Section: Bigger & Complete ESG
b1, b2, b3 = st.columns([1.5, 0.8, 1.2])

with b1:
    st.markdown("<div class='section-header'>📊 Station Breakdown</div>", unsafe_allow_html=True)
    st.table(df_stations)

with b2:
    st.markdown("<div class='section-header'>🌿 ESG</div>", unsafe_allow_html=True)
    # แสดงข้อมูลครบทั้ง 3 ส่วน: CO2, Coal, Trees
    try:
        st.image("CO2.png", width=110)
        st.markdown("#### 27.24 T <br> <small>CO2 Saved</small>", unsafe_allow_html=True)
        st.write("")
        st.image("Coal.png", width=110) # ข้อมูล Coal ที่เคยหายไปกลับมาแล้ว
        st.markdown("#### 21.79 T <br> <small>Coal Saved</small>", unsafe_allow_html=True)
        st.write("")
        st.image("Tree.png", width=110)
        st.markdown("#### 680 <br> <small>Trees Planted</small>", unsafe_allow_html=True)
    except:
        st.info("💡 กรุณาตรวจสอบไฟล์รูปภาพ CO2.png, Coal.png, Tree.png")

with b3:
    st.markdown("<div class='section-header'>🤝 P2P Trading</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='p2p-card'>✅ Admin ⚡ Hall(2): 12.5 kWh</div>
        <div class='p2p-card'>✅ Bus(32) ⚡ Lib(4): 25.0 kWh</div>
        <div style='background-color:#eff6ff; padding:15px; border-radius:10px; border-left:5px solid #3b82f6; font-size:1.2rem;'>
            🔵 Market Status: Active (3.8 - 4.0 ฿)
        </div>
    """, unsafe_allow_html=True)
