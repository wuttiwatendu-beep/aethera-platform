import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import numpy as np

# --- 1. CORE CONFIG & PROFESSIONAL STYLING ---
st.set_page_config(page_title="AETHERA COMMAND PLATFORM", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8fafc; }

    /* Header & Titles */
    .main-title { font-size: 2.2rem !important; font-weight: 800; color: #1e3a8a; line-height: 1.2; margin-bottom: 5px; }
    .sub-title { font-size: 1.1rem; font-weight: 600; color: #b43d8b; }

    /* ✅ ESG Container: คลีน ไม่มีกล่องว่าง จัดวางกึ่งกลาง */
    .esg-group {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 15px;
    }
    .esg-value { font-size: 3rem !important; font-weight: 800; color: #0f172a; margin-top: 15px; }
    .esg-label { font-size: 1.1rem; color: #64748b; font-weight: 600; }

    /* Trading & Metric Cards */
    .card-pro {
        background: white;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .trading-val { font-size: 1.8rem; font-weight: 800; color: #10b981; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER SECTION ---
h_l, h_m, h_r = st.columns([1, 4, 2])

with h_l:
    st.image("rmut.png", width=150)

with h_m:
    st.markdown('<p class="sub-title">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#475569; font-weight:500;">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)

with h_r:
    st.image("NetZero platform 1.png", width=260)
    st.markdown(f"""
        <div style="background: #2563eb; color: white; padding: 15px; border-radius: 15px; margin-top: 10px;">
            <small>📍 NAKHON RATCHASIMA WEATHER</small><br>
            <b style="font-size: 1.8rem;">33.3°C</b><br>
            <small>Humidity: 40% | Wind: 5.6 km/h</small>
        </div>
    """, unsafe_allow_html=True)

# --- 3. ESG METRICS (Clean & Giant) ---
st.write("")
btn_c, c1, c2, c3 = st.columns([1.2, 2, 2, 2])

with btn_c:
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    st.button("ESG Metrics", use_container_width=True, type="primary")

def esg_block(col, img, val, lab):
    with col:
        st.markdown('<div class="esg-group">', unsafe_allow_html=True)
        st.image(img, width=140) # ขยายไอคอนใหญ่สะใจ
        st.markdown(f'<div class="esg-value">{val}</div><div class="esg-label">{lab}</div></div>', unsafe_allow_html=True)

esg_block(c1, "CO2.png", "27.24 T", "CO2 Saved")
esg_block(c2, "Coal.png", "21.79 T", "Coal Saved")
esg_block(c3, "Tree.png", "680", "Trees Planted")

# --- 4. ⚡ NEW: P2P ENERGY TRADING SECTION ---
st.write("")
st.markdown("### 🤝 P2P Energy Trading")
t1, t2, t3, t4 = st.columns(4)

trading_data = [
    ("Total Trading Today", "150.5 kWh", "#10b981"),
    ("Current Market Price", "4.20 THB", "#3b82f6"),
    ("Successful Transactions", "24 Deals", "#f59e0b"),
    ("Avoided Grid Cost", "632.10 THB", "#8b5cf6")
]

for i, (lab, val, col) in enumerate(trading_data):
    with [t1, t2, t3, t4][i]:
        st.markdown(f"""
            <div class="card-pro" style="border-left: 6px solid {col};">
                <small style="color:#64748b; font-weight:600;">{lab}</small><br>
                <b style="font-size:1.6rem; color:{col};">{val}</b>
            </div>
        """, unsafe_allow_html=True)

# --- 5. PERFORMANCE & ANALYTICS ---
st.write("")
st.divider()
left_col, right_col = st.columns([1.8, 1])

with left_col:
    st.markdown("### ⚡ 24-Hour Solar Production & Grid Mix")
    # กราฟรวมข้อมูล
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=np.random.normal(2000, 400, 24), name="Solar Gen", fill='tozeroy', line_color='#f59e0b'))
    fig.add_trace(go.Scatter(y=np.random.normal(1500, 200, 24), name="Grid Load", line_color='#ef4444'))
    fig.update_layout(height=400, margin=dict(l=0,r=0,t=10,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.markdown("### ✅ Station Details (Full List)")
    df = pd.DataFrame({
        "อาคาร (Station)": ["สนง.วิชาการฯ (35)", "บริหารธุรกิจ (32)", "อาคาร A (สำรอง)", "อาคาร B (สำรอง)", "เครื่องกล (G)", "เรียนรวม 7", "วิทยบริการฯ (4)", "หอประชุม (2)"],
        "kW Status": ["485.76", "400.00", "380.00", "365.00", "354.56", "314.24", "280.00", "250.00"]
    })
    st.table(df) # ข้อมูลครบทั้ง 8 สถานี
