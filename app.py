import streamlit as st
import random
import time

st.set_page_config(page_title="단답형 주기율표 퀴즈", page_icon="🧪")
st.title("🧪 단답형 주기율표 퀴즈 (20문제)")

# -------------------------------
# 🔹 원소 데이터 (20개)
elements = [
    {"name":"수소","symbol":"H","number":1,"period":1,"group":1,"type":"비금속"},
    {"name":"헬륨","symbol":"He","number":2,"period":1,"group":18,"type":"비활성기체"},
    {"name":"리튬","symbol":"Li","number":3,"period":2,"group":1,"type":"금속"},
    {"name":"베릴륨","symbol":"Be","number":4,"period":2,"group":2,"type":"금속"},
    {"name":"붕소","symbol":"B","number":5,"period":2,"group":13,"type":"준금속"},
    {"name":"탄소","symbol":"C","number":6,"period":2,"group":14,"type":"비금속"},
    {"name":"질소","symbol":"N","number":7,"period":2,"group":15,"type":"비금속"},
    {"name":"산소","symbol":"O","number":8,"period":2,"group":16,"type":"비금속"},
    {"name":"플루오린","symbol":"F","number":9,"period":2,"group":17,"type":"비금속"},
    {"name":"네온","symbol":"Ne","number":10,"period":2,"group":18,"type":"비활성기체"},
    {"name":"나트륨","symbol":"Na","number":11,"period":3,"group":1,"type":"금속"},
    {"name":"마그네슘","symbol":"Mg","number":12,"period":3,"group":2,"type":"금속"},
    {"name":"알루미늄","symbol":"Al","number":13,"period":3,"group":13,"type":"금속"},
    {"name":"규소","symbol":"Si","number":14,"period":3,"group":14,"type":"준금속"},
    {"name":"인","symbol":"P","number":15,"period":3,"group":15,"type":"비금속"},
    {"name":"황","symbol":"S","number":16,"period":3,"group":16,"type":"비금속"},
    {"name":"염소","symbol":"Cl","number":17,"period":3,"group":17,"type":"비금속"},
    {"name":"아르곤","symbol":"Ar","number":18,"period":3,"group":18,"type":"비활성기체"},
    {"name":"칼륨","symbol":"K","number":19,"period":4,"group":1,"type":"금속"},
    {"name":"칼슘","symbol":"Ca","number":20,"period":4,"group":2,"type":"금속"},
]

# -------------------------------
# 🔹 새 퀴즈 생성 함수
def create_quiz():
    quiz = []
    for elem in elements:
        info_types = ["symbol","number","period","group","type"]
        chosen_info = random.choice(info_types)
        quiz.append({"elem": elem, "info": chosen_info})
    random.shuffle(quiz)
    return quiz

# -------------------------------
# 🔹 세션 상태 초기화 및 새 퀴즈 생성
if "quiz" not in st.session_state:
    st.session_state.quiz = create_quiz()
    st.session_state.index = 0
    st.session_state.answers = []
    st.session_state.show_result = False
    st.session_state.start_time = None
    st.session_state.current_input = ""

# -------------------------------
# 🔹 제출 처리 함수
def handle_submit():
    ans = st.session_state.current_input.strip()
    if ans == "":
        st.warning("⚠️ 답을 입력해주세요!")
        return

    # 첫 문제 입력 시 시간 측정 시작
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()

    st.session_state.answers.append(ans)
    st.session_state.current_input = ""

    if st.session_state.index + 1 < len(st.session_state.quiz):
        st.session_state.index += 1
    else:
        st.session_state.show_result = True
    st.rerun()

# -------------------------------
# 🔹 결과 화면
if st.session_state.show_result:
    st.success("🎉 퀴즈 완료!")
    score = 0
    for i, item in enumerate(st.session_state.quiz):
        elem = item["elem"]
        info = item["info"]
        user = st.session_state.answers[i]

        if info == "symbol":
            question_text = f"{elem['name']}의 원소 기호는?"
            correct = elem["symbol"]
        elif info == "number":
            question_text = f"{elem['name']}의 원자번호는?"
            correct = str(elem["number"])
        elif info == "period":
            question_text = f"{elem['name']}는 몇 주기인가요?"
            correct = str(elem["period"])
        elif info == "group":
            question_text = f"{elem['name']}는 몇 족인가요?"
            correct = str(elem["group"])
        elif info == "type":
            question_text = f"{elem['name']}의 원소 종류는?"
            correct = elem["type"]

        if user.strip().lower() == correct.lower():
            st.write(f"✅ {i+1}. {question_text} → {user} (정답!)")
            score += 1
        else:
            st.write(f"❌ {i+1}. {question_text} → {user} (정답: {correct})")

    # 소요 시간 표시
    if st.session_state.start_time:
        elapsed = time.time() - st.session_state.start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        st.markdown(f"⏱️ **총 소요 시간:** {minutes}분 {seconds}초")
    
    st.subheader(f"총 점수: {score} / {len(st.session_state.quiz)}")

    # 새 퀴즈 생성 버튼
    if st.button("🔁 다시 시작하기"):
        st.session_state.quiz = create_quiz()
        st.session_state.index = 0
        st.session_state.answers = []
        st.session_state.show_result = False
        st.session_state.start_time = None
        st.session_state.current_input = ""
        st.rerun()

# -------------------------------
# 🔹 퀴즈 진행 중
else:
    i = st.session_state.index
    item = st.session_state.quiz[i]
    elem = item["elem"]
    info = item["info"]

    if info == "symbol":
        question_text = f"{elem['name']}의 원소 기호는?"
    elif info == "number":
        question_text = f"{elem['name']}의 원자번호는?"
    elif info == "period":
        question_text = f"{elem['name']}는 몇 주기인가요?"
    elif info == "group":
        question_text = f"{elem['name']}는 몇 족인가요?"
    elif info == "type":
        question_text = f"{elem['name']}의 원소 종류는?"

    st.subheader(f"문제 {i+1} / 20")
    st.write(f"👉 {question_text}")
    st.text_input("정답 입력:", key="current_input", on_change=handle_submit)
    if st.button("다음 문제 ➡️"):
        handle_submit()
