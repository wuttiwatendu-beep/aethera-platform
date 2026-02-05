import streamlit as st
import pandas as pd
import numpy as np

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Business Management", layout="wide")

# 2. หัวข้อหลัก
st.markdown("<h1 style='text-align: center; color: #00A8E8;'>💎 AETHERA Operations & Billing</h1>", unsafe_allow_html=True)

# 3. ส่วนการจดทะเบียนสถานีใหม่ (Registration & Input)
with st.expander("➕ ลงทะเบียนสถานี/คู่สัญญาใหม่ (New Registration)"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st_id = st.text_input("รหัสสถานี (เช่น ST-31)")
        st_type = st.selectbox("ประเภท", ["Seller (ผู้ขาย)", "Buyer (ผู้ซื้อ)"])
    with col2:
        st_energy = st.number_input("ปริมาณไฟฟ้าต่อวัน (kWh)", min_value=0.0)
        st_price = st.number_input("ราคาเสนอ (฿/หน่วย)", min_value=0.0)
    with col3:
        st_lat = st.number_input("พิกัดละติจูด (Lat)", value=13.75)
        st_lon = st.number_input("พิกัดลองจิจูด (Lon)", value=100.50)
    
    if st.button("บันทึกข้อมูลสัญญา (Register Contract)"):
        st.success(f"จดทะเบียนสถานี {st_id} เข้าสู่เครือข่ายเรียบร้อยแล้ว!")

st.divider()

# 4. ข้อมูลจำลองสำหรับรอบบัญชีปัจจุบัน (Simulated Database)
np.random.seed(42)
ids = [f"ST-{i+1:02d}" for i in range(10)]
types = ["Seller", "Buyer", "Seller", "Buyer", "Seller", "Buyer", "Seller", "Buyer", "Seller", "Buyer"]
amounts = [150, 120, 200, 180, 90, 100, 300, 250, 110, 130]
prices = [3.5, 4.2, 3.2, 4.5, 3.8, 4.0, 3.1, 4.3, 3.4, 4.1]

db = pd.DataFrame({"Station": ids, "Type": types, "Energy_kWh": amounts, "Base_Price": prices})

# 5. Dashboard สรุปภาพรวม (เหมือน 5 หน้าที่เราทำมา)
st.write("### 📊 Dashboard สรุปผลการดำเนินงาน")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
total_trade = sum(amounts)
wheeling = 1.3103
kpi1.metric("ปริมาณการเทรดรวม", f"{total_trade} kWh")
kpi2.metric("สถานีที่ Active", "10 สถานี")
kpi3.metric("Wheeling Charge", f"{wheeling} ฿")
kpi4.metric("รายได้ค่าธรรมเนียมรวม", f"{(total_trade * wheeling):,.2.2f} ฿")

# 6. บิลค่าใช้จ่ายประจำรอบ (Billing & Settlement)
st.write("### 📑 สรุปบิลค่าใช้จ่ายรายคู่สัญญา")
match_data = []
# จำลองการจับคู่ 5 คู่สัญญารอบปัจจุบัน
for i in range(0, 10, 2):
    s_idx = i
    b_idx = i+1
    energy = min(db.iloc[s_idx]['Energy_kWh'], db.iloc[b_idx]['Energy_kWh'])
    cost_energy = energy * db.iloc[s_idx]['Base_Price']
    cost_wheeling = energy * wheeling
    total_bill = cost_energy + cost_wheeling
    
    match_data.append({
        "คู่สัญญา (S -> B)": f"{db.iloc[s_idx]['Station']} ➔ {db.iloc[b_idx]['Station']}",
        "พลังงานที่ซื้อขาย (kWh)": energy,
        "ค่าไฟต้นทาง (฿)": f"{cost_energy:,.2f}",
        "ค่า Wheeling (฿)": f"{cost_wheeling:,.2f}",
        "ยอดรวมบิลนี้ (฿)": f"{total_bill:,.2f}",
        "สถานะการชำระ": "รอดำเนินการ (Pending)"
    })

st.table(pd.DataFrame(match_data))

# 7. แผนที่และกราฟ (ย่อส่วนไว้ด้านล่าง)
c_left, c_right = st.columns([1, 1])
with c_left:
    st.write("📈 ราคาตลาด")
    st.line_chart(db.set_index('Station')['Base_Price'])
with c_right:
    st.write("📍 ตำแหน่งสถานีคู่สัญญา")
    # สุ่มพิกัดกรุงเทพฯ สำหรับแผนที่
    map_df = pd.DataFrame({
        'lat': np.random.uniform(13.7, 13.8, 10),
        'lon': np.random.uniform(100.5, 100.6, 10)
    })
    st.map(map_df)

st.info("AETHERA System: ระบบกำลังรันรอบบัญชีประจำวันที่ 05/02/2026")
