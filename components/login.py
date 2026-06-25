import streamlit as st
from agents.memory_agent import initialize_employee_tasks



def render_login():

    st.title("🤖 OnboardAssist_AI")

    st.subheader("Enterprise New Joinee Assistant")

    st.write("")

    st.info(
        """
Welcome!

I can help you with:

• HR Policies

• IT Setup

• Compliance Policies

Please enter your Employee ID to continue.
"""
    )

    employee_id = st.text_input(
        "Employee ID",
        placeholder="Example: EMP1001"
    )

    if st.button("Continue", use_container_width=True):

        if employee_id.strip():

            st.session_state.employee_id = employee_id.strip()

            st.session_state.logged_in = True

            st.session_state.employee_id = employee_id.strip()

            st.session_state.logged_in = True

            initialize_employee_tasks(
            employee_id.strip()
                )

            st.rerun()

        else:

            st.warning("Please enter Employee ID.")