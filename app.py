import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Energy Network", layout="wide")

# CSS สำหรับปรับแต่งความสวยงามและ Animation
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    .stMetric { background-color: #1e293b; padding: 15px; border-radius: 12px; border: 1px solid #334155; }
    div[data-testid="stMetricValue"] { color: #E85D04; }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (Master Data)
data = [
    {"Bldg": "อาคาร G (หนองระเวียง)", "kW": 354.56, "Lat": 14.9435, "Lon": 102.2140, "Type": "Source"},
    {"Bldg": "อาคาร 35 (ทะเบียน)", "kW": 485.76, "Lat": 14.9922, "Lon": 102.1162, "Type": "Source"},
    {"Bldg": "อาคาร 32 (บริหาร)", "kW": 400.00, "Lat": 14.9925, "Lon": 102.1155, "Type": "P2P"},
    {"Bldg": "อาคาร 4 (วิทยบริการ)", "kW": 280.00, "Lat": 14.9910, "Lon": 102.1165, "Type": "P2P"},
    {"Bldg": "อาคาร 2 (หอประชุม)", "kW": 250.00, "Lat": 14.9905, "Lon": 102.1158, "Type": "P2P"},
    {"Bldg": "อาคาร 1 (อธิการบดี)", "kW": 220.00, "Lat": 14.9915, "Lon": 102.1160, "Type": "P2P"},
    {"Bldg": "Sports Complex", "kW": 150.00, "Lat": 14.9940, "Lon": 102.1140, "Type": "P2P"},
    {"Bldg": "อาคาร A", "kW": 314.24, "Lat": 14.9935, "Lon": 102.1168, "Type": "P2P"},
    {"Bldg": "อาคาร B", "kW": 300.00, "Lat": 14.9900, "Lon": 102.1170, "Type": "P2P"},
    {"Bldg": "อาคาร 7 (เรียนรวม)", "kW": 100.00, "Lat": 14.9930, "Lon": 102.1145, "Type": "P2P"}
]
df = pd.DataFrame(data)

# 3. ส่วนหัวข้อโครงการ
st.title("🌐 RMUTI AETHERA: Smart Grid Energy Flow")
st.write("การเชื่อมโยงโครงข่ายพลังงานอัจฉริยะระหว่าง 2 วิทยาเขต (Phase 1)")

# 4. สร้างกราฟิก Network Flow ด้วย Plotly
fig = go.Figure()

# วาดเส้นเชื่อมโยง (Energy Flow Lines) จากแหล่งผลิตหลักไปยังจุดต่างๆ
source_node = df.iloc[0] # อาคาร G หนองระเวียง
for i in range(1, len(df)):
    fig.add_trace(go.Scattermapbox(
        mode = "lines",
        lon = [source_node['Lon'], df.iloc[i]['Lon']],
        lat = [source_node['Lat'], df.iloc[i]['Lat']],
        line = dict(width = 1.5, color = '#E85D04'),
        opacity = 0.3,
        hoverinfo = 'none'
    ))

# วาดจุดสถานี (Nodes)
fig.add_trace(go.Scattermapbox(
    lat=df['Lat'], lon=df['Lon'],
    mode='markers+text',
    marker=go.scattermapbox.Marker(
        size=df['kW']/15, 
        color=['#00ff00' if t == 'Source' else '#E85D04' for t in df['Type']],
        opacity=0.8
    ),
    text=df['Bldg'],
    textposition="top right",
    hoverinfo='text'
))

fig.update_layout(
    mapbox=dict(style="carto-darkmatter", zoom=11, center=dict(lat=14.97, lon=102.16)),
    margin={"r":0,"t":0,"l":0,"b":0}, height=600, showlegend=False
)

# 5. การจัด Layout แบ่งส่วนหน้าจอ
col_left, col_right = st.columns([2, 1])

with col_left:
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("📊 ระบบวิเคราะห์พลังงาน")
    st.metric("Total Generation", "2.85 MW", "+12% จากเป้าหมาย")
    st.metric("P2P Active Trades", "14 Matchings", "Live")
    
    st.write("---")
    st.write("**สถานะการส่งไฟ (Live Flow)**")
    for _, row in df.head(5).iterrows():
        c1, c2 = st.columns([3,1])
        c1.caption(row['Bldg'])
        c2.write(f"🟢 {row['kW']} kW")
        st.progress(np.random.randint(30, 95))

st.success("🚀 ระบบพร้อมสำหรับการนำเสนอ Digital Twin ต่อคณะกรรมการ")
