import streamlit as st

from agents.memory_agent import initialize_db

from components.login import render_login
from components.sidebar import render_sidebar
from components.chat import render_chat
from components.dashboard import render_dashboard

st.set_page_config(
    page_title="OnboardAssist_AI",
    page_icon="🤖",
    layout="wide"
)

initialize_db()
# =====================================================
# Session State Initialization
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "employee_id" not in st.session_state:
    st.session_state.employee_id = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# Login Page
# =====================================================

if not st.session_state.logged_in:

    render_login()

# =====================================================
# Main Application
# =====================================================

else:

    employee_id = st.session_state.employee_id

    # Sidebar
    render_sidebar(employee_id)

    # Header
    st.title("🤖 OnboardAssist_AI")
    st.caption("Your Intelligent Onboarding Assistant")

    st.success(f"👋 Welcome back, {employee_id}")

    st.divider()

    # -----------------------------
    # Dashboard FIRST
    # -----------------------------

    render_dashboard(employee_id)

    st.divider()

    # -----------------------------
    # Chat SECOND
    # -----------------------------

    render_chat(employee_id)