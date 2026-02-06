import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="RMUTI AETHERA COMMAND", layout="wide")

st.markdown("""
    <style>
    /* ขยายตัวเลขหลักด้านบน (Metrics) */
    [data-testid="stMetricValue"] {
        font-size: 3.8rem !important;
        font-weight: 800 !important;
        color: #1e3a8a;
    }
    
    /* ปรับแต่งส่วน ESG ในกรอบสีน้ำเงิน */
    .esg-container {
        text-align: center;
        padding: 10px;
    }
    .esg-value {
        font-size: 2.2rem !important;
        font-weight: 800;
        color: #1f2937;
        margin-top: 5px;
    }
    .esg-label {
        font-size: 1.2rem;
        font-weight: 600;
        color: #4b5563;
    }
    
    /* หัวข้อ Section */
    .section-header {
        font-size: 1.8rem !important;
        font-weight: 700;
        color: #1e3a8a;
        border-left: 10px solid #f59e0b;
        padding-left: 15px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header: Logo & Title
h_col1, h_col2 = st.columns([1, 4])
with h_col1:
    try: st.image("rmut.png", width=240) 
    except: st.title("🏛️")
with h_col2:
    st.markdown("<h1 style='font-size:3.5rem; color:#1e3a8a; margin-top:30px; text-align:center;'>AETHERA COMMAND CENTER</h1>", unsafe_allow_html=True)

# 3. ESG Row: "The Blue Box Zone" (ย้ายขึ้นมาและขยายขนาดใหญ่)
st.write("") 
e_pad, e1, e2, e3, e_pad2 = st.columns([0.5, 1, 1, 1, 0.5])

with e1:
    st.markdown("<div class='esg-container'>", unsafe_allow_html=True)
    st.image("CO2.png", width=180) # ขยายรูปให้ใหญ่ขึ้นชัดเจน
    st.markdown("<div class='esg-value'>27.24 T</div><div class='esg-label'>CO2 Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with e2:
    st.markdown("<div class='esg-container'>", unsafe_allow_html=True)
    st.image("Coal.png", width=180) # คืนค่าข้อมูล Coal Saved
    st.markdown("<div class='esg-value'>21.79 T</div><div class='esg-label'>Coal Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with e3:
    st.markdown("<div class='esg-container'>", unsafe_allow_html=True)
    st.image("Tree.png", width=180) # ขยายรูปให้ใหญ่สมดุล
    st.markdown("<div class='esg-value'>680 Trees</div><div class='esg-label'>Planted</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# 4. Key Performance Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("P2P Volume (kWh)", "80.3")

st.write("")

# 5. Analytics Charts Row
c1, c2 = st.columns(2)
with c1:
    st.markdown("<div class='section-header'>⚡ Today Power Mix (kW)</div>", unsafe_allow_html=True)
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(y=np.random.normal(45, 5, 24), name="Load", line_color='#ef4444', fill='tozeroy'))
    fig1.add_trace(go.Scatter(y=np.random.normal(20, 3, 24), name="Solar", line_color='#3b82f6', fill='tozeroy'))
    fig1.update_layout(height=350, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.markdown("<div class='section-header'>📊 Monthly Generation (MW)</div>", unsafe_allow_html=True)
    fig2 = go.Figure(go.Bar(x=[f"{i+1:02d}" for i in range(28)], y=[80, 235, 255, 270, 245, 165]+[0]*22, marker_color='#a855f7'))
    fig2.update_layout(height=350, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig2, use_container_width=True)

# 6. Bottom Details
st.divider()
b1, b2 = st.columns([1.5, 1])
with b1:
    st.markdown("<div class='section-header'>📊 Station Details</div>", unsafe_allow_html=True)
    df = pd.DataFrame([
        {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"}
    ])
    st.table(df)
with b2:
    st.markdown("<div class='section-header'>🤝 Live P2P Status</div>", unsafe_allow_html=True)
    st.success("✅ Admin ⚡ Hall(2): 12.5 kWh")
    st.success("✅ Bus(32) ⚡ Lib(4): 25.0 kWh")
