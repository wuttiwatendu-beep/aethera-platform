import streamlit as st
import pandas as pd
import numpy as np

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Cloud Sync", layout="wide")

# 2. ฟังก์ชันดึงข้อมูลจาก Google Sheets (หัวใจสำคัญ!)
def load_data_from_gsheets(url):
    # แปลงลิงก์ Google Sheets ให้เป็นลิงก์สำหรับดาวน์โหลด CSV
    csv_url = url.replace('/edit?usp=sharing', '/export?format=csv')
    return pd.read_csv(csv_url)

# --- 📍 ใส่ลิงก์ Google Sheets ของคุณนุที่นี่ครับ ---
SHEET_URL = "วางลิงก์ Google Sheets ของคุณนุตรงนี้" 

# 3. หัวข้อหลัก
st.markdown("<h1 style='text-align: center; color: #00A8E8;'>💎 AETHERA Cloud Database</h1>", unsafe_allow_html=True)

try:
    # ดึงข้อมูลจริงจากเมฆ!
    df = load_data_from_gsheets(SHEET_URL)
    
    st.success("✅ เชื่อมต่อฐานข้อมูล Google Cloud สำเร็จ")
    
    # 4. แสดงผล Dashboard จากข้อมูลจริง
    k1, k2 = st.columns(2)
    k1.metric("จำนวนสถานีในฐานข้อมูล", f"{len(df)} สถานี")
    k2.metric("ปริมาณไฟฟ้ารวม", f"{df['Energy_kWh'].sum():,.2f} kWh")
    
    st.write("### 📋 ตารางข้อมูลสถานี (ดึงมาจาก Google Sheets)")
    st.dataframe(df, use_container_width=True)
    
    st.write("### 📍 แผนที่พิกัดสถานีจริง")
    st.map(df[['lat', 'lon']])

except Exception as e:
    st.warning("📢 รอกราฟและข้อมูลจาก Google Sheets ของคุณนุอยู่นะครับ...")
    st.info("กรุณานำลิงก์จาก Google Sheets มาใส่ในโค้ดเพื่อเริ่มการ Sync ข้อมูลครับ")

# ส่วนแท็บอื่นๆ (บิล/แนวโน้ม) ก็จะทำงานต่อจากข้อมูล df นี้ได้เลยครับ
