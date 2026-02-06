import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# --- 1. CORE CONFIG & PROFESSIONAL THEME ---
st.set_page_config(page_title="AETHERA COMMAND PLATFORM", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
    
    .main-title { font-size: 2.2rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 0px; }
    .sub-title { font-size: 1.1rem; font-weight: 600; color: #b43d8b; }

    /* ✅ ขยายขนาดตัวอักษร 200% ตามสั่ง */
    .agency-name { 
        font-size: 2.2rem !important; 
        font-weight: 700; 
        color: #1e3a8a; 
        margin-top: 10px;
        line-height: 1.4;
    }

    /* ESG: คลีน ไม่มีกล่องว่าง จัดวางกึ่งกลาง */
    .esg-container { display: flex; flex-direction: column; align-items: center; text-align: center; }
    .esg-val { font-size: 3rem !important; font-weight: 800; color: #0f172a; margin-top: 10px; }
    .esg-lab { font-size: 1.1rem; color: #64748b; font-weight: 600; }

    /* Card Styling */
    .card-style { background: white; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .section-head { font-size: 1.3rem; font-weight: 700; color: #1e293b; margin: 20px 0 10px 0; border-left: 5px solid #2563eb; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER SECTION ---
h1, h2, h3 = st.columns([1, 4, 2])
with h1: st.image("rmut.png", width=160)
with h2:
    st.markdown('<p class="sub-title">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    # ✅ ปรับขนาดตามที่คุณนุต้องการ
    st.markdown('<p class="agency-name">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)
with h3:
    st.image("NetZero platform 1.png", width=250)
    st.markdown('<div style="background:#2563eb; color:white; padding:15px; border-radius:12px; text-align:center; font-weight:600;">📍 KORAT: 33.3°C | Hum: 40%</div>', unsafe_allow_html=True)

# --- 3. ESG METRICS (CLEAN DESIGN) ---
st.write("")
b_col, c1, c2, c3 = st.columns([1.2, 2, 2, 2])
with b_col:
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    st.button("ESG Metrics", use_container_width=True, type="primary")

def draw_esg(col, img, val, lab):
    with col:
        st.markdown('<div class="esg-container">', unsafe_allow_html=True)
        st.image(img, width=140)
        st.markdown(f'<div class="esg-val">{val}</div><div class="esg-lab">{lab}</div></div>', unsafe_allow_html=True)

draw_esg(c1, "CO2.png", "27.24 T", "CO2 Saved")
draw_esg(c2, "Coal.png", "21.79 T", "Coal Saved")
draw_esg(c3, "Tree.png", "680", "Trees Planted")

# --- 4. PERFORMANCE & P2P METRICS (ALL RESTORED) ---
st.markdown('<div class="section-head">📊 Performance & Trading Insights</div>', unsafe_allow_html=True)
m_cols = st.columns(6)
m_data = [("Real-Time (kW)", "2,854.56"), ("Total Yield (MW)", "54.47"), ("Peak Capacity (kW)", "2,854.56"), ("Daily Yield (MW)", "28.80"), ("Solar Capacity (kW)", "10"), ("P2P Volume Today", "80.3")]
for i, (l, v) in enumerate(m_data):
    with m_cols[i]:
        st.markdown(f'<div class="card-style"><small style="color:#64748b; font-weight:600;">{l}</small><br><b style="font-size:1.5rem; color:#1e293b;">{v}</b></div>', unsafe_allow_html=True)

# --- 5. ANALYTICS GRID (GRAPHS & TABLES) ---
st.write("")
st.divider()
left, mid, right = st.columns([1.2, 1.2, 1])

with left:
    # 5.1 Solar Production Trend
    st.markdown('<div class="section-head">⚡ Solar Production Trend (kW)</div>', unsafe_allow_html=True)
    fig1 = go.Figure(go.Scatter(y=np.random.normal(2000, 400, 24), fill='tozeroy', line_color='#f59e0b'))
    fig1.update_layout(height=280, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1, use_container_width=True)

    # 5.2 Monthly Generation
    st.markdown('<div class="section-head">📊 Monthly Generation (MW)</div>', unsafe_allow_html=True)
    fig_bar = go.Figure(go.Bar(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], y=[450, 520, 610, 580, 490, 420], marker_color='#8b5cf6'))
    fig_bar.update_layout(height=200, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_bar, use_container_width=True)

with mid:
    # 5.3 Power Mix
    st.markdown('<div class="section-head">⚡ Today Power Mix (kW)</div>', unsafe_allow_html=True)
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(y=np.random.normal(50, 5, 24), name="Grid Load", fill='tozeroy', line_color='#ef4444'))
    fig2.add_trace(go.Scatter(y=np.random.normal(30, 3, 24), name="Solar Gen", fill='tozeroy', line_color='#3b82f6'))
    fig2.update_layout(height=280, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)

    # 5.4 P2P Stats
    st.markdown('<div class="section-head">🤝 Live P2P Status</div>', unsafe_allow_html=True)
    st.success("✅ Admin → Hub(1): 27.5 kWh")
    st.info("✅ Business(32) → Lib(4): 15.3 kWh")

with right:
    # 5.5 Station Details
    st.markdown('<div class="section-head">✅ Station Details</div>', unsafe_allow_html=True)
    df = pd.DataFrame({
        "อาคาร (Station)": ["สนง.วิชาการฯ", "บริหารธุรกิจ", "เครื่องกล (G)", "วิทยบริการฯ", "หอประชุม (2)", "Sports Complex", "คณะเทคโนโลยี"],
        "kW": [485.76, 400.00, 354.56, 280.00, 250.00, 200.00, 150.00]
    })
    st.table(df)
