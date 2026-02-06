import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# 1. ข้อมูลพื้นฐานและการคำนวณ
total_accumulated_mw = 54.473  # ค่าสะสมหน่วย MW
total_accumulated_kwh = total_accumulated_mw * 1000 # แปลงเป็น kWh เพื่อคำนวณ

# คำนวณค่าสิ่งแวดล้อมตามสูตร
co2_saved = total_accumulated_kwh * 0.0005   # หน่วย: Tons
coal_saved = total_accumulated_kwh * 0.0004  # หน่วย: Tons
trees_planted = int(total_accumulated_kwh / 80) # หน่วย: ต้น

# 2. จัดการ Layout และแสดงผล
st.set_page_config(layout="wide")

# ... (ส่วนของ CSS และ Header เหมือนเดิม) ...

# ส่วนของ Environment Benefits (ฝั่งขวาของ Dashboard)
with col_right:
    st.markdown("### 🌿 Environment Benefits (Accumulated)")
    
    # แสดงรูปภาพและค่าที่คำนวณได้
    ev_col1, ev_col2, ev_col3 = st.columns(3)
    
    with ev_col1:
        st.image("CO2.png", use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-weight:bold; color:#FF9100;'>{co2_saved:,.2f} Tons</p>", unsafe_allow_html=True)
        
    with ev_col2:
        st.image("Coal.png", use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-weight:bold; color:#FF9100;'>{coal_saved:,.2f} Tons</p>", unsafe_allow_html=True)
        
    with ev_col3:
        st.image("Tree.png", use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-weight:bold; color:#FF9100;'>{trees_planted:,.0f} Trees</p>", unsafe_allow_html=True)

    # ... (ส่วนของ Station Details ด้านล่าง) ...
