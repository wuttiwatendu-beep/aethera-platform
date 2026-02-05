import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Enterprise", layout="wide")

# 2. หัวข้อหลัก
st.markdown("<h1 style='text-align: center; color: #00A8E8;'>💎 AETHERA Cloud Sync</h1>", unsafe_allow_html=True)

# --- 📍 ใส่ลิงก์ Google Sheets ของคุณนุที่นี่ (ถ้ามี) ---
SHEET_URL = "" 

# 3. ฟังก์ชันดึงข้อมูล (ถ้าไม่มีลิงก์ ให้สร้างข้อมูลจำลองแทน)
def get_combined_data(url):
    if url and "google.com" in url:
        try:
            csv_url = url.replace('/edit?usp=sharing', '/export?format=csv')
            return pd.read_csv(csv_url), "Live Cloud Data ☁️"
        except:
            pass
    
    # ข้อมูลจำลอง (ถ้าเชื่อมต่อไม่ได้)
    np.random.seed(42)
    df_sim = pd.DataFrame({
        "Station": [f"ST-{i+1:02d}" for i in range(10)],
        "Type": ["Seller", "Buyer"] * 5,
        "Energy_kWh": [150, 120, 200, 180, 90, 100, 300, 250, 110, 130],
        "Base_Price": [3.5, 4.2, 3.2, 4.5, 3.8, 4.0, 3.1, 4.3, 3.4, 4.1],
        "lat": np.random.uniform(13.72, 13.82, 10),
        "lon": np.random.uniform(100.48, 100.60, 10)
    })
    return df_sim, "Simulation Mode 🛠️"

df, status_msg = get_combined_data(SHEET_URL)

# 4. แสดงสถานะและ KPI
st.info(f"สถานะระบบ: {status_msg}")
total_trade = df['Energy_kWh'].sum()
wheeling = 1.3103
income = total_trade * wheeling

c1, c2, c3 = st.columns(3)
c1.metric("พลังงานรวม", f"{total_trade:,.0f} kWh")
c2.metric("รายได้แพลตฟอร์ม", f"{income:,.2f} ฿")
c3.metric("จำนวนสถานี", len(df))

# 5. แท็บการใช้งาน
tab1, tab2, tab3 = st.tabs(["📊 วิเคราะห์ข้อมูล", "📍 แผนที่โครงข่าย", "📑 สรุปบิลวันนี้"])

with tab1:
    st.write("### 📈 ราคาเสนอซื้อ-ขาย")
    st.bar_chart(df.set_index('Station')['Base_Price'])

with tab2:
    st.write("### 📍 ตำแหน่งสถานี")
    st.map(df[['lat', 'lon']])

with tab3:
    st.write("### 📑 สรุปบิล")
    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 ดาวน์โหลดรายงาน (CSV)", data=csv, file_name="Aethera_Report.csv")

st.divider()
st.caption(f"Update: {datetime.now().strftime('%H:%M:%S')}")
