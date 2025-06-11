import streamlit as st

# 한글 초성/중성/종성 획수 사전
CHO_STROKES = [2, 4, 2, 3, 6, 5, 4, 4, 8, 2, 4, 1, 3, 6, 4, 3, 4, 4, 3]
JUNG_STROKES = [2, 3, 2, 3, 2, 3, 2, 3, 1, 1, 3, 3, 4, 4, 3, 3, 4, 4, 2, 2, 4]
JONG_STROKES = [0,2,4,2,3,6,5,4,4,8,2,4,1,3,6,4,3,4,4,3,2,4,2,3,3,1,2,4]

def get_stroke_count(hangul):
    total = 0
    for char in hangul:
        if ord('가') <= ord(char) <= ord('힣'):
            base = ord(char) - 0xAC00
            cho = base // 588
            jung = (base % 588) // 28
            jong = base % 28
            total += CHO_STROKES[cho] + JUNG_STROKES[jung] + JONG_STROKES[jong]
    return total

def calculate_compatibility(name1, name2):
    total1 = get_stroke_count(name1)
    total2 = get_stroke_count(name2)
    score = 100 - abs(total1 - total2) * 3
    return max(0, min(score, 100))

# 🎨 빈티지 스타일
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');

    html, body, [class*="css"] {
        font-family: 'Special+Elite', monospace;
        background-color: #f8f1e5;
        color: #4b3b2f;
    }

    .title {
        font-size: 48px;
        text-align: center;
        margin-bottom: 10px;
        color: #6e4f3a;
    }

    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #9c7e65;
    }

    .result-box {
        border: 2px dashed #7b5e43;
        background-color: #fdf6e3;
        padding: 20px;
        border-radius: 8px;
        margin-top: 30px;
        font-size: 18px;
    }

    .footer {
        font-size: 13px;
        text-align: center;
        color: #aaa;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀 🎞️
st.markdown('<div class="title">💌 이름 궁합 타자기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🪶 옛 감성으로 보는 두 사람의 인연 궁합 📜</div>', unsafe_allow_html=True)

# 입력 ✍️
name1 = st.text_input("🌸 당신의 이름", max_chars=10)
name2 = st.text_input("🌼 상대방 이름", max_chars=10)

# 결과 버튼
if st.button("🔍 이름 궁합 보기"):
    if name1 and name2:
        score = calculate_compatibility(name1, name2)

        # 감성 메시지 💘
        if score >= 90:
            message = "🌟 운명적인 만남이에요! 두 분은 찰떡궁합 💑"
        elif score >= 70:
            message = "💖 서로 잘 이해하고 배려할 수 있는 커플이에요!"
        elif score >= 50:
            message = "🌿 대화와 노력이 필요하지만 괜찮은 궁합이에요."
        else:
            message = "📦 인연을 이어가려면 서로를 더 알아가야 해요."

        st.markdown(f"""
            <div class="result-box">
                ✉️ <b>{name1}</b> ❤️ <b>{name2}</b><br><br>
                🔢 획수 궁합 점수: <b>{score}%</b><br><br>
                {message}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("이름을 모두 입력해주세요 💬")

# Footer 📼
st.markdown('<div class="footer">📻 made with love by Vintage Harmony Calculator</div>', unsafe_allow_html=True)
