import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Setup & Custom CSS สำหรับขยายขนาดตัวอักษรทั่วทั้งหน้าจอ
st.set_page_config(page_title="RMUTI AETHERA", layout="wide")

st.markdown("""
    <style>
    /* ขยายขนาดตัวอักษรหลัก */
    html, body, [class*="css"]  {
        font-size: 1.1rem; 
    }
    /* ปรับแต่ง Metric ให้ตัวเลขใหญ่สะใจ */
    [data-testid="stMetricValue"] {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        color: #1e3a8a;
    }
    [data-testid="stMetricLabel"] {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
    }
    /* ปรับแต่งหัวข้อ */
    h1 { font-size: 3.5rem !important; }
    h2 { font-size: 2.5rem !important; }
    h3 { font-size: 1.8rem !important; }
    
    /* ปรับตารางให้ตัวหนังสือใหญ่ขึ้น */
    .stDataFrame div[data-testid="stTable"] {
        font-size: 1.2rem !font-important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (เน้นอาคาร G 354.56 kW โซนหนองระเวียง)
df_stations = pd.DataFrame([
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง"},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 314.24, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง"},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง"},
])

# 3. ส่วนหัว (Header) พร้อมโลโก้ขนาดใหญ่ขึ้น
head_left, head_right = st.columns([1, 4])
with head_left:
    try: st.image("rmut.png", width=180) # ขยายโลโก้ให้เด่น
    except: st.title("🏛️")
with head_right:
    st.markdown("<h1 style='margin-top: 20px;'>RMUTI AETHERA PLATFORM</h1>", unsafe_allow_html=True)
    st.markdown("### Smart Grid Management System")

st.write("---")

# 4. Key Metrics (ตัวเลขใหญ่พิเศษ)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Real-Time (kW)", "2,854.56")
m2.metric("Total Yield (MW)", "54.473")
m3.metric("Capacity (kW)", "2,854.56")
m4.metric("P2P Volume (kWh)", "80.3")

st.write("---")

# 5. Main Content Area
col_graph, col_esg, col_table = st.columns([1.5, 0.8, 1.2])

with col_graph:
    st.markdown("### ⚡ Power Distribution (kW)")
    fig = go.Figure(data=[
        go.Bar(name='Solar', x=['Load'], y=[2854.56], marker_color='#f59e0b', text="2,854 kW", textfont=dict(size=18)),
        go.Bar(name='Grid', x=['Load'], y=[500], marker_color='#ef4444', text="500 kW", textfont=dict(size=18))
    ])
    fig.update_layout(barmode='stack', height=500, font=dict(size=16)) # ขยายกราฟ
    st.plotly_chart(fig, use_container_width=True)

with col_esg:
    st.markdown("### 🌿 ESG Impact")
    # ขยายรูปและตัวเลข ESG
    try:
        st.image("CO2.png", width=120)
        st.markdown("## 27.24 T <br> <small>CO2 Saved</small>", unsafe_allow_html=True)
        st.write("")
        st.image("Coal.png", width=120)
        st.markdown("## 21.79 T <br> <small>Coal Saved</small>", unsafe_allow_html=True)
        st.write("")
        st.image("Tree.png", width=120)
        st.markdown("## 680 <br> <small>Trees Planted</small>", unsafe_allow_html=True)
    except:
        st.info("💡 Files: CO2.png, Coal.png, Tree.png")

with col_table:
    st.markdown("### 📊 Station Details (kW)")
    # ปรับแต่งตารางให้ดูง่ายและตัวอักษรใหญ่
    st.table(df_stations)

st.write("---")

# 6. P2P History (ตัวอักษรใหญ่ชัดเจน)
st.markdown("### 🤝 Live P2P Trading History")
st.success("### ✅ Admin → Hall (อาคาร 2) : 12.5 kWh | 3.8฿")
st.success("### ✅ Business (32) → Lib (4) : 25.0 kWh | 4.0฿")
