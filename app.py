import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Platform", layout="wide")

# 2. สร้าง Sidebar สำหรับเลือกโปรเจกต์
st.sidebar.title("🚀 เลือกโครงการ")
project_mode = st.sidebar.radio("ไปที่หน้า:", ["มทร. อีสาน (9+1 Nodes)", "ระบบทดสอบเดิม (30 Nodes)"])

# ---------------------------------------------------------
# MODE 1: มทร. อีสาน (งานจริง Phase 1)
# ---------------------------------------------------------
if project_mode == "มทร. อีสาน (9+1 Nodes)":
    st.markdown("<h1 style='color: #E85D04;'>🏫 RMUTI Smart Grid (Phase 1)</h1>", unsafe_allow_html=True)
    
    # ข้อมูลจริงจากเอกสาร
    rmuti_data = [
        {"อาคาร": "G กลุ่มวิชาชีพเครื่องกล (หนองระเวียง)", "kW": 354.56, "Group": "หนองระเวียง", "Lat": 14.9435, "Lon": 102.2140},
        {"อาคาร": "สำนักส่งเสริมวิชาการฯ (อาคาร 35)", "kW": 485.76, "Group": "ศูนย์กลาง", "Lat": 14.9922, "Lon": 102.1162},
        {"อาคาร": "คณะบริหารธุรกิจ (อาคาร 32)", "kW": 400.00, "Group": "ศูนย์กลาง", "Lat": 14.9925, "Lon": 102.1155},
        {"อาคาร": "สำนักวิทยบริการฯ (อาคาร 4)", "kW": 280.00, "Group": "ศูนย์กลาง", "Lat": 14.9910, "Lon": 102.1165},
        {"อาคาร": "หอประชุมวทัญญูฯ (อาคาร 2)", "kW": 250.00, "Group": "ศูนย์กลาง", "Lat": 14.9905, "Lon": 102.1158},
        {"อาคาร": "สำนักงานอธิการบดี (อาคาร 1)", "kW": 220.00, "Group": "ศูนย์กลาง", "Lat": 14.9915, "Lon": 102.1160},
        {"อาคาร": "Sports Complex (Gym)", "kW": 150.00, "Group": "ศูนย์กลาง", "Lat": 14.9940, "Lon": 102.1140},
        {"อาคาร": "อาคารเรียนรวม (อาคาร 7)", "kW": 100.00, "Group": "ศูนย์กลาง", "Lat": 14.9930, "Lon": 102.1145},
        {"อาคาร": "อาคาร A (เพิ่มใหม่)", "kW": 314.24, "Group": "ศูนย์กลาง", "Lat": 14.9935, "Lon": 102.1168},
        {"อาคาร": "อาคาร B (เพิ่มใหม่)", "kW": 300.00, "Group": "ศูนย์กลาง", "Lat": 14.9900, "Lon": 102.1170},
    ]
    df_rmuti = pd.DataFrame(rmuti_data)
    
    # สรุปผล มทร.
    st.metric("Total Capacity", f"{(df_rmuti['kW'].sum()/1000):.2f} MW")
    
    fig_rmuti = px.scatter_mapbox(df_rmuti, lat="Lat", lon="Lon", color="Group", size="kW",
                                 hover_name="อาคาร", zoom=11, height=500, mapbox_style="carto-positron")
    st.plotly_chart(fig_rmuti, use_container_width=True)
    st.table(df_rmuti[['อาคาร', 'kW', 'Group']])

# ---------------------------------------------------------
# MODE 2: ระบบทดสอบเดิม (30 Nodes เมื่อวาน)
# ---------------------------------------------------------
else:
    st.markdown("<h1 style='color: #00A8E8;'>💎 AETHERA Global Test Net</h1>", unsafe_allow_html=True)
    st.write("โหมดจำลองสถานีทดสอบ 30 Nodes สำหรับรันระบบ Matching ราคา")
    
    # สร้างข้อมูลสุ่ม 30 สถานีเหมือนเมื่อวาน
    np.random.seed(42)
    df_test = pd.DataFrame({
        "Station": [f"ST-{i+1:02d}" for i in range(30)],
        "Type": np.random.choice(["Seller", "Buyer"], 30),
        "Price": np.random.uniform(2.5, 4.5, 30).round(2),
        "Lat": np.random.uniform(13.7, 13.9, 30),
        "Lon": np.random.uniform(100.4, 100.6, 30)
    })
    
    # กราฟราคา
    st.bar_chart(df_test.pivot(index='Station', columns='Type', values='Price'))
    
    # แผนที่ 30 จุด
    fig_test = px.scatter_mapbox(df_test, lat="Lat", lon="Lon", color="Type", size="Price",
                                zoom=10, height=500, mapbox_style="carto-positron")
    st.plotly_chart(fig_test, use_container_width=True)
    
    # ตาราง Matching
    st.write("🤝 Matching Summary (30 Nodes)")
    st.dataframe(df_test.head(10))

st.sidebar.info("คุณนุสามารถสลับหน้าไปมาได้ ข้อมูลไม่หายครับ!")
