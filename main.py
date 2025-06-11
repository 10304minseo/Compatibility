import streamlit as st

# 한글 자모의 획수 사전 (예시, 더 정교하게 확장 가능)
hangeul_stroke = {
    'ㄱ': 2, 'ㄲ': 4, 'ㄴ': 2, 'ㄷ': 3, 'ㄸ': 6, 'ㄹ': 5, 'ㅁ': 4, 'ㅂ': 4, 'ㅃ': 8, 'ㅅ': 2,
    'ㅆ': 4, 'ㅇ': 1, 'ㅈ': 3, 'ㅉ': 6, 'ㅊ': 4, 'ㅋ': 3, 'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 3,
    'ㅏ': 2, 'ㅑ': 3, 'ㅓ': 2, 'ㅕ': 3, 'ㅗ': 2, 'ㅛ': 3, 'ㅜ': 2, 'ㅠ': 3,
    'ㅡ': 1, 'ㅣ': 1, 'ㅐ': 3, 'ㅔ': 3, 'ㅒ': 4, 'ㅖ': 4, 'ㅚ': 3, 'ㅟ': 3,
    'ㅙ': 4, 'ㅞ': 4, 'ㅢ': 2
}

from hangul_utils import split_syllable_char  # 외부 모듈 필요
# 설치: pip install hangul-utils

def get_stroke_count(name):
    total = 0
    for char in name:
        if not ('가' <= char <= '힣'):
            continue
        chosung, jungsung, jongsung = split_syllable_char(char)
        total += hangeul_stroke.get(chosung, 1)
        total += hangeul_stroke.get(jungsung, 1)
        if jongsung:
            total += hangeul_stroke.get(jongsung, 1)
    return total

def calculate_compatibility(name1, name2):
    total1 = get_stroke_count(name1)
    total2 = get_stroke_count(name2)
    score = 100 - abs(total1 - total2) * 3
    return max(0, min(score, 100))

# 🎨 빈티지 스타일 설정
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');

    html, body, [class*="css"] {
        font-family: 'Special Elite', monospace;
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

# 입력 폼 ✍️
name1 = st.text_input("🌸 당신의 이름", max_chars=10)
name2 = st.text_input("🌼 상대방 이름", max_chars=10)

# 결과 버튼
if st.button("🔍 이름 궁합 보기"):
    if name1 and name2:
        score = calculate_compatibility(name1, name2)

        # 💘 이모지 기반 감성 메시지
        if score >= 90:
            message = "🌟 운명적인 만남이에요! 두 분은 찰떡궁합 💑"
        elif score >= 70:
            message = "💖 서로 잘 이해하고 배려할 수 있는 커플이에요!"
        elif score >= 50:
            message = "🌿 대화와 노력이 필요하지만 괜찮은 궁합이에요."
        else:
            message = "📦 인연을 이어가려면 서로를 더 알아가야 해요."

        # 출력 결과
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
