import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration & Advanced CSS
st.set_page_config(page_title="RMUTI AETHERA PLATFORM", layout="wide")

st.markdown("""
    <style>
    /* ปรับแต่งตัวเลขหลักให้ดูแน่นและมีพลัง */
    [data-testid="stMetricValue"] {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        color: #1e3a8a;
    }
    /* ปรับแต่งข้อความกำกับ ESG */
    .esg-text {
        font-size: 1.3rem;
        font-weight: 700;
        text-align: center;
        color: #1f2937;
        margin-top: -10px;
    }
    /* หัวข้อกราฟ */
    .section-title {
        font-size: 1.8rem !important;
        font-weight: 700;
        color: #1e3a8a;
        border-left: 8px solid #f59e0b;
        padding-left: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Top Header Area (Logo & Title)
head_l, head_r = st.columns([1, 4])
with head_l:
    try: st.image("rmut.png", width=260) # Logo ขนาดใหญ่สมดุล
    except: st.title("🏛️")
with head_r:
    st.markdown("<h1 style='font-size:3.5rem; color:#1e3a8a; margin-top:25px; text-align:center;'>AETHERA COMMAND CENTER</h1>", unsafe_allow_html=True)

# 3. ESG ROW (วางในตำแหน่งกรอบสีน้ำเงินที่คุณนุทำไว้)
# จัดวาง 3 รูปแนวนอนให้สมดุล
st.write("") # สร้างช่องไฟ
esg_col1, esg_col2, esg_col3, esg_col4, esg_col5 = st.columns([1, 1, 1, 1, 1])

with esg_col2:
    st.image("CO2.png", width=140)
    st.markdown("<div class='esg-text'>27.24 T<br>CO2 Saved</div>", unsafe_allow_html=True)
with esg_col3:
    st.image("Coal.png", width=140) # ข้อมูล Coal กลับมาเด่นชัด
    st.markdown("<div class='esg-text'>21.79 T<br>Coal Saved</div>", unsafe_allow_html=True)
with esg_col4:
    st.image("Tree.png", width=140)
    st.markdown("<div class='esg-text'>680 Trees<br>Planted</div>", unsafe_allow_html=True)

st.divider()

# 4. Key Metrics Row
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("P2P Volume (kWh)", "80.3")

st.write("")

# 5. Analytics Charts Row
col_l, col_r = st.columns(2)

with col_l:
    st.markdown("<div class='section-title'>⚡ Today Power Mix (kW)</div>", unsafe_allow_html=True)
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 5, 24), name="Load", line_color='#ef4444', fill='tozeroy'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(20, 3, 24), name="Solar", line_color='#3b82f6', fill='tozeroy'))
    fig_mix.update_layout(height=380, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_mix, use_container_width=True)

with col_r:
    st.markdown("<div class='section-title'>📊 Monthly Generation (MW)</div>", unsafe_allow_html=True)
    # กราฟแท่งสีม่วง
    fig_bar = go.Figure(go.Bar(x=[f"{i+1:02d}" for i in range(28)], y=[80, 235, 255, 270, 245, 165]+[0]*22, marker_color='#a855f7'))
    fig_bar.update_layout(height=380, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_bar, use_container_width=True)

# 6. Detail Section
st.divider()
bot_l, bot_r = st.columns([1.5, 1])
with bot_l:
    st.markdown("<div class='section-title'>📊 Station Details</div>", unsafe_allow_html=True)
    df = pd.DataFrame([
        {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
        {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"}
    ])
    st.table(df)
with bot_r:
    st.markdown("<div class='section-title'>🤝 Live P2P Status</div>", unsafe_allow_html=True)
    st.success("✅ Admin ⚡ Hall(2): 12.5 kWh")
    st.success("✅ Bus(32) ⚡ Lib(4): 25.0 kWh")
