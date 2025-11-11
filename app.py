import streamlit as st
import time

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
    st.session_state.start_time = None  # 시작 시간
    st.session_state.current_input = ""  # 현재 입력값

def handle_submit():
    """엔터키로 입력 완료 시 실행"""
    ans = st.session_state.current_input.strip()

    # 첫 입력 시점에 시간 측정 시작
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()

    if ans == "":
        st.warning("⚠️ 답을 입력해주세요!")
        return

    st.session_state.answers.append(ans)
    st.session_state.current_input = ""

    if st.session_state.index + 1 < len(quiz):
        st.session_state.index += 1
    else:
        st.session_state.show_result = True

    st.rerun()

# 🔹 퀴즈 완료 후 결과 표시
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

    # 🔹 시간 계산
    if st.session_state.start_time:
        elapsed = time.time() - st.session_state.start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        st.markdown(f"⏱️ **총 소요 시간:** {minutes}분 {seconds}초")

    st.subheader(f"총 점수: {score} / {len(quiz)}")

    if st.button("🔁 다시 시작하기"):
        for key in ["index", "answers", "show_result", "start_time", "current_input"]:
            if key == "index":
                st.session_state[key] = 0
            elif key == "answers":
                st.session_state[key] = []
            elif key == "show_result":
                st.session_state[key] = False
            else:
                st.session_state[key] = None if key == "start_time" else ""
        st.rerun()

# 🔹 퀴즈 진행 중
else:
    i = st.session_state.index
    formula, correct = quiz[i]

    st.subheader(f"문제 {i+1} / {len(quiz)}")
    st.write(f"👉 **{formula}** 의 물질 이름은 무엇일까요?")

    # 🔹 엔터키로 제출 가능 (on_change 이벤트 사용)
    st.text_input(
        "정답 입력:",
        key="current_input",
        on_change=handle_submit
    )

    # 혹시 버튼으로도 제출하고 싶을 경우
    if st.button("다음 문제 ➡️"):
        handle_submit()
