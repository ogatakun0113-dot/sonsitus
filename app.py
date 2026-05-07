import streamlit as st
import math

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

# データ定義
cable_ref = {
    "5D-2V": {"freq": 400.0, "loss_10m": 1.7},
    "5D-FB": {"freq": 400.0, "loss_10m": 1.1},
    "8D-FB": {"freq": 400.0, "loss_10m": 0.8},
    "10D-FB": {"freq": 400.0, "loss_10m": 0.65},
    "RG-58A/U": {"freq": 400.0, "loss_10m": 3.8}
}

preset_freqs = {
    "70MHz帯": 70.0,
    "150MHz帯": 150.0,
    "400MHz帯": 400.0,
    "900MHz帯": 900.0,
    "1200MHz帯": 1200.0,
    "自由入力": 0.0
}

col1, col2 = st.columns(2)
with col1:
    cable_type = st.selectbox("同軸ケーブル型番", list(cable_ref.keys()))
with col2:
    freq_mode = st.selectbox("周波数区分", list(preset_freqs.keys()), index=0)

if freq_mode == "自由入力":
    target_freq = st.number_input("周波数 (MHz)", value=70.000, format="%.3f")
else:
    target_freq = preset_freqs[freq_mode]
    st.info(f"設定: {target_freq} MHz")

length = st.number_input("長さ (m)", value=10.0, step=1.0, format="%.1f")

# 計算ロジック
ref_freq = cable_ref[cable_type]["freq"]
ref_loss = cable_ref[cable_type]["loss_10m"] / 10.0

if target_freq > 0:
    calc_loss_per_m = ref_loss * math.sqrt(target_freq / ref_freq)
    total_loss = calc_loss_per_m * length
else:
    total_loss = 0.0

st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.subheader("📊 計算結果")
st.metric("合計損失 (推定値)", f"-{total_loss:.2f} dB")
st.write(f"条件: {cable_type} / {target_freq} MHz / {length} m")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("※標準特性に基づく近似値です。接栓損失は別途加算してください。")
