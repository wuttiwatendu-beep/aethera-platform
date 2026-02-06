import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="RMUTI AETHERA COMMAND", layout="wide")

st.markdown("""
    <style>
    /* ขยายตัวเลข Metrics หลัก */
    [data-testid="stMetricValue"] { font-size: 3.8rem !important; font-weight: 800 !important; color: #1e3a8a; }
    
    /* สไตล์ส่วน ESG */
    .esg-container { text-align: center; padding: 10px; }
    .esg-value { font-size: 2.2rem !important; font-weight: 800; color: #1f2937; margin-top: 5px; }
    .esg-label { font-size: 1.2rem; font-weight: 600; color: #4b5563; }
    
    /* หัวข้อ Section */
    .section-header {
        font-size: 1.8rem !important;
        font-weight: 700;
        color: #1e3a8a;
        border-left: 10px solid #f59e0b;
        padding-left: 15px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header
h1, h2 = st.columns([1, 4])
with h1:
    try: st.image("rmut.png", width=250) 
    except: st.title("🏛️")
with h2:
    st.markdown("<h1 style='font-size:3.5rem; color:#1e3a8a; margin-top:25px; text-align:center;'>AETHERA COMMAND CENTER</h1>", unsafe_allow_html=True)

# 3. ESG ROW (ขยายใหญ่ 3 รูปในตำแหน่งกรอบบน)
st.write("") 
e_pad, e1, e2, e3, e_pad2 = st.columns([0.5, 1, 1, 1, 0.5])
with e1:
    st.markdown("<div class='esg-container'>", unsafe_allow_html=True)
    st.image("CO2.png", width=200) #
    st.markdown("<div class='esg-value'>27.24 T</div><div class='esg-label'>CO2 Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
with e2:
    st.markdown("<div class='esg-container'>", unsafe_allow_html=True)
    st.image("Coal.png", width=200) #
    st.markdown("<div class='esg-value'>21.79 T</div><div class='esg-label'>Coal Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
with e3:
    st.markdown("<div class='esg-container'>", unsafe_allow_html=True)
    st.image("Tree.png", width=200)
    st.markdown("<div class='esg-value'>680 Trees</div><div class='esg-label'>Planted</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# 4. Key Performance Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("P2P Volume (kWh)", "80.3")

st.divider()

# 5. Production Graph & Station Details
col_l, col_r = st.columns([1.5, 1])

with col_l:
    st.markdown("<div class='section-header'>📈 24-Hour Solar Production Trend (kW)</div>", unsafe_allow_html=True)
    hours = [f"{i:02d}:00" for i in range(24)]
    gen_values = [0,0,0,0,0,50,300,900,1800,2500,2854,2700,2400,1900,1100,400,80,0,0,0,0,0,0,0]
    fig_24h = go.Figure()
    fig_24h.add_trace(go.Scatter(x=hours, y=gen_values, mode='lines', line=dict(color='#f59e0b', width=4), fill='tozeroy'))
    fig_24h.update_layout(height=450, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_24h, use_container_width=True)

with col_r:
    st.markdown("<div class='section-header'>📊 Station Details (Corrected)</div>", unsafe_allow_html=True)
    # เพิ่มอาคาร A และ B ในโซนศูนย์กลางตามสั่ง
    df_stations = pd.DataFrame([
        {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "อาคาร A (สำรอง)", "kW": 380.00, "Zone": "ศูนย์กลาง"}, # เพิ่มใหม่
        {"อาคาร": "อาคาร B (สำรอง)", "kW": 365.00, "Zone": "ศูนย์กลาง"}, # เพิ่มใหม่
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"}, #
        {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "หอประชุมวชิราลงกรณ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง"},
    ])
    st.table(df_stations)
