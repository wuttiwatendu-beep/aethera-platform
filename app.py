import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# --- CONFIG & DATA ---
st.set_page_config(page_title="RMUTI Smart Grid & P2P", layout="wide")

# ข้อมูล P2P Trading จำลอง (เฉพาะศูนย์กลาง)
df_p2p = pd.DataFrame([
    {"Time": "10:30", "Seller": "สำนักงานอธิการบดี (1)", "Buyer": "หอประชุมวทัญญูฯ (2)", "Amount (kWh)": 15.5, "Price (฿)": 4.2},
    {"Time": "11:15", "Seller": "คณะบริหารธุรกิจ (32)", "Buyer": "สำนักวิทยบริการฯ (4)", "Amount (kWh)": 22.0, "Price (฿)": 4.1},
    {"Time": "12:00", "Seller": "สำนักส่งเสริมวิชาการฯ (35)", "Buyer": "Sports Complex", "Amount (kWh)": 45.2, "Price (฿)": 3.9},
])

# ... (ข้อมูล df_nodes และการคำนวณเดิมคงไว้) ...

# --- UI LAYOUT ---
st.markdown("<h2 style='text-align: center; color: #004a7c;'>🏛️ RMUTI AETHERA: Smart Grid & P2P Trading</h2>", unsafe_allow_html=True)

# ส่วนที่ 1: Metric Cards (เพิ่ม P2P Metric)
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Real Time Power", f"{realtime_sum:,.2f} kW")
with m2: st.metric("Total Production", f"54.473 MW")
with m3: st.metric("Total Capacity", f"2,854.56 MW")
with m4: st.metric("P2P Traded Today", "82.7 kWh", delta="12% vs Yesterday")

st.write("---")

# ส่วนที่ 2: Dashboard Content
col_main, col_p2p = st.columns([1.5, 1])

with col_main:
    # แสดงแผนที่เดิมที่มีอยู่
    st.markdown("### 🌐 Digital Twin & P2P Network")
    fig_map = px.scatter_mapbox(df_nodes, lat="Lat", lon="Lon", color="Zone", size="kW",
                                zoom=14, height=450, mapbox_style="carto-positron",
                                title="Trading Nodes at Central Campus")
    st.plotly_chart(fig_map, use_container_width=True)
    
    # กราฟราคาตลาด P2P
    st.markdown("### 💹 Market Energy Price (P2P)")
    price_data = pd.DataFrame({
        "Time": [f"{h:02d}:00" for h in range(7, 18)],
        "Price (Baht)": [4.5, 4.4, 4.2, 4.0, 3.8, 3.7, 3.8, 3.9, 4.1, 4.3, 4.5]
    })
    fig_price = px.line(price_data, x="Time", y="Price (Baht)", markers=True)
    fig_price.update_traces(line_color='#2ECC71')
    st.plotly_chart(fig_price, use_container_width=True)

with col_p2p:
    st.markdown("### 🤝 Live P2P Transactions")
    st.success("Current Market Status: **Open**")
    
    # แสดงรายการเทรดล่าสุด
    for index, row in df_p2p.iterrows():
        with st.container():
            st.markdown(f"""
            <div style="background-color: white; padding: 10px; border-radius: 10px; border-left: 5px solid #2ECC71; margin-bottom: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
                <small>{row['Time']}</small><br>
                <b>{row['Seller']}</b> ➡️ <b>{row['Buyer']}</b><br>
                <span style="color: #2ECC71;">{row['Amount (kWh)']} kWh</span> | <span style="color: #004a7c;">฿{row['Price (฿)']} / Unit</span>
            </div>
            """, unsafe_allow_html=True)
    
    st.write("---")
    # สรุปประหยัดเงิน
    st.markdown("### 💰 Cost Saving")
    st.info("วันนี้มหาวิทยาลัยประหยัดค่าไฟจากการเทรดกันเองได้: **฿1,245.50**")
    
    # ส่วนของ Environment เดิม
    st.markdown("### 🌿 Env Impact")
    e1, e2 = st.columns(2)
    with e1: st.write(f"CO2: {co2_saved:.1f} t")
    with e2: st.write(f"Trees: {trees_planted}")

st.caption("RMUTI Smart Campus | Peer-to-Peer Energy Trading Module Enabled")
