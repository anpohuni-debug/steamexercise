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

formulas = list(quiz.keys())

# 🔹 퀴즈 진행 중
if not st.session_state.finished:
    current_index = st.session_state.current
    formula = formulas[current_index]

    st.subheader(f"문제 {current_index + 1} / {len(formulas)}")
    st.write(f"👉 **{formula}** 의 물질 이름은 무엇일까요?")

    with st.form(key=f"form_{current_index}"):
        answer = st.text_input("정답 입력:")
        submitted = st.form_submit_button("다음 문제 ➡️")

        if submitted:
            st.session_state.answers.append(answer.strip())
            st.session_state.current += 1
            if st.session_state.current >= len(formulas):
                st.session_state.finished = True
            st.experimental_rerun()

# 🔹 모든 문제를 푼 뒤 결과 출력
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
        st.session_state.current = 0
        st.session_state.answers = []
        st.session_state.finished = False
        st.experimental_rerun()
