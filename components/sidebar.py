import streamlit as st

from agents.memory_agent import (
    get_pending_tasks,
    get_completed_tasks
)


def render_sidebar(employee_id):

    with st.sidebar:

        st.title("🤖 OnboardAssist_AI")

        st.caption("Enterprise New Joinee Assistant")

        st.divider()

        st.subheader("Employee")

        if employee_id:

            st.success(employee_id)

            pending = len(
                get_pending_tasks(employee_id)
            )

            completed = len(
                get_completed_tasks(employee_id)
            )

            total = pending + completed

            progress = 0

            if total > 0:
                progress = completed / total

            st.metric(
                "Completed",
                completed
            )

            st.metric(
                "Pending",
                pending
            )

            st.progress(progress)

        else:

            st.info("Enter Employee ID")