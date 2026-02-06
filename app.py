import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 1. Advanced Page Setup
st.set_page_config(page_title="RMUTI AETHERA | Command Center", layout="wide", initial_sidebar_state="expanded")

# Custom CSS เพื่อสร้าง UI แบบ Dark Mode ผสม Modern Light (Professional Look)
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #0e1117; color: white; }
    .metric-card {
        background-color: #ffffff; border-radius: 12px; padding: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-left: 5px solid #1e3a8a;
    }
    .stPlotlyChart { border-radius: 15px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
    h1, h2, h3 { font-family: 'Inter', sans-serif; font-weight: 700; color: #1e3a8a; }
    </style>
    """, unsafe_allow_html=True)

# 2. Data Preparation (เฉพาะอาคาร G ในโซนหนองระเวียง)
df_stations = pd.DataFrame([
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง"}
])

# 3. Sidebar: Control & Secondary Info
with st.sidebar:
    st.image("https://www.rmuti.ac.th/main/wp-content/uploads/2019/09/Logo-RMUTI-Standard.png", width=100)
    st.title("AETHERA Control")
    st.markdown("---")
    st.subheader("🤝 Live Market P2P")
    st.info("⚡ Admin → Hall (2)\n12.5 kWh | 3.8฿")
    st.info("⚡ Bus (32) → Lib (4)\n25.0 kWh | 4.0฿")
    st.markdown("---")
    st.write("📅 Last Sync: Today 13:00")

# 4. Main Dashboard Header
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Live Solar Power", "2,854.56 kW", "↑ 12%")
with m2: st.metric("Total Yield", "54.473 MW", "Cumulative")
with m3: st.metric("Grid Reliance", "15.2 %", "-2.4%", delta_color="inverse")
with m4: st.metric("Daily Savings", "฿ 1,420.50", "P2P Profit")

st.markdown("---")

# 5. Grid Layout: 2 Rows, 2 Columns
row1_left, row1_right = st.columns([2, 1])

with row1_left:
    st.markdown("### ⚡ Smart Energy Flow Control (Real-time)")
    # Sankey ที่มีมิติและระบุหน่วยชัดเจน
    fig_flow = go.Figure(data=[go.Sankey(
        node = dict(pad=30, thickness=25, 
                   label=["Solar PV (kW)", "PEA Grid (kW)", "RMUTI Smart Load (kW)"],
                   color=["#fbbf24", "#ef4444", "#1e3a8a"]),
        link = dict(source=[0, 1], target=[2, 2], value=[2854.56, 500],
                   color=["rgba(251, 191, 36, 0.4)", "rgba(239, 68, 68, 0.3)"])
    )])
    fig_flow.update_layout(height=380, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig_flow, use_container_width=True)

with row1_right:
    st.markdown("### 🌿 ESG Impact")
    # จัดวางรูปภาพ CO2, Coal, Tree ให้ดูสมดุล
    e_col1, e_col2 = st.columns(2)
    with e_col1:
        st.image("CO2.png", width=100)
        st.write("**27.24 t** CO2 Saved")
    with e_col2:
        st.image("Coal.png", width=100)
        st.write("**21.79 t** Coal Saved")
    st.image("Tree.png", width=100)
    st.write("**680** Trees Equivalent")

st.markdown("---")

row2_left, row2_right = st.columns([1, 1])

with row2_left:
    st.markdown("### 📈 Power Performance Trend")
    # กราฟ Area แบบไล่เฉดสี
    df_trend = pd.DataFrame({"Time": range(24), "kW": np.random.normal(2000, 50, 24)})
    fig_line = px.area(df_trend, x="Time", y="kW", color_discrete_sequence=['#fbbf24'])
    fig_line.update_layout(height=300, yaxis_title="Power (kW)")
    st.plotly_chart(fig_line, use_container_width=True)

with row2_right:
    st.markdown("### 📊 Top Station Breakdown")
    # ตารางที่ปรับแต่งให้ดูแพง
    st.table(df_stations.head(6))
