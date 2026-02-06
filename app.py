import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าจอแบบกว้าง (Wide Mode) และชื่อแท็บ
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# --- CSS เพื่อความสวยงามและ Responsive ---
st.markdown("""
    <style>
    /* ปรับพื้นหลังหลัก */
    .main { background-color: #f4f7f9; }
    
    /* สไตล์กล่อง Card */
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* ปรับแต่งส่วนหัวของ Card */
    .card-container {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #e1e8ed;
        text-align: center;
        height: 100%;
    }
    
    .card-title {
        color: #004a7c;
        font-weight: bold;
        font-size: 1rem;
        margin-bottom: 10px;
    }
    
    .card-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #E85D04;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลโครงการ (จำลอง 10 Nodes)
df = pd.DataFrame([
    {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล", "kW": 354.56, "Zone": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
    {"อาคาร": "สำนักส่งเสริมวิชาการฯ (35)", "kW": 485.76, "Zone": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
    {"อาคาร": "คณะบริหารธุรกิจ (32)", "kW": 400.00, "Zone": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
    {"อาคาร": "สำนักวิทยบริการฯ (4)", "kW": 280.00, "Zone": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
    {"อาคาร": "หอประชุมวทัญญูฯ (2)", "kW": 250.00, "Zone": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
    {"อาคาร": "สำนักงานอธิการบดี (1)", "kW": 220.00, "Zone": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160},
    {"อาคาร": "Sports Complex", "kW": 150.00, "Zone": "ศูนย์กลาง", "Lat": 14.9940, "Lon": 102.1140},
    {"อาคาร": "อาคารเรียนรวม 7", "kW": 100.00, "Zone": "ศูนย์กลาง", "Lat": 14.9930, "Lon": 102.1145},
    {"อาคาร": "อาคาร A", "kW": 314.24, "Zone": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168},
    {"อาคาร": "อาคาร B", "kW": 300.00, "Zone": "ศูนย์กลาง", "Lat": 14.9900, "Lon": 102.1170}
])

# --- ส่วนโครงสร้างหน้าจอ (Top Bar) ---
header_col1, header_col2 = st.columns([1, 4])
with header_col1:
    # คุณนุสามารถใส่โลโก้มหาวิทยาลัยตรงนี้ได้ครับ
    st.write("") 
with header_col2:
    st.markdown("<h1 style='color: #004a7c; margin-bottom: 0;'>RMUTI AETHERA: Smart Grid Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666;'>Phase 1: Digital Twin & Environment Monitoring</p>", unsafe_allow_html=True)

st.write("---")

# --- การจัดวางแบบ Grid 2 ฝั่งหลัก ---
left_panel, right_panel = st.columns([1.2, 2])

# --- ฝั่งซ้าย: สถิติและข้อมูล (Environment & Tables) ---
with left_panel:
    st.markdown("### 🔵 Environment Benefits")
    # แบ่ง 3 คอลัมน์ย่อยข้างใน
    e_col1, e_col2, e_col3 = st.columns(3)
    
    with e_col1:
        st.markdown("<div class='card-container'><div class='card-title'>CO2 Saved</div>", unsafe_allow_html=True)
        st.image("CO2.png", use_container_width=True)
        st.markdown("<div class='card-value'>40.1</div></div>", unsafe_allow_html=True)
        
    with e_col2:
        st.markdown("<div class='card-container'><div class='card-title'>Coal Saved</div>", unsafe_allow_html=True)
        st.image("Coal.png", use_container_width=True)
        st.markdown("<div class='card-value'>21.9</div></div>", unsafe_allow_html=True)
        
    with e_col3:
        st.markdown("<div class='card-container'><div class='card-title'>Trees</div>", unsafe_allow_html=True)
        st.image("Tree.png", use_container_width=True)
        st.markdown("<div class='card-value'>1,507</div></div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("### 📊 Power Generation (kW)")
    # ตารางแบบสรุป
    st.dataframe(
        df[["อาคาร", "kW"]].sort_values(by="kW", ascending=False),
        hide_index=True,
        use_container_width=True,
        height=300
    )

# --- ฝั่งขวา: แผนที่ Digital Twin ---
with right_panel:
    st.markdown("### 🌐 Digital Twin Map (Real-time Locations)")
    fig = px.scatter_mapbox(
        df, lat="Lat", lon="Lon", 
        color="Zone", 
        size="kW",
        hover_name="อาคาร",
        zoom=11.2,
        height=620, # ปรับความสูงให้พอดีกับฝั่งซ้าย
        color_discrete_map={"หนองระเวียง": "#00A8E8", "ศูนย์กลาง": "#E85D04"},
        mapbox_style="carto-positron"
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

# --- Footer ---
st.markdown("---")
f_col1, f_col2 = st.columns(2)
with f_col1:
    st.caption("RMUTI Smart Grid Platform | Powered by AETHERA Team")
with f_col2:
    st.markdown("<p style='text-align: right; color: green;'>● System Online</p>", unsafe_allow_html=True)
