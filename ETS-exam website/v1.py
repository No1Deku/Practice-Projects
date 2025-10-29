import os, base64
import streamlit as st
from PIL import Image

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(page_title="TeachToEach", layout="wide", page_icon="🎓")

# ----------------------------------------------------
# BACKGROUND IMAGE SETUP
# ----------------------------------------------------
@st.cache_data
def get_img_as_base64(file_path: str) -> str | None:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

# ----------------------------------------------------
# COLOUR PALETTE (from provided image)
# ----------------------------------------------------
BACKGROUND = "#1C1B19"
CARD_BG = "#2B2A27"
ACCENT = "#D6B46E"
TEXT_LIGHT = "#EAE6DA"
TEXT_SECONDARY = "#A9A59D"
SHADOW = "rgba(0,0,0,0.5)"

# ----------------------------------------------------
# STYLING
# ----------------------------------------------------
st.markdown(f"""
<style>
    /* General Body Styling */
    body {{
        background-color: {BACKGROUND};
        color: {TEXT_LIGHT};
        font-family: 'Poppins', sans-serif;
    }}

    .stApp {{
        background-color: {BACKGROUND};
    }}

    /* Navigation Bar */
    .navbar {{
        position: fixed;
        top: 0;
        width: 100%;
        background-color: {BACKGROUND};
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 40px;
        z-index: 100;
        border-bottom: 1px solid {CARD_BG};
    }}

    .nav-left img {{
        height: 35px;
        width: auto;
        cursor: pointer;
    }}

    .nav-center {{
        color: {ACCENT};
        font-weight: 600;
        font-size: 18px;
        text-align: center;
    }}

    .nav-right {{
        color: {TEXT_LIGHT};
        font-weight: 500;
        font-size: 18px;
        cursor: pointer;
    }}

    /* Header Section */
    h1 {{
        color: {ACCENT};
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    h2, h3 {{
        color: {ACCENT};
    }}

    p {{
        color: {TEXT_SECONDARY};
    }}

    /* Value Cards */
    .value-container {{
        display: flex;
        justify-content: center;
        align-items: flex-start;
        flex-wrap: wrap;
        gap: 30px;
        margin-top: 25px;
        text-align: center;
    }}

    .value-card {{
        background-color: {CARD_BG};
        border-radius: 12px;
        box-shadow: 0 4px 16px {SHADOW};
        padding: 24px;
        width: 280px;
        transition: all 0.3s ease;
        color: {TEXT_LIGHT};
    }}

    .value-card:hover {{
        transform: translateY(-6px);
        background-color: {ACCENT};
        color: {BACKGROUND};
    }}

    /* Footer */
    .footer {{
        margin-top: 60px;
        text-align: center;
        font-size: 14px;
        color: {TEXT_SECONDARY};
        opacity: 0.8;
    }}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# NAVIGATION BAR
# ----------------------------------------------------
st.markdown("<div class='navbar'>", unsafe_allow_html=True)

# Left (Home Logo)
try:
    logo_small = Image.open("ETS-exam website/Logo.png")
    logo_base64 = get_img_as_base64("ETS-exam website/Logo.png")
    st.markdown(f"""
        <div class='nav-left'>
            <img src="data:image/png;base64,{logo_base64}" alt="Home Logo">
        </div>
    """, unsafe_allow_html=True)
except Exception:
    st.markdown("<div class='nav-left'>🏠</div>", unsafe_allow_html=True)

# Center (Courses)
st.markdown("<div class='nav-center'>Courses & Training</div>", unsafe_allow_html=True)

# Right (Contact)
st.markdown("<div class='nav-right'>Contact</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")  
st.write("")  
st.write("")  # spacing under navbar

# ----------------------------------------------------
# HOME SECTION
# ----------------------------------------------------
with st.container():
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("ETS-exam website/Logo.png"):
            st.image("ETS-exam website/Logo.png", width=55)
    with col2:
        st.markdown(f"<h1>Welcome to <span style='color:{TEXT_LIGHT}'>TeachToEach</span></h1>", unsafe_allow_html=True)

    st.markdown(f"<p>Peer-Led Professional Classes: Empowering Students to Teach & Learn from Each Other.</p>", unsafe_allow_html=True)
    st.write("---")

    st.markdown(f"""
    <div class="value-container">
        <div class="value-card"><h4>Affordable</h4><p>Low-cost peer tutoring designed for student budgets.</p></div>
        <div class="value-card"><h4>Flexible</h4><p>Learn online or in-person at times that suit your schedule.</p></div>
        <div class="value-card"><h4>Earn & Grow</h4><p>Students can share their skills and earn as verified tutors.</p></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">© 2025 TeachToEach • Peer-Led Learning Platform</div>', unsafe_allow_html=True)
