import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AETHERA Enterprise", layout="wide")

# 2. หัวข้อหลัก
st.markdown("<h1 style='text-align: center; color: #00A8E8;'>💎 AETHERA Enterprise System</h1>", unsafe_allow_html=True)

# 3. เมนูหลัก (Tabs) - เพิ่มแท็บ "สรุปรายเดือน"
tab1, tab2, tab3, tab4 = st.tabs(["📝 ลงทะเบียน", "📈 ตลาดวันนี้", "📑 สรุปบิล", "📊 แนวโน้มรายได้"])

# --- ข้อมูลพื้นฐาน ---
wheeling = 1.3103
np.random.seed(42)
ids = [f"ST-{i+1:02d}" for i in range(10)]
types = ["Seller", "Buyer"] * 5
amounts = [150, 120, 200, 180, 90, 100, 300, 250, 110, 130]
prices = [3.5, 4.2, 3.2, 4.5, 3.8, 4.0, 3.1, 4.3, 3.4, 4.1]
db = pd.DataFrame({"Station": ids, "Type": types, "Energy_kWh": amounts, "Base_Price": prices})

# --- หน้าที่ 1: ลงทะเบียน ---
with tab1:
    st.subheader("➕ ลงทะเบียนคู่สัญญาใหม่")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        c1.text_input("รหัสสถานี")
        c1.selectbox("ประเภท", ["ผู้ซื้อ", "ผู้ขาย"])
        c2.number_input("ปริมาณ (kWh)", value=100.0)
        c2.number_input("ราคา (฿)", value=3.5)
        if st.form_submit_button("บันทึก"):
            st.success("บันทึกสำเร็จ!")

# --- หน้าที่ 2: ตลาดวันนี้ ---
with tab2:
    total_trade = sum(amounts)
    platform_income = total_trade * wheeling
    k1, k2, k3 = st.columns(3)
    k1.metric("พลังงานรวมวันนี้", f"{total_trade} kWh")
    k2.metric("รายได้แพลตฟอร์ม", f"{platform_income:,.2f} ฿")
    k3.metric("อัตรา Wheeling", f"{wheeling} ฿")
    st.bar_chart(db.set_index('Station')['Base_Price'])

# --- หน้าที่ 3: สรุปบิล & ปุ่มดาวน์โหลด ---
with tab3:
    st.subheader("📑 สรุปบิลประจำรอบ")
    bill_list = []
    for i in range(0, 10, 2):
        s, b = db.iloc[i], db.iloc[i+1]
        energy = min(s['Energy_kWh'], b['Energy_kWh'])
        bill_list.append({
            "คู่สัญญา": f"{s['Station']} ➔ {b['Station']}",
            "พลังงาน (kWh)": energy,
            "ยอดสุทธิ (฿)": round(energy * (s['Base_Price'] + wheeling), 2),
            "วันที่": datetime.now().strftime("%Y-%m-%d")
        })
    bill_df = pd.DataFrame(bill_list)
    st.dataframe(bill_df, use_container_width=True)
    
    # --- ปุ่ม Export ข้อมูล (ส่วนที่เพิ่ม) ---
    csv = bill_df.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 ดาวน์โหลดบิลวันนี้ (CSV)",
        data=csv,
        file_name=f'AETHERA_Bills_{datetime.now().strftime("%Y%m%d")}.csv',
        mime='text/csv',
    )

# --- หน้าที่ 4: แนวโน้มรายได้ (ส่วนที่เพิ่ม) ---
with tab4:
    st.subheader("📊 รายงานสรุปย้อนหลัง 7 วัน")
    # จำลองข้อมูลย้อนหลัง
    dates = [(datetime.now() - timedelta(days=i)).strftime("%d %b") for i in range(7)][::-1]
    revenue_trend = [platform_income * np.random.uniform(0.8, 1.2) for _ in range(7)]
    energy_trend = [total_trade * np.random.uniform(0.9, 1.1) for _ in range(7)]
    
    trend_df = pd.DataFrame({"วันที่": dates, "รายได้แพลตฟอร์ม (฿)": revenue_trend, "พลังงานรวม (kWh)": energy_trend})
    
    c_left, c_right = st.columns(2)
    with c_left:
        st.write("💰 **แนวโน้มรายได้ค่าธรรมเนียม**")
        st.line_chart(trend_df.set_index("วันที่")["รายได้แพลตฟอร์ม (฿)"])
    with c_right:
        st.write("⚡ **แนวโน้มปริมาณการใช้พลังงาน**")
        st.area_chart(trend_df.set_index("วันที่")["พลังงานรวม (kWh)"])

st.divider()
st.caption(f"AETHERA System Update: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
