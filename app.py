import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="AETHERA NETZERO PLATFORM", layout="wide")

st.markdown("""
    <style>
    /* ปรับแต่งชื่อ Platform และเพิ่มช่องไฟ (Margin Bottom) */
    .platform-name {
        font-size: 1.8rem !important;
        font-weight: 700;
        color: #1e3a8a;
        letter-spacing: 3px;
        margin-bottom: 25px !important; /* เพิ่มช่องไฟให้มากขึ้นตามสั่ง */
        border-bottom: 2px solid #e5e7eb;
        display: inline-block;
        padding-bottom: 5px;
    }
    
    /* ข้อความโครงการหลัก */
    .project-main-title {
        font-size: 2.8rem !important;
        font-weight: 800;
        color: #b43d8b; /* สีชมพูเข้ม */
        line-height: 1.2;
        margin-top: 10px;
    }
    
    .project-sub-title {
        font-size: 1.8rem !important;
        font-weight: 700;
        color: #1e40af;
        margin-top: 5px;
    }

    /* ตกแต่ง Metric Card */
    [data-testid="stMetricValue"] {
        font-size: 3.2rem !important;
        font-weight: 800 !important;
        color: #1e3a8a;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header: Logo | Aligned Titles | NetZero Logo
h_col1, h_col2, h_col3 = st.columns([1, 4, 1])

with h_col1:
    st.image("rmut.png", width=200) # โลโก้มหาวิทยาลัย

with h_col2:
    # ปรับระดับลงมาตามแนวเส้นใต้เดิมที่คุณนุเคยกำหนด
    st.markdown("<div style='height: 120px;'></div>", unsafe_allow_html=True)
    
    # ส่วนของชื่อ Platform พร้อมช่องไฟที่กว้างขึ้น
    st.markdown('<p class="platform-name">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    
    # ข้อความโครงการ
    st.markdown('<p class="project-main-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p class="project-sub-title">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

with h_col3:
    # วางรูป NetZero Platform 1 ในระดับที่สมดุลกัน
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
    st.image("NetZero_Platform_1.png", width=180)

st.write("")
st.divider()

# 3. Environmental & Performance Section
# แสดงผล 3 รูป ESG ขนาดใหญ่ในตำแหน่งเดิม (กรอบสีน้ำเงิน)
e_pad, e1, e2, e3, e_pad2 = st.columns([0.8, 1, 1, 1, 0.8])
with e1:
    st.image("CO2.png", width=140)
    st.metric("CO2 Saved", "27.24 T")
with e2:
    st.image("Coal.png", width=140)
    st.metric("Coal Saved", "21.79 T")
with e3:
    st.image("Tree.png", width=140)
    st.metric("Trees Planted", "680 Trees")

st.divider()

# 4. Analytics Dashboard (24h Trend, Power Mix, Station Details)
# ส่วนนี้ยังคงข้อมูลครบถ้วนทั้ง 10 สถานีและกราฟวิเคราะห์
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 24-Hour Production Trend (kW)")
    # กราฟเทรนด์สีส้มทอง
    hours = [f"{i:02d}:00" for i in range(24)]
    gen = [0,0,0,0,0,50,300,900,1800,2500,2854,2700,2400,1900,1100,400,80,0,0,0,0,0,0,0]
    fig = go.Figure(go.Scatter(x=hours, y=gen, fill='tozeroy', line_color='#f59e0b'))
    fig.update_layout(height=300, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📋 Station Details (10 Buildings)")
    df = pd.DataFrame([
        {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
        {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "อาคาร A (สำรอง)", "kW": 180.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "อาคาร B (สำรอง)", "kW": 170.00, "Zone": "ศูนย์กลาง"}
    ])
    st.table(df)

with col_right:
    st.subheader("⚡ Today Power Mix")
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 5, 24), name="Load", fill='tozeroy', line_color='#ef4444'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(20, 3, 24), name="Solar", fill='tozeroy', line_color='#3b82f6'))
    fig_mix.update_layout(height=300, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig_mix, use_container_width=True)
    
    st.subheader("📅 Monthly Performance")
    fig_m = go.Figure(go.Bar(x=[f"{i+1:02d}" for i in range(28)], y=[80, 235, 255, 270, 245, 165]+[0]*22, marker_color='#a855f7'))
    fig_m.update_layout(height=250, margin=dict(t=0, b=0))
    st.plotly_chart(fig_m, use_container_width=True)
