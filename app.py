import streamlit as st
import pandas as pd
import numpy as np

# 1. ตั้งค่าหน้าเว็บให้กว้างและดูโปร
st.set_page_config(page_title="AETHERA Smart Platform", layout="wide")

# 2. หัวข้อหลัก (ใช้ HTML เพื่อความสวยงาม)
st.markdown("<h1 style='text-align: center; color: #00A8E8;'>💎 AETHERA Smart Energy Platform</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ระบบบริหารจัดการและแผนที่โครงข่ายซื้อขายไฟฟ้าอัจฉริยะ (P2P Grid)</p>", unsafe_allow_html=True)

# 3. แถบด้านข้างสำหรับปรับราคา (Sidebar)
st.sidebar.header("⚙️ การตั้งค่าราคาโครงข่าย")
t_fee = st.sidebar.slider("1. ค่าระบบส่ง (Transmission)", 0.1, 1.0, 0.28)
s_fee = st.sidebar.slider("2. ค่าความมั่นคง (Security)", 0.1, 1.0, 0.53)
p_fee = st.sidebar.slider("3. ค่าสนับสนุนนโยบาย (Policy)", 0.1, 1.0, 0.50)
total_wheeling = t_fee + s_fee + p_fee

st.sidebar.metric("รวม Wheeling Charge", f"{total_wheeling:.4f} ฿")
st.sidebar.divider()
st.sidebar.info("ลองปรับแถบเลื่อนเพื่อดูผลกระทบต่อราคาซื้อขายในระบบครับ")

# 4. สร้างฐานข้อมูลจำลอง 30 สถานี (รวมพิกัดแผนที่)
np.random.seed(42)
ids = [f"ST-{i+1:02d}" for i in range(30)]
types = np.random.choice(["Seller", "Buyer"], 30)
prices = np.random.uniform(2.5, 4.5, 30).round(2)
# สุ่มพิกัดให้อยู่ในเขตกรุงเทพฯ
lat = np.random.uniform(13.72, 13.82, 30)
lon = np.random.uniform(100.48, 100.60, 30)

df = pd.DataFrame({
    "Station": ids, 
    "Type": types, 
    "Price (฿)": prices,
    "lat": lat,
    "lon": lon
})

# 5. --- บล็อกที่ 1: กราฟราคา ---
st.write("### 📈 กราฟเปรียบเทียบราคาเสนอซื้อ-ขาย (30 สถานี)")
chart_df = df.pivot(index='Station', columns='Type', values='Price (฿)')
st.bar_chart(chart_df)

st.divider()

# 6. --- บล็อกที่ 2: แผนที่แสดงตำแหน่ง ---
st.write("### 📍 แผนที่แสดงพิกัดสถานีในเครือข่าย AETHERA")
# แสดงแผนที่ 30 จุด
st.map(df)

st.divider()

# 7. --- บล็อกที่ 3: ตารางการจับคู่ ---
st.write("### 🤝 สรุปการจับคู่ซื้อขายที่คุ้มค่าที่สุดในขณะนี้")
sellers = df[df['Type'] == "Seller"].sort_values("Price (฿)")
buyers = df[df['Type'] == "Buyer"].sort_values("Price (฿)", ascending=False)

match_list = []
for i in range(min(len(sellers), len(buyers))):
    s = sellers.iloc[i]
    b = buyers.iloc[i]
    match_list.append({
        "จากผู้ขาย": s['Station'],
        "ส่งให้ผู้ซื้อ": b['Station'],
        "ราคาต้นทาง": f"{s['Price (฿)']} ฿",
        "ราคาจ่ายรวมค่าส่ง": f"{s['Price (฿)'] + total_wheeling:.2f} ฿",
        "สถานะ": "⚡ Connected"
    })

st.table(pd.DataFrame(match_list).head(10))

# 8. สรุปท้ายหน้า
st.info(f"💡 สถานะปัจจุบัน: ออนไลน์ | จำนวนสถานี: 30 | ค่าธรรมเนียมรวม: {total_wheeling:.4f} บาท")
