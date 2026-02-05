import streamlit as st
import pandas as pd
import numpy as np

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Platform", layout="wide")

# 2. หัวข้อหลัก
st.title("💎 AETHERA Smart Energy Platform")
st.subheader("ระบบจำลองเครือข่ายซื้อขายไฟฟ้าอัตโนมัติ (Peer-to-Peer Grid)")

# 3. ส่วนการตั้งค่า Wheeling Charge (Sidebar)
st.sidebar.header("⚙️ ตั้งค่าค่าธรรมเนียม (Wheeling Charge)")
t_fee = st.sidebar.number_input("1. ค่าระบบส่ง (Transmission)", value=0.2800, format="%.4f")
s_fee = st.sidebar.number_input("2. ค่าความมั่นคง (Security)", value=0.5303, format="%.4f")
p_fee = st.sidebar.number_input("3. ค่าสนับสนุนนโยบาย (Policy)", value=0.5000, format="%.4f")

total_wheeling = t_fee + s_fee + p_fee
st.sidebar.markdown(f"### รวม: **{total_wheeling:.4f}** บาท/หน่วย")
st.sidebar.divider()
st.sidebar.info("คุณนุสามารถปรับตัวเลขข้างบนเพื่อดูผลกระทบต่อราคาซื้อขายได้ทันทีครับ")

# 4. สร้างข้อมูลจำลอง 30 สถานี
np.random.seed(42) # ล็อกค่าสุ่มให้เหมือนกันทุกครั้ง
data = {
    "ID": [f"ST-{i+1:02d}" for i in range(30)],
    "ประเภท": np.random.choice(["ผู้ขาย (Generator)", "ผู้ซื้อ (Consumer)"], 30),
    "กำลังผลิต/ความต้องการ (kWh)": np.random.uniform(10, 100, 30).round(2),
    "ราคาเสนอ (บาท)": np.random.uniform(2.5, 4.5, 30).round(2)
}
df = pd.DataFrame(data)

# 5. แสดงผล Dashboard
col1, col2, col3 = st.columns(3)
col1.metric("จำนวนสถานีทั้งหมด", "30 สถานี")
col2.metric("สถานะเครือข่าย", "Active", delta="Normal")
col3.metric("Wheeling Charge", f"{total_wheeling:.4f} ฿")

st.divider()

# 6. แสดงตารางข้อมูลสถานี
st.write("### 📊 ข้อมูลการใช้ไฟฟ้าและราคาเสนอของ 30 สถานี")
st.dataframe(df, use_container_width=True)

# 7. สรุปผลด้านล่าง
st.success(f"✅ ข้อมูลถูกอัปเดตเรียบร้อยแล้วครับคุณนุ ลองตรวจสอบสถานี ST-01 ถึง ST-30 ได้เลย!")
