import streamlit as st

st.set_page_config(page_title="同軸ケーブル損失計算", layout="centered")

st.markdown("""
<style>
.stNumberInput label { font-size: 18px !important; font-weight: 800 !important; color: #4682B4 !important; }
.result-box { background-color: #f0f8ff; padding: 20px; border-radius: 10px; border-left: 5px solid #4682B4; margin-top: 20px; }
.credit { text-align: right; font-size: 14px; color: #666; margin-bottom: -20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title('📡 同軸ケーブル損失計算')

cable_data = {
    "5D-2V (144MHz)": 0.094,
    "5D-2V (430MHz)": 0.170,
    "5D-FB (144MHz)": 0.063,
    "5D-FB (430MHz)": 0.110,
    "10D-FB (430MHz)": 0.055,
    "RG-58A/U (430MHz)": 0.380
}

cable_type = st.selectbox("ケーブル型番と周波数を選択", list(cable_data.keys()))
length = st.number_input("ケーブル長 (m)", value=10.0, step=1.0)

loss_per_m = cable_data[cable_type]
total_loss = loss_per_m * length

st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.subheader("📊 計算結果")
st.metric("合計損失", f"-{total_loss:.2f} dB")
st.write(f"1mあたりの損失: {loss_per_m} dB")
st.markdown('</div>', unsafe_allow_html=True)
st.caption("※コネクタ接栓の損失（1箇所あたり約0.5dB）は別途加算してください。")
