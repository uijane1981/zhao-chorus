import streamlit as st
import os
import datetime

st.set_page_config(page_title="照小合唱團 練習平台", layout="centered")

st.title("🎵 照小合唱團 練習平台")
st.write("請依下列步驟操作：輸入姓名 → 播放伴奏 → 上傳音檔")

# 顯示伴奏播放器
st.audio("堅持的路.mp3", format="audio/mp3")
st.markdown("**請先聽伴奏再開始錄音唷！**")

# 學生姓名輸入
student_name = st.text_input("請輸入你的姓名（真實姓名）：")

# 音檔上傳
uploaded_file = st.file_uploader("請選擇要上傳的音檔（.mp3 或 .wav）", type=["mp3", "wav"])

# 處理上傳
if uploaded_file and student_name:
    os.makedirs("student_results", exist_ok=True)
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{student_name}_{now}_{uploaded_file.name}"
    filepath = os.path.join("student_results", filename)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ 上傳成功！檔案已儲存為：{filename}")

    st.subheader("📊 評分結果（模擬示意）")
    st.write(f"學生姓名：**{student_name}**")
    st.write("🎯 音準：88%")
    st.write("⏱️ 節奏：92%")
    st.write("🔊 音量：86%")

elif student_name and not uploaded_file:
    st.warning("請選擇一個音檔上傳")

