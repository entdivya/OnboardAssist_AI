import streamlit as st

from agents.memory_agent import (
    get_pending_tasks,
    get_completed_tasks,
    complete_task
)


def render_dashboard(employee_id):

    # ---------------------------------------
    # Get Tasks
    # ---------------------------------------

    pending_tasks = get_pending_tasks(employee_id)
    completed_tasks = get_completed_tasks(employee_id)

    pending = len(pending_tasks)
    completed = len(completed_tasks)

    total = pending + completed

    progress = 0

    if total > 0:
        progress = completed / total

    # ---------------------------------------
    # Dashboard Header
    # ---------------------------------------

    st.subheader("📊 Onboarding Progress")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Pending",
            pending
        )

    with col2:
        st.metric(
            "Completed",
            completed
        )

    with col3:
        st.metric(
            "Progress",
            f"{int(progress * 100)}%"
        )

    st.progress(progress)

    st.divider()

    # ---------------------------------------
    # Pending & Completed Tasks
    # ---------------------------------------

    left, right = st.columns(2)

    # ---------------------------------------
    # Pending Tasks
    # ---------------------------------------

    with left:

        st.markdown("### 🎯 Your Next Steps")

        if pending_tasks:

            for task in pending_tasks:

                task_name = task[0]

                if st.checkbox(
                    task_name,
                    key=f"{employee_id}_{task_name}"
                ):

                    complete_task(
                        employee_id,
                        task_name
                    )

                    st.success(f"Completed: {task_name}")

                    st.rerun()

        else:

            st.success("🎉 No pending tasks!")

    # ---------------------------------------
    # Completed Tasks
    # ---------------------------------------

    with right:

        st.markdown("### ✔ Completed")

        if completed_tasks:

            for task in completed_tasks:

                st.success(f"✅ {task[0]}")

        else:

            st.info("No completed tasks yet.")