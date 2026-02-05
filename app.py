import streamlit as st
import pandas as pd
import numpy as np

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Business Management", layout="wide")

# 2. หัวข้อหลัก
st.markdown("<h1 style='text-align: center; color: #00A8E8;'>💎 AETHERA Smart Operations</h1>", unsafe_allow_html=True)

# 3. เมนูหลัก (Tabs) แบ่งเป็น 3 ส่วนเพื่อให้ดูง่ายในมือถือ
tab1, tab2, tab3 = st.tabs(["📝 ลงทะเบียน & สัญญา", "📈 ตลาดซื้อขาย", "📑 บิลค่าใช้จ่าย"])

# --- จำลองข้อมูลพื้นฐาน ---
wheeling = 1.3103
np.random.seed(42)
ids = [f"ST-{i+1:02d}" for i in range(10)]
types = ["Seller", "Buyer"] * 5
amounts = [150, 120, 200, 180, 90, 100, 300, 250, 110, 130]
prices = [3.5, 4.2, 3.2, 4.5, 3.8, 4.0, 3.1, 4.3, 3.4, 4.1]
db = pd.DataFrame({"Station": ids, "Type": types, "Energy_kWh": amounts, "Base_Price": prices})

# --- หน้าที่ 1: ลงทะเบียน & สัญญา ---
with tab1:
    st.subheader("➕ ระบบจดทะเบียนคู่สัญญาใหม่")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        new_id = c1.text_input("รหัสสถานี (เช่น ST-11)")
        new_type = c1.selectbox("ประเภทสัญญา", ["ผู้ซื้อ (Consumer)", "ผู้ขาย (Generator)"])
        new_energy = c2.number_input("ปริมาณซื้อขายที่คาดการณ์ (kWh)", value=100.0)
        new_price = c2.number_input("ราคาเสนอขาย (฿/หน่วย)", value=3.5)
        submitted = st.form_submit_button("บันทึกสัญญา (Register Contract)")
        if submitted:
            st.success(f"✅ บันทึกสัญญาสำหรับ {new_id} เรียบร้อยแล้ว!")

# --- หน้าที่ 2: ตลาดซื้อขาย (Dashboard) ---
with tab2:
    st.write("### 📊 ภาพรวมตลาดประจำรอบ")
    k1, k2, k3 = st.columns(3)
    total_trade = sum(amounts)
    platform_income = total_trade * wheeling
    k1.metric("พลังงานหมุนเวียนรวม", f"{total_trade} kWh")
    k2.metric("ค่าธรรมเนียมรวม", f"{wheeling} ฿")
    k3.metric("รายได้แพลตฟอร์ม", f"{platform_income:,.2f} ฿") # แก้ Error ตรงนี้ครับ
    
    st.write("📈 **กราฟเปรียบเทียบราคาเสนอซื้อ-ขาย**")
    st.bar_chart(db.set_index('Station')['Base_Price'])

# --- หน้าที่ 3: สรุปบิลค่าใช้จ่าย (Billing) ---
with tab3:
    st.write("### 📑 สรุปบิลรายคู่สัญญา (Bill Summary)")
    bill_data = []
    for i in range(0, 10, 2):
        s = db.iloc[i]
        b = db.iloc[i+1]
        energy = min(s['Energy_kWh'], b['Energy_kWh'])
        energy_cost = energy * s['Base_Price']
        wheeling_cost = energy * wheeling
        total = energy_cost + wheeling_cost
        
        bill_data.append({
            "คู่สัญญา (S➔B)": f"{s['Station']} ➔ {b['Station']}",
            "พลังงาน (kWh)": energy,
            "ค่าไฟ (฿)": round(energy_cost, 2),
            "ค่าส่ง (฿)": round(wheeling_cost, 2),
            "ยอดสุทธิ (฿)": round(total, 2),
            "สถานะ": "Pending ⏳"
        })
    st.dataframe(pd.DataFrame(bill_data), use_container_width=True)
    st.info("💡 บิลนี้คำนวณจาก: (ราคาเสนอขาย + Wheeling Charge) x ปริมาณการใช้จริง")

st.divider()
st.caption("AETHERA Platform | Powered by Gemini & Streamlit")
