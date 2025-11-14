import streamlit as st

col1, col2 = st.columns(2) # 두 개의 컬럼 생성. 표현하고 싶은 내용을 열 데이터로 나눠 보여주고 싶을 떄 사용합니다.

# col1이라는 열(column) 안에 배치되는 요소들
with col1: # form을 사용하지 않고 입력 필드를 만들고 입력 값을 받음
    text1 = st.text_input("form을 이용하지 않는 경우")  # 한 줄 입력 필드
    text2 = st.text_area("form을 이용하지 않는 경우")   # 여러 줄 입력 필드

    # 입력된 값을 화면에 출력함
    st.write("1번 입력값: " + text1)  # 첫 번째 입력 필드의 값을 출력
    st.write("2번 입력값: " + text2)  # 두 번째 입력 필드의 값을 출력!!

# col2라는 열(column) 안에 배치되는 요소들
with col2:# "form을 사용합니다"라는 이름의 form을 만듦
    with st.form("form을 사용합니다"): # form 내부에 입력 필드를 생성하고 입력 값을 받음
        text3 = st.text_input("form을 이용하는 경우")  # 한 줄 입력 필드
        text4 = st.text_area("form을 이용하는 경우")   # 여러 줄 입력 필드

        # 제출 버튼을 만들어서 사용자가 버튼을 눌렀는지 여부를 확인
        submitted = st.form_submit_button("제출")  # 제출 버튼 생성

        if submitted:# 사용자가 제출 버튼을 눌렀을 경우 입력된 값을 화면에 출력
            st.write("1번 입력값: " + text3)  # 첫 번째 입력 필드의 값을 출력
            st.write("2번 입력값: " + text4)  # 두 번째 입력 필드의 값을 출력
        else:# 사용자가 제출 버튼을 누르지 않았을 경우 빈 값으로 출력 (초기 상태)
            st.write("1번 입력값: ")  # 첫 번째 입력 필드가 비어있음
            st.write("2번 입력값: ")  # 두 번째 입력 필드가 비어있음

