import streamlit as st
import os
import datetime

st.set_page_config(page_title="照小合唱團 練習平台", layout="centered")

st.title("🎵 照小合唱團 練習平台")
st.write("請依下列步驟操作：輸入姓名 → 選擇音檔 → 上傳並等待評分結果")

# 1️⃣ 學生姓名輸入
student_name = st.text_input("請輸入你的姓名（真實姓名）：")

# 2️⃣ 音檔上傳
uploaded_file = st.file_uploader("請選擇要上傳的音檔（.mp3 或 .wav）", type=["mp3", "wav"])

# 3️⃣ 儲存與評分（簡易示範）
if uploaded_file and student_name:
    # 自動建立 student_results 資料夾
    os.makedirs("student_results", exist_ok=True)

    # 檔案命名
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{student_name}_{now}_{uploaded_file.name}"
    filepath = os.path.join("student_results", filename)

    # 儲存檔案
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ 上傳成功！檔案已儲存為：{filename}")

    # 模擬評分結果（實際版本會分析音準、節奏等）
    st.subheader("📊 評分結果（示意）")
    st.write(f"學生姓名：**{student_name}**")
    st.write("🎯 音準：87%")
    st.write("⏱️ 節奏：90%")
    st.write("🔊 音量：85%")

elif student_name and not uploaded_file:
    st.warning("請選擇一個音檔上傳")
fix: 移除 Flask 錯誤語法，改用 Streamlit 介面
