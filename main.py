import streamlit as st

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    html, body, [class*="css"] {
        font-family: 'Special Elite', cursive;
        background-color: #fdf6e3;
        color: #4b3b2f;
    }
    .title {
        text-align: center;
        font-size: 48px;
        margin-bottom: 20px;
        color: #6e4f3a;
    }
    .result {
        background-color: #fff8e6;
        border: 2px dashed #c2a270;
        border-radius: 10px;
        padding: 20px;
        margin-top: 30px;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💘 키 궁합 계산기</div>', unsafe_allow_html=True)
st.write("당신의 키를 입력하면, 당신에게 잘 어울리는 이상형의 키 범위를 알려드려요! 🥰")

gender = st.radio("당신의 성별은?", ["여자", "남자"])
height = st.number_input("당신의 키를 입력하세요 (cm)", min_value=100, max_value=250, step=1)

if st.button("🔍 이상형 키 알아보기"):
    if height:
        if gender == "여자":
            min_match = height + 10
            max_match = height + 15
            st.markdown(f"""
                <div class='result'>
                💃 당신의 키는 <b>{height}cm</b> 이군요!<br><br>
                🕺 당신과 잘 어울리는 이상형의 키는 <b>{min_match}cm ~ {max_match}cm</b> 입니다.<br><br>
                ✨ 키 차이가 자연스럽고 포근한 케미를 만들어줄 거예요 💖
                </div>
            """, unsafe_allow_html=True)
        else:
            min_match = height - 15
            max_match = height - 10
            st.markdown(f"""
                <div class='result'>
                🕺 당신의 키는 <b>{height}cm</b> 이군요!<br><br>
                💃 당신과 잘 어울리는 이상형의 키는 <b>{min_match}cm ~ {max_match}cm</b> 입니다.<br><br>
                ✨ 눈높이도 맞고, 사진 찍을 때도 예쁜 조합이에요 📸💕
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("키를 입력해 주세요!")

