import streamlit as st

# ตั้งค่าหน้าเว็บ AETHERA
st.set_page_config(page_title="AETHERA Platform", layout="wide")

st.title("💎 AETHERA Smart Energy Platform")
st.subheader("ระบบจำลองเครือข่ายซื้อขายไฟฟ้าอัตโนมัติ")

# แถบด้านข้างสำหรับตั้งค่า Wheeling Charge
st.sidebar.header("⚙️ ตั้งค่า Wheeling Charge")
t_fee = st.sidebar.number_input("1. ค่าระบบส่ง (Transmission)", value=0.2800, format="%.4f")
s_fee = st.sidebar.number_input("2. ค่าความมั่นคง (Security)", value=0.5303, format="%.4f")
p_fee = st.sidebar.number_input("3. ค่าสนับสนุนนโยบาย (Policy)", value=0.5000, format="%.4f")

total = t_fee + s_fee + p_fee
st.sidebar.info(f"ยอดรวม Wheeling Charge: {total:.4f} บาท/หน่วย")

# ส่วนแสดงผลหลัก
st.success(f"สวัสดีครับคุณนุ! เว็บออนไลน์เรียบร้อยแล้ว ค่าธรรมเนียมรวมคือ {total:.4f} บาท")
st.metric("สถานะระบบ", "Online", delta="Ready")

