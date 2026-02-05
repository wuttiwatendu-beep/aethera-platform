import streamlit as st
import pandas as pd
import numpy as np

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Platform", layout="wide")

# 2. หัวข้อหลัก
st.markdown("<h1 style='text-align: center; color: #00A8E8;'>💎 AETHERA Smart Energy Platform</h1>", unsafe_allow_html=True)

# 3. Sidebar ตั้งค่า
st.sidebar.header("⚙️ การตั้งค่าราคา")
t_fee = st.sidebar.slider("1. ค่าระบบส่ง", 0.1, 1.0, 0.28)
s_fee = st.sidebar.slider("2. ค่าความมั่นคง", 0.1, 1.0, 0.53)
p_fee = st.sidebar.slider("3. ค่าสนับสนุนนโยบาย", 0.1, 1.0, 0.50)
total_wheeling = t_fee + s_fee + p_fee
st.sidebar.metric("รวม Wheeling Charge", f"{total_wheeling:.4f} ฿")

# 4. ข้อมูลสถานี (ใช้พิกัดที่แน่นอนเพื่อให้แผนที่โหลดง่ายขึ้น)
@st.cache_data
def get_data():
    np.random.seed(42)
    ids = [f"ST-{i+1:02d}" for i in range(30)]
    types = np.random.choice(["Seller", "Buyer"], 30)
    prices = np.random.uniform(2.5, 4.5, 30).round(2)
    # กำหนดพิกัดกรุงเทพฯ แบบเจาะจงจุดกึ่งกลาง
    lat = np.random.uniform(13.73, 13.75, 30)
    lon = np.random.uniform(100.52, 100.54, 30)
    return pd.DataFrame({"Station": ids, "Type": types, "Price (฿)": prices, "lat": lat, "lon": lon})

df = get_data()

# 5. กราฟราคา
st.write("### 📈 กราฟเปรียบเทียบราคาเสนอซื้อ-ขาย")
chart_df = df.pivot(index='Station', columns='Type', values='Price (฿)')
st.bar_chart(chart_df)

st.divider()

# 6. แผนที่ (ปรับคำสั่งใหม่ให้ Compatible กับคอมพิวเตอร์มากขึ้น)
st.write("### 📍 แผนที่พิกัดสถานีในเครือข่าย AETHERA")
# เพิ่มพารามิเตอร์ center เพื่อให้แผนที่รู้ว่าต้องเปิดไปที่ไหนทันที
st.map(df, latitude='lat', longitude='lon', zoom=13, use_container_width=True)

st.divider()

# 7. ตารางจับคู่
st.write("### 🤝 สรุปการจับคู่ซื้อขายที่คุ้มค่าที่สุด")
sellers = df[df['Type'] == "Seller"].sort_values("Price (฿)")
buyers = df[df['Type'] == "Buyer"].sort_values("Price (฿)", ascending=False)
match_list = []
for i in range(min(len(sellers), len(buyers))):
    s = sellers.iloc[i]
    b = buyers.iloc[i]
    match_list.append({
        "จากผู้ขาย": s['Station'], "ไปที่ผู้ซื้อ": b['Station'], 
        "ราคาต้นทาง": s['Price (฿)'], "ราคารวมส่ง": round(s['Price (฿)']+total_wheeling, 2)
    })
st.table(pd.DataFrame(match_list).head(10))
