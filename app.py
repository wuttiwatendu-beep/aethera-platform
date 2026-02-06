import streamlit as st
import plotly.graph_objects as go

def show_energy_flow():
    st.markdown("### ⚡ Real-time Energy Flow (Zero Export Mode)")
    st.info("💡 ระบบใช้พลังงานแสงอาทิตย์เป็นหลัก หากไม่พอจะดึงไฟจากการไฟฟ้าอัตโนมัติ")

    # ตัวเลขจำลองที่สัมพันธ์กับ 2,854.56 kW ของคุณนุ
    solar_gen = 1850.0  # ผลิตได้ตอนนี้
    total_load = 2200.0 # ความต้องการใช้ไฟทั้งหมด
    pea_import = total_load - solar_gen # ส่วนต่างที่ดึงจากไฟหลวง
    p2p_transfer = 150.0 # มีการเทรดกันภายใน

    # สร้าง Sankey Diagram โทนสว่าง
    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 20, thickness = 30,
          label = ["☀️ Solar PV", "🔌 PEA Grid", "🏦 RMUTI Busbar", "🏫 Central Campus", "🚜 Nong Rawiang"],
          color = ["#FBC02D", "#E57373", "#90A4AE", "#0288D1", "#0288D1"]
        ),
        link = dict(
          source = [0, 1, 2, 2], # ต้นทาง
          target = [2, 2, 3, 4], # ปลายทาง
          value = [solar_gen, pea_import, 1400, 800], # ปริมาณ kW
          # สีเส้น: เหลือง (Solar), แดง (Grid)
          color = ["rgba(251, 192, 45, 0.4)", "rgba(229, 115, 115, 0.4)", 
                   "rgba(2, 136, 209, 0.2)", "rgba(2, 136, 209, 0.2)"]
      ))])

    fig.update_layout(
        title_text="RMUTI Energy Distribution (kW)",
        font_size=12,
        height=500,
        paper_bgcolor="white",
        plot_bgcolor="white"
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # แถบแสดงสถานะ
    c1, c2 = st.columns(2)
    with c1:
        st.success(f"✅ Solar Contribution: {(solar_gen/total_load)*100:.1f}%")
    with c2:
        st.warning(f"🔌 Grid Reliance: {(pea_import/total_load)*100:.1f}%")

# เรียกใช้ฟังก์ชันในหน้าเมนูที่เลือก
if page == "Smart Energy Flow":
    show_energy_flow()
