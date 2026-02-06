import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="RMUTI AETHERA COMMAND", layout="wide")

st.markdown("""
    <style>
    /* ปรับแต่งหัวข้อโครงการให้ใหญ่และเด่นชัดตามรูป */
    .main-title {
        font-size: 2.8rem !important;
        font-weight: 800;
        color: #b43d8b; /* สีชมพูเข้มตามรูป */
        text-align: center;
        margin-bottom: 5px;
        line-height: 1.2;
    }
    .sub-title {
        font-size: 2.2rem !important;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* ขยายตัวเลข Metrics แถวกลางให้ใหญ่ */
    [data-testid="stMetricValue"] { font-size: 3.2rem !important; font-weight: 800 !important; color: #1e3a8a; }
    [data-testid="stMetricLabel"] { font-size: 1.2rem !important; font-weight: 600; }
    
    /* ส่วน ESG แถวบนสุด */
    .esg-box { text-align: center; padding: 10px; }
    .esg-number { font-size: 2.2rem !important; font-weight: 800; color: #1f2937; }
    .esg-text { font-size: 1.1rem; font-weight: 600; color: #4b5563; }
    
    .section-header {
        font-size: 1.5rem !important; font-weight: 700; color: #1e3a8a;
        border-left: 8px solid #f59e0b; padding-left: 12px; margin: 15px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Top Header Area
t1, t2 = st.columns([1, 6])
with t1:
    st.image("rmut.png", width=180)
with t2:
    st.markdown('<p class="main-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

# 3. ESG Row (High Visibility Zone)
e_pad, e1, e2, e3, e_pad2 = st.columns([0.8, 1, 1, 1, 0.8])
with e1:
    st.markdown("<div class='esg-box'>", unsafe_allow_html=True)
    st.image("CO2.png", width=140)
    st.markdown("<div class='esg-number'>27.24 T</div><div class='esg-text'>CO2 Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
with e2:
    st.markdown("<div class='esg-box'>", unsafe_allow_html=True)
    st.image("Coal.png", width=140)
    st.markdown("<div class='esg-number'>21.79 T</div><div class='esg-text'>Coal Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
with e3:
    st.markdown("<div class='esg-box'>", unsafe_allow_html=True)
    st.image("Tree.png", width=140)
    st.markdown("<div class='esg-number'>680 Trees</div><div class='esg-text'>Planted</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# 4. Key Performance Metrics Row
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("P2P Volume Today (kWh)", "80.3")

st.divider()

# 5. Dashboard Main Content (Graphs & Table)
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("<div class='section-header'>📊 24-Hour Solar Production Trend (kW)</div>", unsafe_allow_html=True)
    # กราฟ 24 ชม. สีส้มทอง
    hours = [f"{i:02d}:00" for i in range(24)]
    gen_vals = [0,0,0,0,0,50,300,900,1800,2500,2854,2700,2400,1900,1100,400,80,0,0,0,0,0,0,0]
    fig_solar = go.Figure(go.Scatter(x=hours, y=gen_vals, fill='tozeroy', line_color='#f59e0b'))
    fig_solar.update_layout(height=350, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig_solar, use_container_width=True)

    st.markdown("<div class='section-header'>📋 Station Details (9 Central + 1 NRW)</div>", unsafe_allow_html=True)
    # ตาราง 10 สถานี (ศูนย์กลาง 9 + หนองระเวียง 1)
    df_stations = pd.DataFrame([
        {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "หอประชุมวชิราลงกรณ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "Sports Complex", "kW": 200.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "อาคาร A (สำรอง)", "kW": 180.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "อาคาร B (สำรอง)", "kW": 170.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"}
    ])
    st.table(df_stations)

with col_right:
    st.markdown("<div class='section-header'>⚡ Today Power Mix (kW)</div>", unsafe_allow_html=True)
    # กราฟ Power Mix แดง-ฟ้า
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 5, 24), name="Load", fill='tozeroy', line_color='#ef4444'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(20, 3, 24), name="Solar", fill='tozeroy', line_color='#3b82f6'))
    fig_mix.update_layout(height=350, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig_mix, use_container_width=True)

    st.markdown("<div class='section-header'>📅 Monthly Generation (MW)</div>", unsafe_allow_html=True)
    # กราฟรายเดือนสีม่วง
    fig_monthly = go.Figure(go.Bar(x=[f"{i+1:02d}" for i in range(28)], y=[80, 235, 255, 270, 245, 165]+[0]*22, marker_color='#a855f7'))
    fig_monthly.update_layout(height=300, margin=dict(t=0, b=0))
    st.plotly_chart(fig_monthly, use_container_width=True)

    st.markdown("<div class='section-header'>🤝 Live P2P Trading Status</div>", unsafe_allow_html=True)
    # สถานะ P2P
    st.success("✅ Admin ⚡ Hall(2): 12.5 kWh")
    st.info("✅ Business(32) ⚡ Lib(4): 25.0 kWh")
