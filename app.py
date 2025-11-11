import streamlit as st

st.set_page_config(page_title="분자식 퀴즈", page_icon="🧪")
st.title("🧪 분자식 퀴즈 게임")
st.write("아래 분자식의 물질 이름을 맞혀보세요!")

# 🔹 문제 (분자식 : 정답)
quiz = {
    "H₂O": "물",
    "CO₂": "이산화탄소",
    "O₂": "산소",
    "NaCl": "염화나트륨",
    "CH₄": "메테인",
    "NH₃": "암모니아",
    "C₂H₅OH": "에탄올",
    "H₂SO₄": "황산",
    "CaCO₃": "탄산칼슘",
    "N₂": "질소"
}

score = 0

# 🔹 입력받기
for formula, answer in quiz.items():
    user_answer = st.text_input(f"{formula} 의 이름은?", key=formula)
    if user_answer:
        if user_answer.strip() == answer:
            st.success("✅ 정답!")
            score += 1
        else:
            st.error(f"❌ 오답! 정답은 {answer}")

st.markdown("---")
st.subheader(f"🎯 총 점수: {score} / {len(quiz)}")

if st.button("🔄 다시 시작"):
    st.experimental_rerun()
