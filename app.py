import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration & Professional Styling
st.set_page_config(page_title="RMUTI AETHERA PLATFORM", layout="wide")

st.markdown("""
    <style>
    /* ขยายตัวเลข Metrics หลักให้ใหญ่และคมชัด */
    [data-testid="stMetricValue"] { font-size: 3.5rem !important; font-weight: 800 !important; color: #1e3a8a; }
    
    /* สไตล์ส่วน ESG (กรอบสีน้ำเงินด้านบน) */
    .esg-container { text-align: center; padding: 5px; }
    .esg-value { font-size: 2.2rem !important; font-weight: 800; color: #1f2937; margin-top: 5px; }
    .esg-label { font-size: 1.1rem; font-weight: 600; color: #4b5563; }
    
    /* หัวข้อ Section */
    .section-header {
        font-size: 1.6rem !important; font-weight: 700; color: #1e3a8a;
        border-left: 8px solid #f59e0b; padding-left: 15px; margin: 15px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header: Logo & Title
h1, h2 = st.columns([1, 4])
with h1:
    try: st.image("rmut.png", width=220) 
    except: st.title("🏛️")
with h2:
    st.markdown("<h1 style='font-size:3.2rem; color:#1e3a8a; margin-top:20px; text-align:center;'>AETHERA COMMAND CENTER</h1>", unsafe_allow_html=True)

# 3. ESG IMPACT ROW: "The Blue Box Zone"
# ขยายขนาดใหญ่ 3 รูป พร้อมค่าตัวเลขที่ชัดเจน
st.write("") 
e_pad, e1, e2, e3, e_pad2 = st.columns([0.6, 1, 1, 1, 0.6])
with e1:
    st.markdown("<div class='esg-container'>", unsafe_allow_html=True)
    st.image("CO2.png", width=180) #
    st.markdown("<div class='esg-value'>27.24 T</div><div class='esg-label'>CO2 Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
with e2:
    st.markdown("<div class='esg-container'>", unsafe_allow_html=True)
    st.image("Coal.png", width=180) #
    st.markdown("<div class='esg-value'>21.79 T</div><div class='esg-label'>Coal Saved</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
with e3:
    st.markdown("<div class='esg-container'>", unsafe_allow_html=True)
    st.image("Tree.png", width=180)
    st.markdown("<div class='esg-value'>680 Trees</div><div class='esg-label'>Planted</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# 4. KEY METRICS ROW
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Peak Capacity (kW)", "2,854.56")
m4.metric("P2P Volume (kWh)", "80.3")

# 5. MAIN ANALYTICS: 24-HOUR TREND & POWER MIX
col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    st.markdown("<div class='section-header'>📈 24-Hour Solar Production Trend (kW)</div>", unsafe_allow_html=True)
    hours = [f"{i:02d}:00" for i in range(24)]
    gen_values = [0,0,0,0,0,50,300,900,1800,2500,2854,2700,2400,1900,1100,400,80,0,0,0,0,0,0,0]
    fig_24h = go.Figure()
    fig_24h.add_trace(go.Scatter(x=hours, y=gen_values, mode='lines', fill='tozeroy', line_color='#f59e0b'))
    fig_24h.update_layout(height=350, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_24h, use_container_width=True)

with col_graph2:
    st.markdown("<div class='section-header'>⚡ Today Power Mix (kW)</div>", unsafe_allow_html=True)
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(45, 5, 24), name="Load", fill='tozeroy', line_color='#ef4444'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(20, 3, 24), name="Solar", fill='tozeroy', line_color='#3b82f6'))
    fig_mix.update_layout(height=350, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig_mix, use_container_width=True)

# 6. SECONDARY ANALYTICS: STATION DETAILS & MONTHLY GENERATION
col_table, col_month = st.columns([1.2, 1])

with col_table:
    st.markdown("<div class='section-header'>📊 Station Details (9 Central + 1 NRW)</div>", unsafe_allow_html=True)
    # ศูนย์กลาง 9 อาคาร (รวม A, B) + หนองระเวียง 1 (อาคาร G)
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
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
    ])
    st.table(df_stations)

with col_month:
    st.markdown("<div class='section-header'>📊 Monthly Generation (MW)</div>", unsafe_allow_html=True)
    # กราฟแท่งสีม่วง
    fig_bar = go.Figure(go.Bar(x=[f"{i+1:02d}" for i in range(28)], y=[80, 235, 255, 270, 245, 165]+[0]*22, marker_color='#a855f7'))
    fig_bar.update_layout(height=400, margin=dict(t=0, b=0))
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # 7. Live P2P Status
    st.markdown("<div class='section-header'>🤝 Live P2P Status</div>", unsafe_allow_html=True)
    st.success("✅ Admin ⚡ Hall(2): 12.5 kWh")
    st.success("✅ Business(32) ⚡ Lib(4): 25.0 kWh")
