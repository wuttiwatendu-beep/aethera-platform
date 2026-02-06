import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="RMUTI AETHERA PLATFORM", layout="wide")

st.markdown("""
    <style>
    /* ขยายตัวเลขหลักให้ดูแน่น */
    [data-testid="stMetricValue"] {
        font-size: 3.8rem !important;
        font-weight: 800 !important;
        color: #1e3a8a;
    }
    /* ปรับแต่งหัวข้อ Section ให้เด่น */
    .section-header {
        font-size: 2rem !important;
        font-weight: 700;
        color: #1e3a8a;
        border-left: 10px solid #f59e0b;
        padding-left: 15px;
        margin-top: 10px;
    }
    /* ตกแต่งข้อความ ESG */
    .esg-label {
        font-size: 1.2rem;
        font-weight: 700;
        text-align: center;
        color: #374151;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Top Header: Huge Logo & Title
# เน้น Logo มหาวิทยาลัยให้ใหญ่ตามสั่ง
head_l, head_r = st.columns([1, 3.5])
with head_l:
    try: st.image("rmut.png", width=280) 
    except: st.title("🏛️ RMUTI")
with head_r:
    st.markdown("<h1 style='font-size:4rem; color:#1e3a8a; margin-top:40px;'>AETHERA COMMAND CENTER</h1>", unsafe_allow_html=True)

st.divider()

# 3. Main Metrics (แถวที่ 2)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("P2P Volume (kWh)", "80.3")

st.write("") # เพิ่มระยะห่างเล็กน้อย

# 4. ESG Section (ย้ายลงมาวางแนวนอนเหนือระดับกราฟ)
# ขยายขนาดรูปไอคอน 3 รูปให้ใหญ่และสมดุล
st.markdown("---")
e_space, e1, e2, e3, e_title = st.columns([1, 1, 1, 1, 1.5])

with e1:
    st.image("CO2.png", width=130) # ขยายขนาดรูป
    st.markdown("<div class='esg-label'>27.24 T<br>CO2 Saved</div>", unsafe_allow_html=True)
with e2:
    st.image("Coal.png", width=130) # ข้อมูล Coal กลับมาเด่นชัด
    st.markdown("<div class='esg-label'>21.79 T<br>Coal Saved</div>", unsafe_allow_html=True)
with e3:
    st.image("Tree.png", width=130)
    st.markdown("<div class='esg-label'>680 Trees<br>Planted</div>", unsafe_allow_html=True)
with e_title:
    st.markdown("<h2 style='text-align:right; color:#059669; margin-top:20px;'>🌿 Environment<br>Benefits</h2>", unsafe_allow_html=True)

# 5. Charts Area (วางต่อจาก ESG ทันทีเพื่อให้ดูไม่โล่ง)
col_l, col_r = st.columns(2)

with col_l:
    st.markdown("<div class='section-header'>⚡ Today Power Mix (kW)</div>", unsafe_allow_html=True)
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 5, 24), name="Consumption", line_color='#ef4444', fill='tozeroy'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(20, 3, 24), name="Solar Generation", line_color='#3b82f6', fill='tozeroy'))
    fig_mix.update_layout(height=400, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_mix, use_container_width=True)

with col_r:
    st.markdown("<div class='section-header'>📊 Monthly Generation (MW)</div>", unsafe_allow_html=True)
    # กราฟแท่งสีม่วงเลียนแบบ Revenue ที่คุณนุชอบ
    fig_bar = go.Figure(go.Bar(
        x=[f"{i+1:02d}" for i in range(28)], 
        y=[80, 235, 255, 270, 245, 165] + [0]*22, 
        marker_color='#a855f7'
    ))
    fig_bar.update_layout(height=400, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_bar, use_container_width=True)

# 6. Footer: Station & P2P
st.divider()
bot_l, bot_r = st.columns([1.5, 1])
with bot_l:
    st.markdown("<div class='section-header'>📊 Station Details</div>", unsafe_allow_html=True)
    df = pd.DataFrame([
        {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
        {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"}
    ])
    st.table(df)
with bot_r:
    st.markdown("<div class='section-header'>🤝 Live P2P Status</div>", unsafe_allow_html=True)
    st.success("### ✅ Admin ⚡ Hall(2): 12.5 kWh")
    st.success("### ✅ Business(32) ⚡ Lib(4): 25.0 kWh")
