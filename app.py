"""
Time Series NPTL Quiz Dashboard
A beautiful Streamlit-based quiz application for NPTEL Time Series Analysis course.
"""

import streamlit as st
import random
import time
from questions import QUIZ_DATA

# ─────────────────────────────────────────────────
# Page Configuration
# ─────────────────────────────────────────────────
st.set_page_config(
    page_title="Time Series NPTL Quiz",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────
# Custom CSS for Premium White Theme
# ─────────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Google Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

    /* ── Root Variables ── */
    :root {
        --bg-primary: #FFFFFF;
        --bg-secondary: #F8F9FC;
        --bg-card: #FFFFFF;
        --text-primary: #1A1D2E;
        --text-secondary: #5A607F;
        --text-muted: #8E94B2;
        --accent-primary: #6366F1;
        --accent-secondary: #818CF8;
        --accent-gradient: linear-gradient(135deg, #6366F1 0%, #8B5CF6 50%, #A78BFA 100%);
        --success: #10B981;
        --success-bg: #ECFDF5;
        --success-border: #A7F3D0;
        --error: #EF4444;
        --error-bg: #FEF2F2;
        --error-border: #FECACA;
        --warning: #F59E0B;
        --border: #E5E7EB;
        --border-light: #F0F1F5;
        --shadow-sm: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.03);
        --shadow-md: 0 4px 16px rgba(0,0,0,0.06), 0 2px 4px rgba(0,0,0,0.04);
        --shadow-lg: 0 10px 40px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.04);
        --shadow-accent: 0 4px 20px rgba(99, 102, 241, 0.25);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --radius-xl: 20px;
    }

    /* ── Global Styles ── */
    .stApp {
        background: var(--bg-secondary) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    .main .block-container {
        max-width: 900px;
        padding: 2rem 1.5rem 4rem;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: var(--bg-primary) !important;
        border-right: 1px solid var(--border-light) !important;
    }

    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown li,
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: var(--text-primary) !important;
    }

    /* ── Typography ── */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        color: var(--text-primary) !important;
    }

    p, li, span, div {
        font-family: 'Inter', sans-serif !important;
    }

    /* ── Radio Buttons (Quiz Options) ── */
    .stRadio > div {
        gap: 0.5rem !important;
    }

    .stRadio > div > label {
        background: var(--bg-primary) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        padding: 0.875rem 1.25rem !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
    }

    .stRadio > div > label:hover {
        border-color: var(--accent-primary) !important;
        background: #F5F3FF !important;
        transform: translateY(-1px);
        box-shadow: var(--shadow-sm) !important;
    }

    .stRadio > div > label[data-checked="true"],
    .stRadio > div > label:has(input:checked) {
        border-color: var(--accent-primary) !important;
        background: #EEF2FF !important;
        box-shadow: var(--shadow-accent) !important;
    }

    /* ── Buttons ── */
    .stButton > button {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        border-radius: var(--radius-md) !important;
        padding: 0.65rem 2rem !important;
        border: none !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        letter-spacing: 0.01em;
    }

    .stButton > button[kind="primary"],
    .stButton > button:first-child {
        background: var(--accent-gradient) !important;
        color: white !important;
        box-shadow: var(--shadow-accent) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 24px rgba(99, 102, 241, 0.35) !important;
    }

    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* ── Metric Cards ── */
    div[data-testid="stMetric"] {
        background: var(--bg-primary);
        border: 1px solid var(--border-light);
        border-radius: var(--radius-lg);
        padding: 1.25rem;
        box-shadow: var(--shadow-sm);
    }

    div[data-testid="stMetric"] label {
        color: var(--text-muted) !important;
        font-size: 0.8rem !important;
        font-weight: 500 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
    }

    /* ── Progress Bar ── */
    .stProgress > div > div {
        background: var(--border-light) !important;
        border-radius: 99px !important;
        height: 8px !important;
    }

    .stProgress > div > div > div {
        background: var(--accent-gradient) !important;
        border-radius: 99px !important;
    }

    /* ── Expander ── */
    .streamlit-expanderHeader {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        background: var(--bg-primary) !important;
        border: 1px solid var(--border-light) !important;
        border-radius: var(--radius-md) !important;
    }

    /* ── Divider ── */
    hr {
        border-color: var(--border-light) !important;
    }

    /* ── Success / Error Alerts ── */
    .stAlert [data-testid="stMarkdownContainer"] p {
        font-size: 0.95rem !important;
    }

    /* ── Custom Components ── */
    .hero-banner {
        background: var(--accent-gradient);
        border-radius: var(--radius-xl);
        padding: 2.5rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-lg);
        position: relative;
        overflow: hidden;
    }

    .hero-banner::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 40%, rgba(255,255,255,0.15) 0%, transparent 50%),
                    radial-gradient(circle at 70% 80%, rgba(255,255,255,0.1) 0%, transparent 40%);
        animation: shimmer 8s ease-in-out infinite alternate;
    }

    @keyframes shimmer {
        0% { transform: translate(0, 0) rotate(0deg); }
        100% { transform: translate(-5%, 5%) rotate(2deg); }
    }

    .hero-banner h1 {
        color: #FFFFFF !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.25rem !important;
        position: relative;
        z-index: 1;
        letter-spacing: -0.02em;
    }

    .hero-banner p {
        color: rgba(255,255,255,0.88) !important;
        font-size: 1.05rem !important;
        font-weight: 400 !important;
        position: relative;
        z-index: 1;
    }

    .question-card {
        background: var(--bg-primary);
        border: 1px solid var(--border-light);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: var(--shadow-md);
        transition: box-shadow 0.3s ease;
    }

    .question-card:hover {
        box-shadow: var(--shadow-lg);
    }

    .question-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: var(--accent-gradient);
        color: white;
        font-weight: 700;
        font-size: 0.85rem;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        margin-right: 0.75rem;
        flex-shrink: 0;
    }

    .question-text {
        font-size: 1.05rem;
        font-weight: 600;
        color: var(--text-primary);
        line-height: 1.6;
    }

    .week-card {
        background: var(--bg-primary);
        border: 1.5px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 1.25rem 1.5rem;
        margin-bottom: 0.75rem;
        cursor: pointer;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .week-card:hover {
        border-color: var(--accent-primary);
        box-shadow: var(--shadow-md);
        transform: translateY(-2px);
    }

    .week-card.active {
        border-color: var(--accent-primary);
        background: #EEF2FF;
        box-shadow: var(--shadow-accent);
    }

    .stat-card {
        background: var(--bg-primary);
        border: 1px solid var(--border-light);
        border-radius: var(--radius-lg);
        padding: 1.5rem;
        text-align: center;
        box-shadow: var(--shadow-sm);
        transition: all 0.3s ease;
    }

    .stat-card:hover {
        box-shadow: var(--shadow-md);
        transform: translateY(-2px);
    }

    .stat-value {
        font-size: 2rem;
        font-weight: 800;
        background: var(--accent-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .stat-label {
        font-size: 0.8rem;
        font-weight: 500;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-top: 0.25rem;
    }

    .result-correct {
        background: var(--success-bg);
        border: 1.5px solid var(--success-border);
        border-radius: var(--radius-md);
        padding: 1rem 1.25rem;
        margin: 0.5rem 0;
    }

    .result-incorrect {
        background: var(--error-bg);
        border: 1.5px solid var(--error-border);
        border-radius: var(--radius-md);
        padding: 1rem 1.25rem;
        margin: 0.5rem 0;
    }

    .explanation-box {
        background: #F5F3FF;
        border-left: 4px solid var(--accent-primary);
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        padding: 1rem 1.25rem;
        margin-top: 0.75rem;
        font-size: 0.92rem;
        color: var(--text-secondary);
        line-height: 1.6;
    }

    .badge {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.3rem 0.85rem;
        border-radius: 99px;
        font-size: 0.78rem;
        font-weight: 600;
    }

    .badge-success {
        background: var(--success-bg);
        color: var(--success);
        border: 1px solid var(--success-border);
    }

    .badge-error {
        background: var(--error-bg);
        color: var(--error);
        border: 1px solid var(--error-border);
    }

    .badge-neutral {
        background: #F0F1F5;
        color: var(--text-muted);
        border: 1px solid var(--border);
    }

    .score-display {
        text-align: center;
        padding: 2.5rem 2rem;
        background: var(--bg-primary);
        border-radius: var(--radius-xl);
        border: 1px solid var(--border-light);
        box-shadow: var(--shadow-lg);
        margin: 1.5rem 0;
    }

    .score-circle {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1.5rem;
        font-size: 2.5rem;
        font-weight: 800;
        color: white;
        box-shadow: 0 8px 30px rgba(99, 102, 241, 0.3);
    }

    .score-excellent { background: linear-gradient(135deg, #10B981, #059669); box-shadow: 0 8px 30px rgba(16, 185, 129, 0.3); }
    .score-good { background: linear-gradient(135deg, #6366F1, #8B5CF6); }
    .score-average { background: linear-gradient(135deg, #F59E0B, #D97706); box-shadow: 0 8px 30px rgba(245, 158, 11, 0.3); }
    .score-poor { background: linear-gradient(135deg, #EF4444, #DC2626); box-shadow: 0 8px 30px rgba(239, 68, 68, 0.3); }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 99px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }

    /* ── Hide Streamlit Branding ── */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* ── Sidebar Week Selector ── */
    .sidebar-section-title {
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--text-muted);
        margin: 1.5rem 0 0.75rem 0;
    }

    /* ── Code Blocks in Questions ── */
    code {
        font-family: 'JetBrains Mono', monospace !important;
        background: #F5F3FF !important;
        color: var(--accent-primary) !important;
        padding: 0.15rem 0.45rem !important;
        border-radius: 4px !important;
        font-size: 0.88em !important;
    }

    pre code {
        display: block;
        padding: 1rem !important;
        border-radius: var(--radius-md) !important;
        background: #1E1E2E !important;
        color: #CDD6F4 !important;
        font-size: 0.85rem !important;
        line-height: 1.6 !important;
        overflow-x: auto;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────
# Session State Initialization
# ─────────────────────────────────────────────────
def init_session_state():
    """Initialize all session state variables."""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"
    if "selected_week" not in st.session_state:
        st.session_state.selected_week = None
    if "quiz_mode" not in st.session_state:
        st.session_state.quiz_mode = None  # "practice" or "test"
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    if "quiz_history" not in st.session_state:
        st.session_state.quiz_history = {}
    if "shuffled_questions" not in st.session_state:
        st.session_state.shuffled_questions = None
    if "show_results" not in st.session_state:
        st.session_state.show_results = False


init_session_state()


# ─────────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────────
def get_score_class(percentage):
    """Get CSS class based on score percentage."""
    if percentage >= 80:
        return "score-excellent"
    elif percentage >= 60:
        return "score-good"
    elif percentage >= 40:
        return "score-average"
    else:
        return "score-poor"


def get_grade_emoji(percentage):
    """Get emoji based on score percentage."""
    if percentage >= 90:
        return "🏆"
    elif percentage >= 80:
        return "🌟"
    elif percentage >= 70:
        return "👏"
    elif percentage >= 60:
        return "👍"
    elif percentage >= 40:
        return "📚"
    else:
        return "💪"


def get_grade_message(percentage):
    """Get encouraging message based on score."""
    if percentage >= 90:
        return "Outstanding! You've mastered this topic!"
    elif percentage >= 80:
        return "Excellent work! Almost perfect!"
    elif percentage >= 70:
        return "Great job! You have a solid understanding."
    elif percentage >= 60:
        return "Good effort! A bit more practice will help."
    elif percentage >= 40:
        return "Keep studying! Review the explanations below."
    else:
        return "Don't give up! Review the material and try again."


def reset_quiz():
    """Reset quiz state for a new attempt."""
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.shuffled_questions = None
    st.session_state.show_results = False


def start_quiz(week, mode):
    """Start a new quiz."""
    reset_quiz()
    st.session_state.selected_week = week
    st.session_state.quiz_mode = mode
    st.session_state.current_page = "quiz"
    questions = QUIZ_DATA[week]["questions"].copy()
    if mode == "test":
        random.shuffle(questions)
    st.session_state.shuffled_questions = questions


def start_mixed_quiz(num_questions, selected_weeks):
    """Start a mixed quiz from selected weeks."""
    reset_quiz()
    all_questions = []
    for week_key in selected_weeks:
        for q in QUIZ_DATA[week_key]["questions"]:
            q_copy = q.copy()
            q_copy["source_week"] = week_key
            all_questions.append(q_copy)
    random.shuffle(all_questions)
    num_questions = min(num_questions, len(all_questions))
    st.session_state.shuffled_questions = all_questions[:num_questions]
    st.session_state.selected_week = "Mixed Quiz"
    st.session_state.quiz_mode = "test"
    st.session_state.current_page = "quiz"


# ─────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────
def render_sidebar():
    """Render the sidebar navigation."""
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0 0.5rem;">
            <div style="font-size: 2.5rem; margin-bottom: 0.25rem;">📉</div>
            <div style="font-size: 1.15rem; font-weight: 800; color: #1A1D2E; letter-spacing: -0.02em;">Time Series</div>
            <div style="font-size: 0.82rem; font-weight: 500; color: #5A607F;">NPTL Quiz Dashboard</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # Navigation
        if st.button("🏠  Home", use_container_width=True, key="nav_home"):
            st.session_state.current_page = "home"
            reset_quiz()
            st.rerun()

        if st.button("📊  Dashboard", use_container_width=True, key="nav_dash"):
            st.session_state.current_page = "dashboard"
            st.rerun()

        if st.button("🔀  Mixed Quiz", use_container_width=True, key="nav_mixed"):
            st.session_state.current_page = "mixed"
            reset_quiz()
            st.rerun()

        st.markdown('<div class="sidebar-section-title">Weekly Quizzes</div>', unsafe_allow_html=True)

        for week_key, week_data in QUIZ_DATA.items():
            icon = week_data["icon"]
            # Check history
            best = ""
            if week_key in st.session_state.quiz_history:
                scores = st.session_state.quiz_history[week_key]
                best_score = max(scores)
                best = f" — Best: {best_score}%"

            if st.button(f"{icon}  {week_key}{best}", use_container_width=True, key=f"nav_{week_key}"):
                st.session_state.selected_week = week_key
                st.session_state.current_page = "week_detail"
                reset_quiz()
                st.rerun()

        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; padding: 0.5rem 0;">
            <div style="font-size: 0.72rem; color: #8E94B2; line-height: 1.5;">
                NPTEL Time Series Analysis<br>
                Built with ❤️ using Streamlit
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────
# Home Page
# ─────────────────────────────────────────────────
def render_home():
    """Render the home page."""
    # Hero Banner
    st.markdown("""
    <div class="hero-banner">
        <h1>📉 Time Series NPTL Quiz</h1>
        <p>Master Time Series Analysis through interactive quizzes — from basics to advanced concepts</p>
    </div>
    """, unsafe_allow_html=True)

    # Stats Row
    total_questions = sum(len(w["questions"]) for w in QUIZ_DATA.values())
    total_weeks = len(QUIZ_DATA)
    attempted_weeks = len(st.session_state.quiz_history)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{total_weeks}</div>
            <div class="stat-label">Total Weeks</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{total_questions}</div>
            <div class="stat-label">Questions</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{attempted_weeks}</div>
            <div class="stat-label">Attempted</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        if st.session_state.quiz_history:
            avg_score = sum(
                max(scores) for scores in st.session_state.quiz_history.values()
            ) / len(st.session_state.quiz_history)
            avg_display = f"{avg_score:.0f}%"
        else:
            avg_display = "—"
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{avg_display}</div>
            <div class="stat-label">Avg Best Score</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Week Cards
    st.markdown("### 📚 Select a Week to Begin")
    st.markdown("")

    for week_key, week_data in QUIZ_DATA.items():
        col_icon, col_info, col_action = st.columns([0.8, 5, 2])

        with col_icon:
            st.markdown(f"<div style='font-size: 2.5rem; text-align: center; padding-top: 0.5rem;'>{week_data['icon']}</div>", unsafe_allow_html=True)

        with col_info:
            # Badge for completion status
            badge_html = ""
            if week_key in st.session_state.quiz_history:
                best = max(st.session_state.quiz_history[week_key])
                if best >= 80:
                    badge_html = f'<span class="badge badge-success">✓ Best: {best}%</span>'
                else:
                    badge_html = f'<span class="badge badge-neutral">Best: {best}%</span>'

            st.markdown(f"""
            <div style="padding: 0.5rem 0;">
                <div style="font-size: 1.1rem; font-weight: 700; color: #1A1D2E; margin-bottom: 0.2rem;">
                    {week_key} {badge_html}
                </div>
                <div style="font-size: 0.88rem; color: #5A607F;">
                    {week_data['title']} · {len(week_data['questions'])} questions
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_action:
            st.markdown("<div style='padding-top: 0.65rem;'>", unsafe_allow_html=True)
            if st.button("Start →", key=f"start_{week_key}", use_container_width=True):
                st.session_state.selected_week = week_key
                st.session_state.current_page = "week_detail"
                reset_quiz()
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")

    # Mixed Quiz Card
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🔀 Mixed Quiz — Test Across All Weeks")
    st.markdown("")

    col_icon, col_info, col_action = st.columns([0.8, 5, 2])
    with col_icon:
        st.markdown("<div style='font-size: 2.5rem; text-align: center; padding-top: 0.5rem;'>🔀</div>", unsafe_allow_html=True)
    with col_info:
        total_q = sum(len(w['questions']) for w in QUIZ_DATA.values())
        mixed_badge = ""
        if "Mixed Quiz" in st.session_state.quiz_history:
            mbest = max(st.session_state.quiz_history["Mixed Quiz"])
            if mbest >= 80:
                mixed_badge = f'<span class="badge badge-success">✓ Best: {mbest}%</span>'
            else:
                mixed_badge = f'<span class="badge badge-neutral">Best: {mbest}%</span>'
        st.markdown(f"""
        <div style="padding: 0.5rem 0;">
            <div style="font-size: 1.1rem; font-weight: 700; color: #1A1D2E; margin-bottom: 0.2rem;">
                Mixed Quiz {mixed_badge}
            </div>
            <div style="font-size: 0.88rem; color: #5A607F;">
                Shuffled questions from all {len(QUIZ_DATA)} weeks · {total_q} questions available
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_action:
        st.markdown("<div style='padding-top: 0.65rem;'>", unsafe_allow_html=True)
        if st.button("Configure →", key="start_mixed_home", use_container_width=True):
            st.session_state.current_page = "mixed"
            reset_quiz()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")


# ─────────────────────────────────────────────────
# Week Detail Page
# ─────────────────────────────────────────────────
def render_week_detail():
    """Render the week detail / mode selection page."""
    week_key = st.session_state.selected_week
    week_data = QUIZ_DATA[week_key]

    # Week Header
    st.markdown(f"""
    <div class="hero-banner" style="padding: 2rem;">
        <h1>{week_data['icon']} {week_key}</h1>
        <p>{week_data['title']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Info cards row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{len(week_data['questions'])}</div>
            <div class="stat-label">Questions</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if week_key in st.session_state.quiz_history:
            attempts = len(st.session_state.quiz_history[week_key])
        else:
            attempts = 0
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{attempts}</div>
            <div class="stat-label">Attempts</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if week_key in st.session_state.quiz_history:
            best = max(st.session_state.quiz_history[week_key])
            best_display = f"{best}%"
        else:
            best_display = "—"
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{best_display}</div>
            <div class="stat-label">Best Score</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Mode Selection
    st.markdown("### Choose Quiz Mode")
    st.markdown("")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("""
        <div class="stat-card" style="text-align: left; padding: 1.75rem;">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">📖</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #1A1D2E; margin-bottom: 0.4rem;">Practice Mode</div>
            <div style="font-size: 0.85rem; color: #5A607F; line-height: 1.6;">
                Answer questions one by one. See instant feedback with correct answers and explanations after each question.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("")
        if st.button("Start Practice", key="start_practice", use_container_width=True):
            start_quiz(week_key, "practice")
            st.rerun()

    with col_b:
        st.markdown("""
        <div class="stat-card" style="text-align: left; padding: 1.75rem;">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">🏆</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #1A1D2E; margin-bottom: 0.4rem;">Test Mode</div>
            <div style="font-size: 0.85rem; color: #5A607F; line-height: 1.6;">
                Answer all questions with shuffled order. See your score and detailed review only after submitting all answers.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("")
        if st.button("Start Test", key="start_test", use_container_width=True):
            start_quiz(week_key, "test")
            st.rerun()

    # Quick Look at Topics
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📋 Preview Question Topics"):
        for i, q in enumerate(week_data["questions"], 1):
            # Show first 80 chars of each question
            preview = q["question"][:90] + ("..." if len(q["question"]) > 90 else "")
            st.markdown(f"**Q{i}.** {preview}")


# ─────────────────────────────────────────────────
# Practice Mode
# ─────────────────────────────────────────────────
def render_practice_quiz():
    """Render quiz in practice mode — one question at a time with instant feedback."""
    week_key = st.session_state.selected_week
    week_data = QUIZ_DATA[week_key]
    questions = st.session_state.shuffled_questions
    total = len(questions)
    idx = st.session_state.current_question

    # Header
    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
        <div>
            <span style="font-size: 0.78rem; font-weight: 600; color: #8E94B2; text-transform: uppercase; letter-spacing: 0.06em;">
                {week_key} · Practice Mode
            </span>
            <div style="font-size: 1.25rem; font-weight: 700; color: #1A1D2E; margin-top: 0.15rem;">
                {week_data['title']}
            </div>
        </div>
        <div style="text-align: right;">
            <span class="badge badge-neutral">Question {idx + 1} of {total}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Progress
    st.progress((idx + 1) / total)

    # Show results page
    if st.session_state.show_results:
        render_results()
        return

    # Current Question
    q = questions[idx]
    q_key = f"practice_{week_key}_{idx}"

    st.markdown(f"""
    <div class="question-card">
        <div style="display: flex; align-items: flex-start;">
            <div class="question-number">{idx + 1}</div>
            <div class="question-text">{q['question']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Options
    selected = st.radio(
        "Select your answer:",
        options=q["options"],
        key=q_key,
        index=None,
        label_visibility="collapsed"
    )

    checked = st.session_state.answers.get(idx, {}).get("checked", False)

    col1, col2, col3 = st.columns([2, 2, 2])

    with col1:
        if idx > 0:
            if st.button("← Previous", key=f"prev_{idx}", use_container_width=True):
                st.session_state.current_question = idx - 1
                st.rerun()

    with col2:
        if not checked:
            if st.button("Check Answer ✓", key=f"check_{idx}", use_container_width=True):
                if selected is not None:
                    is_correct = (q["options"].index(selected) == q["correct"])
                    st.session_state.answers[idx] = {
                        "selected": selected,
                        "correct": is_correct,
                        "checked": True
                    }
                    st.rerun()
                else:
                    st.warning("⚠️ Please select an answer first.")

    with col3:
        if idx < total - 1:
            if st.button("Next →", key=f"next_{idx}", use_container_width=True):
                st.session_state.current_question = idx + 1
                st.rerun()
        else:
            if st.button("Finish Quiz 🏁", key=f"finish_{idx}", use_container_width=True):
                st.session_state.show_results = True
                # Save score
                correct_count = sum(1 for a in st.session_state.answers.values() if a.get("correct", False))
                pct = int((correct_count / total) * 100)
                if week_key not in st.session_state.quiz_history:
                    st.session_state.quiz_history[week_key] = []
                st.session_state.quiz_history[week_key].append(pct)
                st.rerun()

    # Show feedback if checked
    if checked:
        answer_data = st.session_state.answers[idx]
        if answer_data["correct"]:
            st.markdown(f"""
            <div class="result-correct">
                <div style="font-weight: 600; color: #059669; margin-bottom: 0.35rem;">✅ Correct!</div>
            </div>
            <div class="explanation-box">
                💡 <strong>Explanation:</strong> {q['explanation']}
            </div>
            """, unsafe_allow_html=True)
        else:
            correct_text = q["options"][q["correct"]]
            st.markdown(f"""
            <div class="result-incorrect">
                <div style="font-weight: 600; color: #DC2626; margin-bottom: 0.35rem;">❌ Incorrect</div>
                <div style="color: #7F1D1D; font-size: 0.9rem;">
                    Correct answer: <strong>{correct_text}</strong>
                </div>
            </div>
            <div class="explanation-box">
                💡 <strong>Explanation:</strong> {q['explanation']}
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────
# Test Mode
# ─────────────────────────────────────────────────
def render_test_quiz():
    """Render quiz in test mode — all questions, submit at end."""
    week_key = st.session_state.selected_week
    week_data = QUIZ_DATA[week_key]
    questions = st.session_state.shuffled_questions
    total = len(questions)

    if st.session_state.show_results:
        render_results()
        return

    # Header
    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
        <div>
            <span style="font-size: 0.78rem; font-weight: 600; color: #8E94B2; text-transform: uppercase; letter-spacing: 0.06em;">
                {week_key} · Test Mode
            </span>
            <div style="font-size: 1.25rem; font-weight: 700; color: #1A1D2E; margin-top: 0.15rem;">
                {week_data['title']}
            </div>
        </div>
        <div>
            <span class="badge badge-neutral">🏆 {total} Questions</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Answer tracker
    answered = sum(1 for i in range(total) if st.session_state.answers.get(i, {}).get("selected") is not None)
    st.progress(answered / total, text=f"{answered}/{total} answered")

    st.markdown("")

    # All questions
    for i, q in enumerate(questions):
        q_key = f"test_{week_key}_{i}"

        st.markdown(f"""
        <div class="question-card">
            <div style="display: flex; align-items: flex-start;">
                <div class="question-number">{i + 1}</div>
                <div class="question-text">{q['question']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Get previously selected value
        prev_selected = st.session_state.answers.get(i, {}).get("selected_index", None)

        selected = st.radio(
            f"Q{i+1}",
            options=q["options"],
            key=q_key,
            index=prev_selected,
            label_visibility="collapsed"
        )

        if selected is not None:
            selected_index = q["options"].index(selected)
            is_correct = (selected_index == q["correct"])
            st.session_state.answers[i] = {
                "selected": selected,
                "selected_index": selected_index,
                "correct": is_correct,
                "checked": False
            }

        st.markdown("")

    # Submit button
    st.markdown("<br>", unsafe_allow_html=True)

    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("📝 Submit Test", key="submit_test", use_container_width=True):
            unanswered = [i + 1 for i in range(total) if st.session_state.answers.get(i, {}).get("selected") is None]
            if unanswered:
                st.warning(f"⚠️ You haven't answered question(s): {', '.join(map(str, unanswered))}")
            else:
                st.session_state.show_results = True
                correct_count = sum(1 for a in st.session_state.answers.values() if a.get("correct", False))
                pct = int((correct_count / total) * 100)
                if week_key not in st.session_state.quiz_history:
                    st.session_state.quiz_history[week_key] = []
                st.session_state.quiz_history[week_key].append(pct)
                st.rerun()


# ─────────────────────────────────────────────────
# Results Page
# ─────────────────────────────────────────────────
def render_results():
    """Render quiz results."""
    week_key = st.session_state.selected_week
    is_mixed = (week_key == "Mixed Quiz")
    questions = st.session_state.shuffled_questions
    total = len(questions)

    correct_count = sum(1 for a in st.session_state.answers.values() if a.get("correct", False))
    percentage = int((correct_count / total) * 100)
    score_class = get_score_class(percentage)
    emoji = get_grade_emoji(percentage)
    message = get_grade_message(percentage)

    # Score Display
    st.markdown(f"""
    <div class="score-display">
        <div class="score-circle {score_class}">
            {percentage}%
        </div>
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{emoji}</div>
        <div style="font-size: 1.3rem; font-weight: 700; color: #1A1D2E; margin-bottom: 0.25rem;">
            {correct_count} out of {total} correct
        </div>
        <div style="font-size: 0.95rem; color: #5A607F;">
            {message}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Action buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Go Home", key="results_home", use_container_width=True):
            st.session_state.current_page = "home"
            reset_quiz()
            st.rerun()
    with col2:
        if is_mixed:
            if st.button("🔀 New Mixed Quiz", key="results_retry", use_container_width=True):
                st.session_state.current_page = "mixed"
                reset_quiz()
                st.rerun()
        else:
            if st.button("🔄 Retry Quiz", key="results_retry", use_container_width=True):
                mode = st.session_state.quiz_mode
                start_quiz(week_key, mode)
                st.rerun()
    with col3:
        if st.button("📊 Dashboard", key="results_dash", use_container_width=True):
            st.session_state.current_page = "dashboard"
            reset_quiz()
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📋 Detailed Review")
    st.markdown("")

    for i, q in enumerate(questions):
        answer_data = st.session_state.answers.get(i, {})
        is_correct = answer_data.get("correct", False)
        selected = answer_data.get("selected", "Not answered")

        status_icon = "✅" if is_correct else "❌"

        # Show source week for mixed quiz
        source_label = ""
        if is_mixed and "source_week" in q:
            source_label = f" [{q['source_week']}]"

        with st.expander(f"{status_icon} Question {i + 1}{source_label}: {'Correct' if is_correct else 'Incorrect'}"):
            if is_mixed and "source_week" in q:
                st.caption(f"📌 Source: {q['source_week']}")
            st.markdown(f"**{q['question']}**")
            st.markdown("")

            for j, option in enumerate(q["options"]):
                if j == q["correct"] and is_correct:
                    st.markdown(f"✅ **{option}** ← Your answer (Correct)")
                elif j == q["correct"] and not is_correct:
                    st.markdown(f"✅ **{option}** ← Correct answer")
                elif option == selected and not is_correct:
                    st.markdown(f"❌ ~~{option}~~ ← Your answer")
                else:
                    st.markdown(f"○ {option}")

            st.markdown("")
            st.info(f"💡 **Explanation:** {q['explanation']}")


# ─────────────────────────────────────────────────
# Dashboard Page
# ─────────────────────────────────────────────────
def render_dashboard():
    """Render the performance dashboard."""
    st.markdown("""
    <div class="hero-banner" style="padding: 2rem;">
        <h1>📊 Performance Dashboard</h1>
        <p>Track your progress across all weeks</p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.quiz_history:
        st.markdown("""
        <div class="stat-card" style="text-align: center; padding: 3rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📝</div>
            <div style="font-size: 1.15rem; font-weight: 600; color: #1A1D2E; margin-bottom: 0.5rem;">No quizzes taken yet</div>
            <div style="font-size: 0.9rem; color: #5A607F;">Complete a quiz to see your performance here!</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Overall Stats
    total_attempts = sum(len(v) for v in st.session_state.quiz_history.values())
    all_scores = [s for scores in st.session_state.quiz_history.values() for s in scores]
    overall_avg = sum(all_scores) / len(all_scores)
    best_overall = max(all_scores)
    weeks_attempted = len(st.session_state.quiz_history)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{total_attempts}</div>
            <div class="stat-label">Total Attempts</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{overall_avg:.0f}%</div>
            <div class="stat-label">Average Score</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{best_overall}%</div>
            <div class="stat-label">Best Score</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{weeks_attempted}/{len(QUIZ_DATA)}</div>
            <div class="stat-label">Weeks Done</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📈 Week-by-Week Performance")
    st.markdown("")

    # Performance table
    for week_key, week_data in QUIZ_DATA.items():
        if week_key in st.session_state.quiz_history:
            scores = st.session_state.quiz_history[week_key]
            best = max(scores)
            latest = scores[-1]
            attempts = len(scores)
            score_class = get_score_class(best)
            emoji = get_grade_emoji(best)

            col_a, col_b, col_c, col_d, col_e = st.columns([3, 1.5, 1.5, 1.5, 1.5])
            with col_a:
                st.markdown(f"**{week_data['icon']} {week_key}**")
                st.caption(week_data['title'])
            with col_b:
                st.metric("Best", f"{best}%")
            with col_c:
                st.metric("Latest", f"{latest}%")
            with col_d:
                st.metric("Attempts", f"{attempts}")
            with col_e:
                st.markdown(f"<div style='font-size: 2rem; text-align: center; padding-top: 0.5rem;'>{emoji}</div>", unsafe_allow_html=True)

            st.markdown("---")
        else:
            col_a, col_b = st.columns([3, 3])
            with col_a:
                st.markdown(f"**{week_data['icon']} {week_key}**")
                st.caption(week_data['title'])
            with col_b:
                st.markdown(f'<span class="badge badge-neutral" style="margin-top: 0.5rem;">Not attempted</span>', unsafe_allow_html=True)
            st.markdown("---")


# ─────────────────────────────────────────────────
# Mixed Quiz Setup Page
# ─────────────────────────────────────────────────
def render_mixed_quiz_setup():
    """Render the mixed quiz configuration page."""
    st.markdown("""
    <div class="hero-banner" style="padding: 2rem;">
        <h1>🔀 Mixed Quiz</h1>
        <p>Challenge yourself with shuffled questions from multiple weeks</p>
    </div>
    """, unsafe_allow_html=True)

    total_q = sum(len(w["questions"]) for w in QUIZ_DATA.values())

    # Stats row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{len(QUIZ_DATA)}</div>
            <div class="stat-label">Weeks Available</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{total_q}</div>
            <div class="stat-label">Total Questions</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        if "Mixed Quiz" in st.session_state.quiz_history:
            mbest = max(st.session_state.quiz_history["Mixed Quiz"])
            mbest_display = f"{mbest}%"
        else:
            mbest_display = "—"
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{mbest_display}</div>
            <div class="stat-label">Best Score</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### ⚙️ Configure Your Mixed Quiz")
    st.markdown("")

    # Week selection
    st.markdown("**Select weeks to include:**")
    week_keys = list(QUIZ_DATA.keys())

    col_sel1, col_sel2 = st.columns(2)
    with col_sel1:
        if st.button("✅ Select All", key="select_all_weeks", use_container_width=True):
            st.session_state.mixed_selected_weeks = week_keys.copy()
            st.rerun()
    with col_sel2:
        if st.button("❎ Deselect All", key="deselect_all_weeks", use_container_width=True):
            st.session_state.mixed_selected_weeks = []
            st.rerun()

    # Initialize selected weeks if not set
    if "mixed_selected_weeks" not in st.session_state:
        st.session_state.mixed_selected_weeks = week_keys.copy()

    # Week checkboxes in columns
    cols = st.columns(3)
    selected_weeks = []
    for i, week_key in enumerate(week_keys):
        week_data = QUIZ_DATA[week_key]
        col_idx = i % 3
        with cols[col_idx]:
            checked = week_key in st.session_state.mixed_selected_weeks
            if st.checkbox(
                f"{week_data['icon']} {week_key} ({len(week_data['questions'])}Q)",
                value=checked,
                key=f"mixed_week_{week_key}"
            ):
                selected_weeks.append(week_key)

    # Update selected weeks in session state
    st.session_state.mixed_selected_weeks = selected_weeks

    # Calculate available questions
    available_q = sum(len(QUIZ_DATA[w]["questions"]) for w in selected_weeks) if selected_weeks else 0

    st.markdown("<br>", unsafe_allow_html=True)

    # Number of questions slider
    st.markdown(f"**Number of questions** (up to {available_q} available):")
    if available_q > 0:
        default_num = min(20, available_q)
        num_questions = st.slider(
            "Number of questions",
            min_value=5,
            max_value=available_q,
            value=default_num,
            step=5,
            label_visibility="collapsed"
        )
    else:
        num_questions = 0
        st.warning("⚠️ Please select at least one week.")

    st.markdown("<br>", unsafe_allow_html=True)

    # Summary & Start
    if selected_weeks and num_questions > 0:
        st.markdown(f"""
        <div class="stat-card" style="text-align: left; padding: 1.5rem;">
            <div style="font-size: 1.1rem; font-weight: 700; color: #1A1D2E; margin-bottom: 0.5rem;">📋 Quiz Summary</div>
            <div style="font-size: 0.9rem; color: #5A607F; line-height: 1.8;">
                • <strong>{num_questions}</strong> questions from <strong>{len(selected_weeks)}</strong> week(s)<br>
                • Questions will be <strong>shuffled randomly</strong><br>
                • Results shown after submitting all answers<br>
                • Each question shows its source week in review
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col_l, col_c, col_r = st.columns([1, 2, 1])
        with col_c:
            if st.button("🚀 Start Mixed Quiz", key="launch_mixed", use_container_width=True):
                start_mixed_quiz(num_questions, selected_weeks)
                st.rerun()


# ─────────────────────────────────────────────────
# Main Router
# ─────────────────────────────────────────────────
def main():
    """Main application entry point and router."""
    render_sidebar()

    page = st.session_state.current_page

    if page == "home":
        render_home()
    elif page == "week_detail":
        render_week_detail()
    elif page == "quiz":
        if st.session_state.quiz_mode == "practice":
            render_practice_quiz()
        elif st.session_state.quiz_mode == "test":
            render_test_quiz()
    elif page == "mixed":
        render_mixed_quiz_setup()
    elif page == "dashboard":
        render_dashboard()
    else:
        render_home()


if __name__ == "__main__":
    main()
