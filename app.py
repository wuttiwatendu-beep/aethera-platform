import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="AETHERA NETZERO PLATFORM", layout="wide")

st.markdown("""
    <style>
    /* ปรับแต่งฟอนต์หัวข้อให้ดู Modern และ High-End */
    .platform-name {
        font-size: 1.8rem !important;
        font-weight: 700;
        color: #1e3a8a;
        letter-spacing: 2px;
        margin-bottom: -10px;
    }
    .project-main-title {
        font-size: 2.8rem !important;
        font-weight: 800;
        color: #b43d8b;
        line-height: 1.2;
    }
    .project-sub-title {
        font-size: 1.8rem !important;
        font-weight: 600;
        color: #1e40af;
    }
    
    /* การตกแต่ง Metric Card ให้ดูพรีเมียม */
    [data-testid="stMetricValue"] {
        font-size: 3.2rem !important;
        font-weight: 800 !important;
        color: #1e3a8a;
    }
    
    /* ส่วน ESG Box แบบมีเงา (Shadow) ให้ดูมีมิติ */
    .esg-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #e5e7eb;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header: RMUTI Logo | Title | NetZero Logo
h_col1, h_col2, h_col3 = st.columns([1, 4, 1])

with h_col1:
    st.image("rmut.png", width=180)

with h_col2:
    # ขยับลงมาในระดับแนวเส้นใต้ที่คุณนุต้องการ
    st.markdown("<div style='height: 120px;'></div>", unsafe_allow_html=True)
    st.markdown('<p class="platform-name">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="project-main-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p class="project-sub-title">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

with h_col3:
    # เพิ่มโลโก้ NetZero Platform 1 ตามที่คุณนุสั่ง
    try: st.image("NetZero_Platform_1.png", width=180)
    except: st.markdown("<div style='text-align:right; font-weight:bold; color:green; margin-top:150px;'>NetZero<br>Platform 1</div>", unsafe_allow_html=True)

st.write("")

# 3. ESG Impact Section (4 Cards Style - ดูสะอาดตา)
e1, e2, e3, e4 = st.columns(4)
with e1:
    st.markdown("<div class='esg-card'>", unsafe_allow_html=True)
    st.image("CO2.png", width=100)
    st.markdown("<h3>27.24 T</h3><p>CO2 Saved</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
with e2:
    st.markdown("<div class='esg-card'>", unsafe_allow_html=True)
    st.image("Coal.png", width=100)
    st.markdown("<h3>21.79 T</h3><p>Coal Saved</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
with e3:
    st.markdown("<div class='esg-card'>", unsafe_allow_html=True)
    st.image("Tree.png", width=100)
    st.markdown("<h3>680 Trees</h3><p>Planted</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
with e4:
    # การ์ดพิเศษสำหรับ NetZero สรุปผล
    st.markdown("<div class='esg-card' style='background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#166534; margin-top:20px;'>NetZero</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:bold;'>Target Reached</p><h3 style='color:#15803d;'>85%</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# 4. Main Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time (kW)", "2,854.56", "↑ 12%")
m2.metric("Total Yield (MW)", "54.473", "↑ 5.4")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("P2P Volume (kWh)", "80.3", "Live")

# 5. Charts Area (24h Trend & Power Mix)
st.write("")
c1, c2 = st.columns(2)
with c1:
    st.subheader("⚡ 24-Hour Solar Production Trend")
    hours = [f"{i:02d}:00" for i in range(24)]
    gen = [0,0,0,0,0,50,300,900,1800,2500,2854,2700,2400,1900,1100,400,80,0,0,0,0,0,0,0]
    fig = go.Figure(go.Scatter(x=hours, y=gen, fill='tozeroy', line_color='#f59e0b', name="Power kW"))
    fig.update_layout(height=350, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("📊 Today Power Mix (Load vs Solar)")
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 5, 24), name="Load", fill='tozeroy', line_color='#ef4444'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(20, 3, 24), name="Solar", fill='tozeroy', line_color='#3b82f6'))
    fig_mix.update_layout(height=350, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_mix, use_container_width=True)

# 6. Bottom Table & Monthly Graph
st.divider()
b1, b2 = st.columns([1.2, 1])
with b1:
    st.subheader("📋 Station Details (10 Buildings)")
    df = pd.DataFrame([
        {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
        {"อาคาร": "อาคาร A (สำรอง)", "kW": 180.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "อาคาร B (สำรอง)", "kW": 170.00, "Zone": "ศูนย์กลาง"}
    ])
    st.table(df)
with b2:
    st.subheader("📅 Monthly Performance (MW)")
    fig_m = go.Figure(go.Bar(x=[f"{i+1:02d}" for i in range(28)], y=[80, 235, 255, 270, 245, 165]+[0]*22, marker_color='#a855f7'))
    fig_m.update_layout(height=300, margin=dict(t=0, b=0))
    st.plotly_chart(fig_m, use_container_width=True)
