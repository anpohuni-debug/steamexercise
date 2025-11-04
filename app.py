import streamlit as st

# 제목
st.title("간단한 Streamlit 예제")

# 텍스트 입력 받기
name = st.text_input("이름을 입력하세요:")

# 버튼
if st.button("인사하기"):
    st.write(f"안녕하세요, {name}님! 👋")

# 슬라이더
age = st.slider("나이를 선택하세요:", 0, 100, 20)
st.write(f"당신의 나이는 {age}살입니다.")
