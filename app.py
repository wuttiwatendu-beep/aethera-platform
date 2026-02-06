import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration & Custom UI Scaling
st.set_page_config(page_title="RMUTI AETHERA PLATFORM", layout="wide")

st.markdown("""
    <style>
    /* ขยายขนาด Metric หลักให้ใหญ่พิเศษ */
    [data-testid="stMetricValue"] {
        font-size: 4.2rem !important;
        font-weight: 800 !important;
        color: #1e3a8a;
        line-height: 1;
    }
    [data-testid="stMetricLabel"] { font-size: 1.5rem !important; font-weight: 600 !important; }
    
    /* ตกแต่ง Header Area */
    .header-container {
        display: flex;
        align-items: center;
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    
    /* ขยายฟอนต์ ESG ด้านบน */
    .esg-top-text {
        font-size: 1.4rem;
        font-weight: 700;
        text-align: center;
        margin-top: 5px;
    }
    
    /* ส่วนหัวข้อ Section */
    .section-title {
        font-size: 2.2rem !important;
        font-weight: 700;
        color: #1e3a8a;
        border-left: 10px solid #f59e0b;
        padding-left: 20px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Top Header: Logo + ESG Horizontal (ย้าย ESG มาไว้ด้านบนตามสั่ง)
head_col1, head_col2, head_col3, head_col4, head_col5 = st.columns([1.5, 1, 1, 1, 1.5])

with head_col1:
    try: st.image("rmut.png", width=250) # เพิ่มขนาด Logo ให้ใหญ่สมดุล
    except: st.title("🏛️ RMUTI")

# ข้อมูล ESG แนวนอน
with head_col2:
    st.image("CO2.png", width=100)
    st.markdown("<div class='esg-top-text'>27.24 T<br><small>CO2 Saved</small></div>", unsafe_allow_html=True)
with head_col3:
    st.image("Coal.png", width=100) # ข้อมูล Coal กลับมาแสดงผลด้านบน
    st.markdown("<div class='esg-top-text'>21.79 T<br><small>Coal Saved</small></div>", unsafe_allow_html=True)
with head_col4:
    st.image("Tree.png", width=100)
    st.markdown("<div class='esg-top-text'>680<br><small>Trees Planted</small></div>", unsafe_allow_html=True)

with head_col5:
    st.markdown("<h1 style='text-align:right; color:#1e3a8a; font-size:2.5rem;'>AETHERA<br>COMMAND</h1>", unsafe_allow_html=True)

st.divider()

# 3. Key Performance Metrics (ขยายขนาดให้สมดุล)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("P2P Volume (kWh)", "80.3")

st.divider()

# 4. Main Content: Charts & Tables (จัดให้แน่นเต็มพื้นที่)
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("<div class='section-title'>⚡ Today Power Mix (kW)</div>", unsafe_allow_html=True)
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 5, 24), name="Load", line_color='red', fill='tozeroy'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(20, 3, 24), name="Solar", line_color='blue', fill='tozeroy'))
    fig_mix.update_layout(height=450, margin=dict(l=0,r=0,t=0,b=0), font=dict(size=14))
    st.plotly_chart(fig_mix, use_container_width=True)

with col_right:
    st.markdown("<div class='section-title'>📊 Monthly Generation (MW)</div>", unsafe_allow_html=True)
    # กราฟแท่งสีม่วงตามตัวอย่างที่ชอบ
    days = [f"{i+1:02d}" for i in range(28)]
    yield_vals = [80, 235, 255, 270, 245, 165] + [0]*22
    fig_monthly = go.Figure(go.Bar(x=days, y=yield_vals, marker_color='#a855f7', textposition='outside'))
    fig_monthly.update_layout(height=450, margin=dict(l=0,r=0,t=0,b=0), font=dict(size=14))
    st.plotly_chart(fig_monthly, use_container_width=True)

st.divider()

# 5. Bottom Details: Station & Trading
bot_l, bot_r = st.columns([1.5, 1])

with bot_l:
    st.markdown("<div class='section-title'>📊 Station Breakdown</div>", unsafe_allow_html=True)
    df_stations = pd.DataFrame([
        {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
        {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"}
    ])
    st.table(df_stations)

with bot_r:
    st.markdown("<div class='section-title'>🤝 Live P2P Status</div>", unsafe_allow_html=True)
    st.success("### ✅ Admin ⚡ Hall(2): 12.5 kWh | 3.8฿")
    st.success("### ✅ Bus(32) ⚡ Lib(4): 25.0 kWh | 4.0฿")
    st.info("### 🔵 Market: Active (3.8 - 4.0 ฿)")
