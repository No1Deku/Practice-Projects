import os, base64
import streamlit as st
from PIL import Image

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(page_title="TeachToEach", layout="wide", page_icon="🎓")

# ----------------------------------------------------
# HELPER: Convert Image to Base64
# ----------------------------------------------------
@st.cache_data
def get_img_as_base64(file_path: str) -> str | None:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


# ----------------------------------------------------
# COLOUR PALETTE (Based on your new scheme)
# ----------------------------------------------------
HEADER_GOLD = "#F2D8A7"      # Gold for headers and captivating text
TEXT_BODY = "#F2F2F2"        # Light for regular text
BG_DARK1 = "#8C8C8C"
BG_DARK2 = "#262626"
BG_DARK3 = "#0D0D0D"

# Create background gradient
BACKGROUND_STYLE = f"linear-gradient(135deg, {BG_DARK3}, {BG_DARK2}, {BG_DARK1});"

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------
st.markdown(f"""
<style>
    body {{
        background: {BACKGROUND_STYLE};
        font-family: 'Poppins', sans-serif;
        color: {TEXT_BODY};
    }}

    .stApp {{
        background: {BACKGROUND_STYLE};
    }}

    /* Header */
    h1, h2, h3, h4 {{
        color: {HEADER_GOLD};
        font-weight: 700;
    }}

    p {{
        color: {TEXT_BODY};
        font-size: 16px;
    }}

    /* Navbar-like Tabs */
    div[data-baseweb="tab-list"] {{
        justify-content: center;
        background: {BG_DARK2};
        border-radius: 12px;
        padding: 6px;
    }}

    div[data-baseweb="tab"] {{
        color: {TEXT_BODY};
        font-weight: 600;
    }}

    div[data-baseweb="tab"][aria-selected="true"] {{
        color: black !important;
        background-color: {HEADER_GOLD} !important;
        border-radius: 8px;
    }}

    /* Cue Cards */
    .card {{
        background-color: {HEADER_GOLD};
        color: black;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 4px 16px rgba(0,0,0,0.4);
        transition: 0.3s;
    }}

    .card:hover {{
        transform: translateY(-6px);
        box-shadow: 0px 6px 20px rgba(0,0,0,0.5);
    }}

    .footer {{
        margin-top: 40px;
        text-align: center;
        font-size: 14px;
        opacity: 0.8;
        color: {TEXT_BODY};
    }}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# LOGO
# ----------------------------------------------------
logo_path = "ETS-exam website/Logo.png"
logo_base64 = get_img_as_base64(logo_path)

# ----------------------------------------------------
# PAGE NAVIGATION (TABS)
# ----------------------------------------------------
tab_home, tab_courses, tab_contact = st.tabs(["🏠 Home", "📘 Courses & Training", "📞 Contact"])

# ----------------------------------------------------
# HOME TAB
# ----------------------------------------------------
with tab_home:
    col1, col2 = st.columns([1, 3])
    with col1:
        if logo_base64:
            st.markdown(f"<img src='data:image/png;base64,{logo_base64}' width='100'>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h1>Welcome to <span style='color:{HEADER_GOLD}'>TeachToEach</span></h1>", unsafe_allow_html=True)
        st.markdown(f"<p>Peer-Led Professional Classes: Empowering Students to Teach & Learn from Each Other.</p>", unsafe_allow_html=True)

    st.write("---")

    # Visual Cue Cards
    st.markdown("### Our Mission")
    colA, colB, colC = st.columns(3)
    with colA:
        st.markdown(f"<div class='card'><h4>Affordable</h4><p>Low-cost peer tutoring designed for student budgets.</p></div>", unsafe_allow_html=True)
    with colB:
        st.markdown(f"<div class='card'><h4>Flexible</h4><p>Learn online or in-person at times that suit your schedule.</p></div>", unsafe_allow_html=True)
    with colC:
        st.markdown(f"<div class='card'><h4>Earn & Grow</h4><p>Students can share their skills and earn as verified tutors.</p></div>", unsafe_allow_html=True)

    st.write("")
    st.image("https://via.placeholder.com/800x400?text=Learning+Together", use_container_width=True)

    st.markdown('<div class="footer">© 2025 TeachToEach • Peer-Led Learning Platform</div>', unsafe_allow_html=True)


# ----------------------------------------------------
# COURSES & TRAINING TAB
# ----------------------------------------------------
with tab_courses:
    st.markdown(f"<h2>Courses & Training</h2>", unsafe_allow_html=True)
    st.write("Explore our diverse range of skill-enhancing courses:")

    col1, col2, col3 = st.columns(3)
    courses = [
        {"name": "Data Analysis for Beginners", "tutor": "John Smith", "price": "$150", "mode": "Online"},
        {"name": "Creative Design Masterclass", "tutor": "Lisa Adams", "price": "$200", "mode": "Hybrid"},
        {"name": "Entrepreneurship Essentials", "tutor": "Michael Lee", "price": "$180", "mode": "In-Person"},
    ]

    for col, c in zip([col1, col2, col3], courses):
        with col:
            st.markdown(f"""
            <div class='card'>
                <h4>{c["name"]}</h4>
                <p><b>Tutor:</b> {c["tutor"]}</p>
                <p><b>Price:</b> {c["price"]}</p>
                <p><b>Mode:</b> {c["mode"]}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="footer">Grow, Learn, and Succeed with TeachToEach</div>', unsafe_allow_html=True)


# ----------------------------------------------------
# CONTACT TAB
# ----------------------------------------------------
with tab_contact:
    st.markdown(f"<h2>Contact Us</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <p><b>Phone:</b> +1 234 567 890</p>
        <p><b>Email:</b> contact@teachtoeach.com</p>
        <p><b>Website:</b> www.teachtoeach.com</p>
        <p><b>WhatsApp:</b> +1 234 567 890</p>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### Leave Us a Review")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        feedback = st.text_area("Your Review")
        if st.button("Submit Feedback"):
            if name and feedback:
                st.success("✅ Thank you for your feedback!")
            else:
                st.warning("Please fill in all required fields.")

    st.markdown('<div class="footer">We appreciate your time and feedback 🌟</div>', unsafe_allow_html=True)
