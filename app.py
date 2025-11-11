import streamlit as st

st.set_page_config(page_title="분자식 퀴즈", page_icon="🧪")
st.title("🧪 분자식 퀴즈 게임")

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

# 🔹 세션 상태 초기화
if "current" not in st.session_state:
    st.session_state.current = 0
    st.session_state.answers = []
    st.session_state.finished = False
    st.session_state.temp_answer = ""  # 입력값 임시 저장용

formulas = list(quiz.keys())

# 🔹 퀴즈 진행 중
if not st.session_state.finished:
    idx = st.session_state.current
    formula = formulas[idx]

    st.subheader(f"문제 {idx + 1} / {len(formulas)}")
    st.write(f"👉 **{formula}** 의 물질 이름은 무엇일까요?")

    # 🔹 입력받기 (폼 제거 — 대신 일반 입력 + 버튼)
    st.session_state.temp_answer = st.text_input(
        "정답 입력:",
        value=st.session_state.temp_answer,
        key=f"answer_{idx}"
    )

    if st.button("다음 문제 ➡️"):
        answer = st.session_state.temp_answer.strip()
        st.session_state.answers.append(answer)
        st.session_state.temp_answer = ""

        st.session_state.current += 1
        if st.session_state.current >= len(formulas):
            st.session_state.finished = True
        st.experimental_rerun()

# 🔹 결과 출력
else:
    st.success("🎉 퀴즈 완료!")
    score = 0
    st.subheader("결과 요약")

    for i, formula in enumerate(formulas):
        user_ans = st.session_state.answers[i]
        correct_ans = quiz[formula]
        if user_ans == correct_ans:
            st.write(f"✅ {formula} → **{user_ans}** (정답!)")
            score += 1
        else:
            st.write(f"❌ {formula} → **{user_ans}** (정답: {correct_ans})")

    st.markdown("---")
    st.subheader(f"총 점수: {score} / {len(formulas)}")

    if st.button("🔁 다시 시작하기"):
        for key in ["current", "answers", "finished", "temp_answer"]:
            st.session_state[key] = 0 if key == "current" else [] if key == "answers" else False if key == "finished" else ""
        st.experimental_rerun()
