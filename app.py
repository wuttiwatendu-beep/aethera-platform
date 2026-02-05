import streamlit as st
import pandas as pd
import numpy as np

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Professional Dashboard", layout="wide")

# 2. หัวข้อหลักพร้อมสไตล์ (แก้คำสะกดตรง unsafe_allow_html)
st.markdown("<h1 style='text-align: center; color: #00A8E8;'>💎 AETHERA Smart Energy Platform</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ระบบบริหารจัดการและจับคู่ซื้อขายไฟฟ้าอัจฉริยะ (Real-time P2P Trading)</p>", unsafe_allow_html=True)

# 3. ตั้งค่า Wheeling Charge (Sidebar)
st.sidebar.header("⚙️ การตั้งค่าราคาโครงข่าย")
t_fee = st.sidebar.slider("1. ค่าระบบส่ง (Transmission)", 0.1, 1.0, 0.28)
s_fee = st.sidebar.slider("2. ค่าความมั่นคง (Security)", 0.1, 1.0, 0.53)
p_fee = st.sidebar.slider("3. ค่าสนับสนุนนโยบาย (Policy)", 0.1, 1.0, 0.50)
total_wheeling = t_fee + s_fee + p_fee

st.sidebar.metric("รวม Wheeling Charge", f"{total_wheeling:.4f} ฿")
st.sidebar.divider()
st.sidebar.write("💡 *ปรับแถบเลื่อนเพื่อจำลองราคาที่เปลี่ยนไป*")

# 4. สร้างข้อมูลสถานี (30 แห่ง)
np.random.seed(42)
ids = [f"ST-{i+1:02d}" for i in range(30)]
types = np.random.choice(["Seller", "Buyer"], 30)
prices = np.random.uniform(2.5, 4.5, 30).round(2)
amounts = np.random.randint(50, 200, 30)

df = pd.DataFrame({"Station": ids, "Type": types, "Price (฿)": prices, "Energy (kWh)": amounts})

# 5. แสดงกราฟวิเคราะห์ราคา
st.write("### 📈 กราฟเปรียบเทียบราคาเสนอซื้อ-ขายแต่ละสถานี")
chart_df = df.pivot(index='Station', columns='Type', values='Price (฿)')
st.bar_chart(chart_df)

st.divider()

# 6. ส่วนการจับคู่ (Matching)
st.write("### 🤝 สรุปการจับคู่ซื้อขายที่คุ้มค่าที่สุด")
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
        "ค่าส่ง (Wheeling)": f"{total_wheeling:.2f} ฿",
        "ราคาที่ผู้ซื้อต้องจ่าย": f"{s['Price (฿)'] + total_wheeling:.2f} ฿",
        "สถานะ": "⚡ Connected"
    })

st.table(pd.DataFrame(match_list).head(8))

# 7. สรุปท้ายหน้า
st.info(f"ระบบกำลังจำลองการซื้อขายสำหรับ 30 สถานี | อัตราค่าธรรมเนียมปัจจุบัน: {total_wheeling:.4f} บาท/หน่วย")
