import streamlit as st

st.set_page_config(page_title="분자식 퀴즈", page_icon="🧪")
st.title("🧪 분자식 퀴즈 게임")

# 🔹 문제 목록
quiz = [
    ("H₂O", "물"),
    ("CO₂", "이산화탄소"),
    ("O₂", "산소"),
    ("NaCl", "염화나트륨"),
    ("CH₄", "메테인"),
    ("NH₃", "암모니아"),
    ("C₂H₅OH", "에탄올"),
    ("H₂SO₄", "황산"),
    ("CaCO₃", "탄산칼슘"),
    ("N₂", "질소")
]

# 🔹 세션 상태 초기화
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.answers = []
    st.session_state.show_result = False

# 🔹 퀴즈 완료 시 결과 보여주기
if st.session_state.show_result:
    st.success("🎉 퀴즈 완료!")
    score = 0
    for i, (formula, correct) in enumerate(quiz):
        user = st.session_state.answers[i]
        if user == correct:
            st.write(f"✅ {i+1}. {formula} → {user} (정답!)")
            score += 1
        else:
            st.write(f"❌ {i+1}. {formula} → {user} (정답: {correct})")
    st.subheader(f"총 점수: {score} / {len(quiz)}")

    if st.button("🔁 다시 시작하기"):
        st.session_state.index = 0
        st.session_state.answers = []
        st.session_state.show_result = False
        st.rerun()

# 🔹 퀴즈 진행 중
else:
    i = st.session_state.index
    formula, correct = quiz[i]

    st.subheader(f"문제 {i+1} / {len(quiz)}")
    st.write(f"👉 **{formula}** 의 물질 이름은 무엇일까요?")

    answer = st.text_input("정답 입력:", key=f"q_{i}")

    # "다음 문제" 버튼
    if st.button("다음 문제 ➡️"):
        if answer.strip() == "":
            st.warning("⚠️ 답을 입력해주세요!")
        else:
            st.session_state.answers.append(answer.strip())

            # 다음 문제로 이동 or 결과 표시
            if i + 1 < len(quiz):
                st.session_state.index += 1
                st.rerun()
            else:
                st.session_state.show_result = True
                st.rerun()
