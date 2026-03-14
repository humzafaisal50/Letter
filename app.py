import streamlit as st
import os
import base64
PASSWORD = "neenuu2803"

password_input = st.text_input("Enter password to open the letter ❤️", type="password")

if password_input != PASSWORD:
    st.stop()

st.set_page_config(
    page_title="For My Neenuu ❤️",
    layout="centered"
)

def load_letter():
    if os.path.exists("letter.txt"):
        with open("letter.txt", "r", encoding="utf-8") as f:
            return f.read()
    return "Add your letter in letter.txt"

def file_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def get_audio_html(audio_path):
    if not os.path.exists(audio_path):
        return ""
    audio_base64 = file_to_base64(audio_path)
    return f"""
    <audio autoplay loop controls style="width:100%; margin-top:10px; border-radius:12px;">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    """

letter_text = load_letter()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Playfair Display', serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, #fff7fb 0%, #ffe9f3 35%, #ffd9e8 70%, #fff0f6 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 900px;
}

.main-title {
    text-align: center;
    font-size: 76px;
    color: #c2185b;
    font-family: 'Great Vibes', cursive;
    margin-bottom: 8px;
    text-shadow: 0 0 12px rgba(194, 24, 91, 0.18);
    animation: glowPulse 3s ease-in-out infinite;
}

.subtitle {
    text-align: center;
    font-size: 24px;
    color: #6d214f;
    margin-bottom: 28px;
    font-style: italic;
}

.cover-image-box {
    background: rgba(255,255,255,0.82);
    padding: 18px;
    border-radius: 26px;
    box-shadow: 0 12px 35px rgba(168, 40, 90, 0.16);
    margin-bottom: 28px;
    backdrop-filter: blur(6px);
}

.section-heading {
    text-align: center;
    font-size: 34px;
    color: #ad1457;
    font-family: 'Playfair Display', serif;
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 700;
}

.audio-box {
    background: rgba(255,255,255,0.88);
    padding: 24px;
    border-radius: 24px;
    box-shadow: 0 10px 28px rgba(168, 40, 90, 0.12);
    margin-bottom: 24px;
}

.countdown-card {
    background: rgba(255,255,255,0.9);
    padding: 26px;
    border-radius: 24px;
    box-shadow: 0 10px 28px rgba(168, 40, 90, 0.14);
    margin-bottom: 28px;
}

.typing-wrapper {
    background: rgba(255,255,255,0.94);
    padding: 42px;
    border-radius: 28px;
    box-shadow: 0 16px 40px rgba(168, 40, 90, 0.18);
    margin-top: 18px;
    margin-bottom: 26px;
    border: 1px solid rgba(194, 24, 91, 0.10);
}

.typing-box {
    font-size: 32px;
    line-height: 2.0;
    color: #3d1c2e;
    font-family: 'Playfair Display', serif;
    min-height: 780px;
    white-space: pre-wrap;
    border-right: 2px solid #c2185b;
    padding-right: 8px;
}

.footer-text {
    text-align: center;
    color: #c2185b;
    font-size: 40px;
    margin-top: 22px;
    font-family: 'Great Vibes', cursive;
}

.small-romantic-line {
    text-align: center;
    color: #7b2952;
    font-size: 18px;
    margin-top: 6px;
    margin-bottom: 10px;
    font-style: italic;
}

.heart {
    position: fixed;
    bottom: -20px;
    color: rgba(255, 105, 180, 0.45);
    font-size: 24px;
    animation: floatUp linear infinite;
    pointer-events: none;
    z-index: 9999;
}

.heart:nth-child(1) { left: 8%; animation-duration: 11s; }
.heart:nth-child(2) { left: 18%; animation-duration: 9s; }
.heart:nth-child(3) { left: 32%; animation-duration: 13s; }
.heart:nth-child(4) { left: 47%; animation-duration: 10s; }
.heart:nth-child(5) { left: 61%; animation-duration: 14s; }
.heart:nth-child(6) { left: 75%; animation-duration: 12s; }
.heart:nth-child(7) { left: 88%; animation-duration: 10s; }

@keyframes floatUp {
    0% {
        transform: translateY(0) translateX(0) scale(1);
        opacity: 0;
    }
    10% {
        opacity: 1;
    }
    100% {
        transform: translateY(-110vh) translateX(30px) scale(1.4);
        opacity: 0;
    }
}

@keyframes glowPulse {
    0% { text-shadow: 0 0 10px rgba(194, 24, 91, 0.10); }
    50% { text-shadow: 0 0 22px rgba(194, 24, 91, 0.28); }
    100% { text-shadow: 0 0 10px rgba(194, 24, 91, 0.10); }
}

@media (max-width: 768px) {
    .main-title {
        font-size: 54px;
    }

    .typing-box {
        font-size: 24px;
        line-height: 1.8;
        min-height: 680px;
    }

    .section-heading {
        font-size: 28px;
    }
}
</style>

<div class="heart">♥</div>
<div class="heart">♥</div>
<div class="heart">♥</div>
<div class="heart">♥</div>
<div class="heart">♥</div>
<div class="heart">♥</div>
<div class="heart">♥</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">My Letter</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">For My Neenuu ❤️</div>', unsafe_allow_html=True)

if os.path.exists("cover.jpg"):
    st.markdown('<div class="cover-image-box">', unsafe_allow_html=True)
    st.image("cover.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-heading">🎵 Our Song</div>', unsafe_allow_html=True)
st.markdown('<div class="audio-box">', unsafe_allow_html=True)
music_html = get_audio_html("song.mp3")
if music_html:
    st.markdown(music_html, unsafe_allow_html=True)
st.markdown('<div class="small-romantic-line">A little music for a love that waited through distance.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-heading">💍 Countdown To Our Wedding</div>', unsafe_allow_html=True)

countdown_html = """
<div class="countdown-card">
    <div id="countdown" style="font-size:30px; color:#4a2238; font-family:'Playfair Display', serif; text-align:center; font-weight:600;"></div>
    <div style="text-align:center; color:#8a3b62; margin-top:10px; font-style:italic;">
        Every second brings us closer to forever.
    </div>
</div>

<script>
const weddingDate = new Date("Mar 28, 2026 00:00:00").getTime();

setInterval(function() {
    const now = new Date().getTime();
    const distance = weddingDate - now;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("countdown").innerHTML =
    days + " days  " + hours + " hours  " + minutes + " minutes  " + seconds + " seconds";
}, 1000);
</script>
"""

st.components.v1.html(countdown_html, height=160)

st.markdown('<div class="section-heading">💌 My Letter To You</div>', unsafe_allow_html=True)

safe_letter = (
    letter_text
    .replace("&", "&amp;")
    .replace("<", "&lt;")
    .replace(">", "&gt;")
)

typing_html = f"""
<div class="typing-wrapper">
    <div id="typing" class="typing-box"></div>
</div>

<script>
const text = `{safe_letter}`;
let i = 0;

function typeWriter() {{
    if (i < text.length) {{
        document.getElementById("typing").innerHTML += text.charAt(i) === "\\n" ? "<br>" : text.charAt(i);
        i++;
        setTimeout(typeWriter, 18);
    }}
}}

typeWriter();
</script>
"""

st.components.v1.html(typing_html, height=980, scrolling=True)

st.markdown("""
<div class="footer-text">
Forever yours,<br>
Hamza ❤️
</div>
""", unsafe_allow_html=True)