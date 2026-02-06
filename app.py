import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import numpy as np

# --- 1. CORE STYLING & PAGE CONFIG ---
st.set_page_config(page_title="AETHERA COMMAND PLATFORM", layout="wide")

st.markdown("""
    <style>
    /* Professional Font & Background */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8fafc; }

    /* Header & Typography */
    .header-container { padding: 1rem 0; }
    .main-title { font-size: 2.2rem !important; font-weight: 800; color: #1e3a8a; line-height: 1.2; margin-bottom: 0.2rem; }
    .sub-title { font-size: 1.2rem; font-weight: 600; color: #b43d8b; margin-bottom: 0.1rem; }
    .location-text { font-size: 1.1rem; color: #475569; font-weight: 500; }

    /* ✅ ESG Metric Cards: Centered & Large */
    .esg-card {
        background: white;
        padding: 2.5rem 1rem;
        border-radius: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        text-align: center;
        height: 100%;
    }
    .esg-value { font-size: 2.8rem; font-weight: 800; color: #0f172a; margin-top: 1rem; }
    .esg-label { font-size: 1.1rem; color: #64748b; font-weight: 600; letter-spacing: 0.5px; }

    /* Analytics Section Styling */
    .section-header { font-size: 1.3rem; font-weight: 700; color: #1e293b; margin: 1.5rem 0 1rem 0; border-left: 5px solid #2563eb; padding-left: 10px; }
    .metric-box { background: white; padding: 1rem; border-radius: 1rem; border: 1px solid #e2e8f0; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA UTILITIES ---
def get_korat_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=14.97&longitude=102.10&current=temperature_2m,relative_humidity_2m"
        data = requests.get(url, timeout=5).json()['current']
        return data
    except: return {"temperature_2m": 33.3, "relative_humidity_2m": 40}

weather = get_korat_weather()

# --- 3. TOP BAR: LOGO & IDENTITY ---
col_logo, col_title, col_netzero = st.columns([1, 4, 2])

with col_logo:
    st.image("rmut.png", width=150)

with col_title:
    st.markdown("""
        <div class="header-container">
            <div class="sub-title">AETHERA COMMAND PLATFORM</div>
            <div class="main-title">โครงการติดตั้งระบบไฟฟ้าจากพลังงานแสงอาทิตย์</div>
            <div class="location-text">มทร.อีสาน ศูนย์กลางนครราชสีมา และ ศูนย์การศึกษาหนองระเวียง</div>
        </div>
    """, unsafe_allow_html=True)

with col_netzero:
    st.image("NetZero platform 1.png", width=260)
    st.markdown(f"""
        <div style="background: #2563eb; color: white; padding: 12px; border-radius: 12px; margin-top: 10px;">
            <div style="font-size: 0.8rem; font-weight: 600; opacity: 0.9;">📍 NAKHON RATCHASIMA WEATHER</div>
            <div style="font-size: 1.8rem; font-weight: 800;">{weather['temperature_2m']}°C</div>
            <div style="font-size: 0.8rem; opacity: 0.8;">Humidity: {weather['relative_humidity_2m']}% | Wind: 5.6 km/h</div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. PRIMARY METRICS (ESG) ---
st.write("")
col_btn, col1, col2, col3 = st.columns([1, 2, 2, 2])

with col_btn:
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    st.button("ESG Metrics", use_container_width=True, type="secondary")

def create_esg_card(column, img_path, val, lab):
    with column:
        st.markdown(f"""<div class="esg-card">""", unsafe_allow_html=True)
        st.image(img_path, width=130) # ขยายรูปไอคอนให้ใหญ่ชัดเจนและกึ่งกลาง
        st.markdown(f"""<div class="esg-value">{val}</div><div class="esg-label">{lab}</div></div>""", unsafe_allow_html=True)

create_esg_card(col1, "CO2.png", "27.24 T", "CO2 Saved")
create_esg_card(col2, "Coal.png", "21.79 T", "Coal Saved")
create_esg_card(col3, "Tree.png", "680", "Trees Planted")

# --- 5. PERFORMANCE SUMMARY GRID ---
st.markdown("<div class='section-header'>3: Performance Metrics</div>", unsafe_allow_html=True)
m = st.columns(6)
m_data = [
    ("Real-Time (kW)", "2,854.56"), ("Total Yield (MW)", "54.47"),
    ("Peak Capacity (kW)", "2,854.56"), ("Daily Yield (MW)", "28.80"),
    ("Solar Capacity (kW)", "10"), ("P2P Volume Today", "80.3")
]
for i, (label, value) in enumerate(m_data):
    with m[i]:
        st.markdown(f"""<div class="metric-box"><div style="color: #64748b; font-size: 0.85rem; font-weight: 600;">{label}</div>
        <div style="font-size: 1.4rem; font-weight: 800; color: #1e293b;">{value}</div></div>""", unsafe_allow_html=True)

# --- 6. ADVANCED ANALYTICS (Charts & Tables) ---
st.write("")
st.divider()
left_pane, right_pane = st.columns([1.8, 1])

with left_pane:
    # กราฟการผลิต
    st.markdown("<div class='section-header'>⚡ 24-Hour Solar Production (kW)</div>", unsafe_allow_html=True)
    fig_prod = go.Figure(go.Scatter(x=list(range(24)), y=np.random.normal(1600, 400, 24), fill='tozeroy', line_color='#f59e0b', fillcolor='rgba(245, 158, 11, 0.15)'))
    fig_prod.update_layout(height=280, margin=dict(l=0,r=0,t=10,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_prod, use_container_width=True)

    # กราฟ Power Mix
    st.markdown("<div class='section-header'>📊 Today Power Mix (kW)</div>", unsafe_allow_html=True)
    fig_mix = go.Figure()
    fig_mix.add_trace(go.Scatter(y=np.random.normal(42, 3, 24), name="Grid Load", fill='tozeroy', line_color='#ef4444', fillcolor='rgba(239, 68, 68, 0.1)'))
    fig_mix.add_trace(go.Scatter(y=np.random.normal(24, 2, 24), name="Solar Generation", fill='tozeroy', line_color='#3b82f6', fillcolor='rgba(59, 130, 246, 0.1)'))
    fig_mix.update_layout(height=280, margin=dict(l=0,r=0,t=10,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig_mix, use_container_width=True)

with right_pane:
    # ตารางสถานีครบ 8 แห่ง
    st.markdown("<div class='section-header'>✅ Station Details (Full List)</div>", unsafe_allow_html=True)
    station_df = pd.DataFrame({
        "อาคาร (Station)": ["สนง.วิชาการฯ (35)", "บริหารธุรกิจ (32)", "อาคาร A (สำรอง)", "อาคาร B (สำรอง)", "เครื่องกล (G)", "เรียนรวม 7", "วิทยบริการฯ (4)", "หอประชุม (2)"],
        "kW Capacity": [485.76, 400.00, 380.00, 365.00, 354.56, 314.24, 280.00, 250.00]
    })
    st.table(station_df)
