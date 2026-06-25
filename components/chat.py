import streamlit as st

from graph import graph


def render_chat(employee_id):

    # -----------------------------
    # Session Chat History
    # -----------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.subheader("💬 Ask OnboardAssist_AI")

    question = st.chat_input(
        "Ask your onboarding question..."
    )

    if question:

        if not employee_id:

            st.warning("Please enter your Employee ID.")

            return

        # Show User Message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        initial_state = {

            "employee_id": employee_id,

            "employee_name": "",

            "question": question,

            "history": [],

            "department": "",

            "context": "",

            "answer": "",

            "recommendations": []

        }

        with st.spinner("Thinking..."):

            result = graph.invoke(
                initial_state
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result["answer"]
            }
        )

    # -----------------------------
    # Display Chat
    # -----------------------------

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(
                message["content"]
            )