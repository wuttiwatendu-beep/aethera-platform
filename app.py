import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Smart Grid", layout="wide")

# CSS ตกแต่งให้โทนสว่างและพรีเมียม
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .env-box {
        text-align: center;
        padding: 15px;
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    h1 { color: #E85D04 !important; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (9+1 Nodes)
df = pd.DataFrame([
    {"Bldg": "อาคาร G (หนองระเวียง)", "kW": 354.56, "Zone": "Nong Rawiang", "Lat": 14.9435, "Lon": 102.2140},
    {"Bldg": "อาคาร 35 (ทะเบียน)", "kW": 485.76, "Zone": "Main Campus", "Lat": 14.9922, "Lon": 102.1162},
    {"Bldg": "อาคาร 32 (บริหาร)", "kW": 400.00, "Zone": "Main Campus", "Lat": 14.9925, "Lon": 102.1155},
    {"Bldg": "อาคาร 4 (วิทยบริการ)", "kW": 280.00, "Zone": "Main Campus", "Lat": 14.9910, "Lon": 102.1165},
    {"Bldg": "อาคาร 2 (หอประชุม)", "kW": 250.00, "Zone": "Main Campus", "Lat": 14.9905, "Lon": 102.1158},
    {"Bldg": "อาคาร 1 (อธิการบดี)", "kW": 220.00, "Zone": "Main Campus", "Lat": 14.9915, "Lon": 102.1160},
    {"Bldg": "Sports Complex", "kW": 150.00, "Zone": "Main Campus", "Lat": 14.9940, "Lon": 102.1140},
    {"Bldg": "อาคารเรียนรวม 7", "kW": 100.00, "Zone": "Main Campus", "Lat": 14.9930, "Lon": 102.1145},
    {"Bldg": "อาคาร A", "kW": 314.24, "Zone": "Main Campus", "Lat": 14.9935, "Lon": 102.1168},
    {"Bldg": "อาคาร B", "kW": 300.00, "Zone": "Main Campus", "Lat": 14.9900, "Lon": 102.1170}
])

# --- HEADER ---
st.title("🏛️ RMUTI AETHERA: Smart University Grid")
st.write("ระบบบริหารจัดการพลังงาน Phase 1 (มีนาคม 2569)")

st.divider()

# --- ส่วนที่ 1: Environment Benefits (ดึงรูปจาก Link ตรง) ---
st.markdown("<h3 style='text-align: center; color: #006699;'>🔵 Environment Benefits</h3>", unsafe_allow_html=True)
e1, e2, e3 = st.columns(3)

with e1:
    st.markdown("<div class='env-box'>", unsafe_allow_html=True)
    st.write("**CO2 Emission Saved**")
    # รูปเมฆ CO2
    st.image("https://cdn-icons-png.flaticon.com/512/2683/2683833.png", width=120)
    st.metric("", "40.13 tons")
    st.markdown("</div>", unsafe_allow_html=True)

with e2:
    st.markdown("<div class='env-box'>", unsafe_allow_html=True)
    st.write("**Standard Coal Saved**")
    # รูปถ่านหิน/ประหยัดพลังงาน
    st.image("https://cdn-icons-png.flaticon.com/512/3569/3569724.png", width=120)
    st.metric("", "21.93 tons")
    st.markdown("</div>", unsafe_allow_html=True)

with e3:
    st.markdown("<div class='env-box'>", unsafe_allow_html=True)
    st.write("**Equivalent Trees Planted**")
    # รูปต้นไม้
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=120)
    st.metric("", "1,507 trees")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# --- ส่วนที่ 2: แผนที่และกราฟ ---
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("🌐 Digital Twin Map")
    fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", color="Zone", size="kW",
                            hover_name="Bldg", zoom=11.2, height=450,
                            color_discrete_map={"Nong Rawiang": "#00A8E8", "Main Campus": "#E85D04"},
                            mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("📊 Generation Details")
    st.bar_chart(df.set_index("Bldg")["kW"])
    st.dataframe(df[["Bldg", "kW"]].sort_values("kW", ascending=False), hide_index=True)

# --- ส่วนที่ 3: P2P Trading ---
st.divider()
st.subheader("🤝 Smart P2P Trading (Simulation)")
t_col1, t_col2 = st.columns(2)
with t_col1:
    st.table(pd.DataFrame({
        "Seller (ผู้ส่ง)": ["อาคาร 35", "อาคาร G", "อาคาร 32"],
        "Buyer (ผู้รับ)": ["อธิการบดี", "อาคาร 4", "หอประชุม"],
        "Amount": ["45.2 kWh", "122.5 kWh", "60.0 kWh"]
    }))
with t_col2:
    st.success("ROI Estimation: 4.5 Years")
    st.info("Status: สำรวจหน้างานแล้ว 100%")
    st.progress(25)

st.caption("RMUTI Smart Grid Platform by AETHERA")
