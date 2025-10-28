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

background_path = "background.jpg"
background_secondary = "background_1.jpg"

backgr = get_img_as_base64(background_path)
backgr2 = get_img_as_base64(background_secondary)

# ----------------------------------------------------
# THEME SETTINGS
# ----------------------------------------------------
PRIMARY = "#1E3A8A"       # Deep blue
ACCENT = "#4F46E5"        # Indigo
TEXT_LIGHT = "#F9FAFB"    # Off-white for dark backgrounds
TEXT_DARK = "#111827"     # Slate for light cards
CARD_BG = "rgba(255, 255, 255, 0.9)"  # Soft white for better visibility

# ----------------------------------------------------
# STYLING
# ----------------------------------------------------
st.markdown(f"""
<style>
    body {{
        color: {TEXT_DARK};
        font-family: 'Poppins', sans-serif;
    }}
    .stApp {{
        background-image: url("data:image/png;base64,{backgr}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    [data-baseweb="tab-list"] {{
        background: linear-gradient(90deg, {PRIMARY}, {ACCENT});
        border-radius: 0px;
        padding: 14px 0;
        text-align: center;
    }}
    h1, h2, h3, h4 {{
        color: {TEXT_LIGHT};
        font-weight: 700;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
    }}
    p, li {{
        color: {TEXT_DARK};
    }}
    .sub-caption {{
        font-size: 20px;
        color: {TEXT_LIGHT};
        opacity: 0.95;
    }}
    .fade-in {{
        animation: fadeIn 1.2s ease-in-out;
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
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
        background: {CARD_BG};
        border-radius: 14px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        padding: 24px;
        width: 300px;
        min-height: 270px;
        transition: transform 0.3s ease, background 0.3s ease, color 0.3s ease;
        backdrop-filter: blur(6px);
        color: {TEXT_DARK};
    }}
    .value-card:hover {{
        transform: translateY(-8px);
        background: {ACCENT};
        color: {TEXT_LIGHT};
    }}
    .footer {{
        margin-top: 50px;
        text-align: center;
        font-size: 14px;
        color: {TEXT_LIGHT};
        opacity: 0.9;
    }}
    .logo-banner {{
        width: 100%;
        display: flex;
        justify-content: center;
        background: linear-gradient(90deg, {PRIMARY}, {ACCENT});
        padding: 8px 0;
        opacity: 0.95;
    }}
    .logo-banner img {{
        width: 100%;
        max-width: 1200px;
        height: auto;
        object-fit: contain;
    }}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# LOGO BANNER
# ----------------------------------------------------
try:
    logo = Image.open("logo.png")
    st.markdown("<div class='logo-banner'>", unsafe_allow_html=True)
    st.image(logo, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
except Exception:
    st.markdown("<h2 style='text-align:center;'>TeachToEach 🎓</h2>", unsafe_allow_html=True)

# ----------------------------------------------------
# DEFINE TABS
# ----------------------------------------------------
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📘 Courses & Tutoring", "📞 Contact"])

# =====================================================
# TAB 1 — HOME
# =====================================================
with tab1:
    st.markdown('<div class="fade-in"><h1>Welcome to TeachToEach</h1></div>', unsafe_allow_html=True)
    st.markdown('<p class="sub-caption">Peer-Led Professional Classes: Empowering Students to Teach & Learn from Each Other</p>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("""
    ### Our Mission  
    At **TeachToEach**, our mission is to make education accessible and empowering by connecting students who wish to learn with peers who are ready to teach.  
    We provide affordable, flexible tutoring and help students gain income through knowledge-sharing.
    """)

    # HOME VALUE CARDS
    st.markdown(f"""
    <div class="value-container">
        <div class="value-card"><h4>🎓 Affordable</h4><p>Low-cost peer tutoring designed for student budgets.</p></div>
        <div class="value-card"><h4>🕓 Flexible</h4><p>Learn online or in-person at times that suit your schedule.</p></div>
        <div class="value-card"><h4>💡 Earn & Grow</h4><p>Students can share their skills and earn as verified tutors.</p></div>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("## How It Works — Student Guide")
    st.markdown("""
    1️⃣ **Browse Courses:** Explore peer-led classes suited to your interests.  
    2️⃣ **Select Tutor:** Choose from trusted, rated student tutors ready to help.  
    3️⃣ **Book Sessions:** Reserve your preferred time slot online or in person.  
    4️⃣ **Review Tutors:** Rate your experience and help others choose effectively.
    """)
    
    st.markdown("#### Quick Video Guide")
    st.video("https://youtu.be/JMLsHI8aV0g?si=sGKxf2EQmJ5Leuva")

    st.markdown('<div class="footer">© 2025 TeachToEach • Peer-Led Learning Platform</div>', unsafe_allow_html=True)

# =====================================================
# TAB 2 — COURSES & TUTORING (Horizontal Layout)
# =====================================================
with tab2:
    st.markdown('<div class="fade-in"><h2>Courses & Tutoring</h2></div>', unsafe_allow_html=True)
    st.markdown('<p class="fade-in" style="color:#F9FAFB;">Explore our featured peer-led sessions designed for students by students.</p>', unsafe_allow_html=True)

    # Standalone image (WEBP)
    course_img_path = "image.webp"
    if os.path.exists(course_img_path):
        st.image(course_img_path, caption="Learn. Teach. Grow.", use_container_width=True)

    # Horizontal container for course cards
    st.markdown(f"""
    <div class="value-container">
        <div class="value-card">
            <h4>🐍 Python for Beginners</h4>
            <p><strong>Tutor:</strong> Alex M.</p>
            <p><strong>Duration:</strong> 4 weeks</p>
            <p><strong>Price:</strong> R120 / session</p>
            <p>Learn Python basics, coding logic, and essential programming skills.</p>
        </div>
        <div class="value-card">
            <h4>📝 Academic Writing & Research</h4>
            <p><strong>Tutor:</strong> Sarah L.</p>
            <p><strong>Duration:</strong> 6 weeks</p>
            <p><strong>Price:</strong> R100 / session</p>
            <p>Develop strong writing, referencing, and research presentation skills.</p>
        </div>
        <div class="value-card">
            <h4>📊 Excel for Data Analysis</h4>
            <p><strong>Tutor:</strong> Thabo K.</p>
            <p><strong>Duration:</strong> 3 weeks</p>
            <p><strong>Price:</strong> R90 / session</p>
            <p>Analyze, clean, and visualize data effectively using Microsoft Excel.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("### Become a Tutor")
    st.info("Share your skills and earn by becoming a verified TeachToEach tutor. Email us at info@teachtoeach.com to apply.")

# =====================================================
# TAB 3 — CONTACT
# =====================================================
with tab3:
    st.markdown("<h2 style='color:#F9FAFB;'>Contact Us</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color:#F9FAFB;'>📧 <b>Email:</b> info@teachtoeach.com<br>
    ☎️ <b>Phone:</b> +27 68 760 3568</p>
    """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("<h3 style='color:#F9FAFB;'>Quick Contact Form</h3>", unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        if st.form_submit_button("Send Message"):
            st.success("Thank you! We’ll get back to you soon via email.")

    st.markdown('<div class="footer">© 2025 TeachToEach • Empowering Students Through Peer Learning</div>', unsafe_allow_html=True)
