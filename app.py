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

    /* ✅ ESG: คลีน ไม่มีกล่องว่าง จัดวางกึ่งกลางเป๊ะ */
    .esg-container { display: flex; flex-direction: column; align-items: center; text-align: center; }
    .esg-val { font-size: 3rem !important; font-weight: 800; color: #0f172a; margin-top: 10px; }
    .esg-lab { font-size: 1.1rem; color: #64748b; font-weight: 600; }

    /* Card Styling */
    .card-style { background: white; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .section-head { font-size: 1.3rem; font-weight: 700; color: #1e293b; margin: 20px 0 10px 0; border-left: 5px solid #2563eb; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER ---
h1, h2, h3 = st.columns([1, 4, 2])
with h1: st.image("rmut.png", width=150)
with h2:
    st.markdown('<p class="sub-title">AETHERA COMMAND PLATFORM</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#475569;">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</p>', unsafe_allow_html=True)
with h3:
    st.image("NetZero platform 1.png", width=250)
    st.markdown('<div style="background:#2563eb; color:white; padding:12px; border-radius:12px; text-align:center;">📍 KORAT: 33.3°C | Hum: 40%</div>', unsafe_allow_html=True)

# --- 3. ROW 1: ESG METRICS (NO EMPTY BOXES) ---
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

# --- 4. ROW 2: PERFORMANCE METRICS (RESTORED) ---
st.markdown('<div class="section-head">📊 Performance Metrics</div>', unsafe_allow_html=True)
p_cols = st.columns(6)
p_data = [("Real-Time (kW)", "2,854.56"), ("Total Yield (MW)", "54.47"), ("Peak Capacity (kW)", "2,854.56"), ("Daily Yield (MW)", "28.80"), ("Solar Capacity (kW)", "10"), ("P2P Volume Today", "80.3")]
for i, (l, v) in enumerate(p_data):
    with p_cols[i]:
        st.markdown(f'<div class="card-style"><small style="color:#64748b; font-weight:600;">{l}</small><br><b style="font-size:1.5rem; color:#1e293b;">{v}</b></div>', unsafe_allow_html=True)

# --- 5. ROW 3: P2P ENERGY TRADING ---
st.markdown('<div class="section-head">🤝 P2P Energy Trading</div>', unsafe_allow_html=True)
t_cols = st.columns(4)
t_data = [("Total Trading Today", "150.5 kWh", "#10b981"), ("Current Market Price", "4.20 THB", "#3b82f6"), ("Successful Transactions", "24 Deals", "#f59e0b"), ("Avoided Grid Cost", "632.10 THB", "#8b5cf6")]
for i, (l, v, c) in enumerate(t_data):
    with t_cols[i]:
        st.markdown(f'<div class="card-style" style="border-left:5px solid {c};"><small>{l}</small><br><b style="font-size:1.4rem; color:{c};">{v}</b></div>', unsafe_allow_html=True)

# --- 6. ROW 4: ANALYTICS GRID (GRAPHS & TABLES) ---
st.write("")
st.divider()
col_left, col_right = st.columns([1.5, 1])

with col_left:
    # 6.1 24-Hour Solar Production
    st.markdown('<div class="section-head">⚡ 24-Hour Solar Production Trend (kW)</div>', unsafe_allow_html=True)
    fig_prod = go.Figure(go.Scatter(y=np.random.normal(2000, 400, 24), fill='tozeroy', line_color='#f59e0b', fillcolor='rgba(245, 158, 11, 0.1)'))
    fig_prod.update_layout(height=280, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_prod, use_container_width=True)

    # 6.2 Today Power Mix
    st.markdown('<div class="section-head">⚡ Today Power Mix (kW)</div>', unsafe_allow_html=True)
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(50, 5, 24), name="Grid Load", fill='tozeroy', line_color='#ef4444', fillcolor='rgba(239, 68, 68, 0.1)'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(30, 3, 24), name="Solar Gen", fill='tozeroy', line_color='#3b82f6', fillcolor='rgba(59, 130, 246, 0.1)'))
    fig_mix.update_layout(height=280, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_mix, use_container_width=True)

with col_right:
    # 6.3 Station Details Table
    st.markdown('<div class="section-head">✅ Station Details (3 Central + 1 NRW)</div>', unsafe_allow_html=True)
    station_df = pd.DataFrame({
        "อาคาร (Station)": ["สนง.วิชาการฯ (35)", "บริหารธุรกิจ (32)", "อาคาร A (สำรอง)", "อาคาร B (สำรอง)", "เครื่องกล (G)", "เรียนรวม 7", "วิทยบริการฯ (4)", "หอประชุม (2)", "Sports Complex", "คณะเทคโนโลยีการเกษตร"],
        "kW": [485.76, 400.00, 380.00, 365.00, 354.56, 314.24, 280.00, 250.00, 200.00, 150.00]
    })
    st.table(station_df)

    # 6.4 Monthly Generation Bar Chart
    st.markdown('<div class="section-head">📊 Monthly Generation (MW)</div>', unsafe_allow_html=True)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    fig_bar = go.Figure(go.Bar(x=months, y=[450, 520, 610, 580, 490, 420], marker_color='#8b5cf6'))
    fig_bar.update_layout(height=200, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_bar, use_container_width=True)
