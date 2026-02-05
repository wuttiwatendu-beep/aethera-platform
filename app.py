import streamlit as st
import pandas as pd
import numpy as np

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Platform", layout="wide")

# 2. หัวข้อหลัก
st.title("💎 AETHERA Smart Energy Platform")
st.subheader("ระบบจับคู่ซื้อขายไฟฟ้าอัตโนมัติ (Peer-to-Peer Matching)")

# 3. ตั้งค่า Wheeling Charge (Sidebar)
st.sidebar.header("⚙️ ตั้งค่า Wheeling Charge")
t_fee = st.sidebar.number_input("1. ค่าระบบส่ง", value=0.2800, format="%.4f")
s_fee = st.sidebar.number_input("2. ค่าความมั่นคง", value=0.5303, format="%.4f")
p_fee = st.sidebar.number_input("3. ค่าสนับสนุนนโยบาย", value=0.5000, format="%.4f")
total_wheeling = t_fee + s_fee + p_fee

# 4. สร้างข้อมูลสถานี (จำลอง 30 แห่ง)
np.random.seed(42)
ids = [f"ST-{i+1:02d}" for i in range(30)]
types = np.random.choice(["ผู้ขาย (Seller)", "ผู้ซื้อ (Buyer)"], 30)
amounts = np.random.uniform(20, 80, 30).round(2)
prices = np.random.uniform(2.5, 4.0, 30).round(2)

df = pd.DataFrame({"ID": ids, "ประเภท": types, "ปริมาณ (kWh)": amounts, "ราคาเสนอ (฿)": prices})

# 5. ระบบ Matching เบื้องต้น
sellers = df[df['ประเภท'] == "ผู้ขาย (Seller)"].sort_values("ราคาเสนอ (฿)")
buyers = df[df['ประเภท'] == "ผู้ซื้อ (Buyer)"].sort_values("ราคาเสนอ (฿)", ascending=False)

# แสดงผล Dashboard
st.write("### 📊 สรุปภาพรวมเครือข่าย")
c1, c2, c3 = st.columns(3)
c1.metric("ผู้ขายในระบบ", f"{len(sellers)} ราย")
c2.metric("ผู้ซื้อในระบบ", f"{len(buyers)} ราย")
c3.metric("ค่าธรรมเนียมรวม", f"{total_wheeling:.4f} ฿")

st.divider()

# 6. แสดงผลการจับคู่
st.write("### 🤝 ผลการจับคู่ซื้อขายที่คุ้มที่สุด (Top Matches)")
match_data = []
for i in range(min(len(sellers), len(buyers))):
    s = sellers.iloc[i]
    b = buyers.iloc[i]
    final_price = s['ราคาเสนอ (฿)'] + total_wheeling
    match_data.append({
        "ผู้ขาย": s['ID'],
        "ผู้ซื้อ": b['ID'],
        "ราคาต้นทาง (฿)": s['ราคาเสนอ (฿)'],
        "ค่าส่ง (Wheeling)": f"{total_wheeling:.4f}",
        "ราคาจ่ายจริง (฿)": round(final_price, 4),
        "สถานะ": "✅ Matching Success"
    })

st.table(pd.DataFrame(match_data).head(10)) # โชว์ 10 คู่แรก

st.divider()
st.write("### 📋 บัญชีรายชื่อสถานีทั้งหมด")
st.dataframe(df, use_container_width=True)
