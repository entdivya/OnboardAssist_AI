from llm_factory import llm


def generate_response(
    question,
    context,
    history
):
    """
    Generate a response using:
    1. Current Question
    2. Retrieved RAG Context
    3. Previous Employee Conversations
    """

    # ---------------------------------------
    # Convert previous conversations to text
    # ---------------------------------------

    if history:

        history_text = "\n".join(
            [
                f"- {question} ({department})"
                for question, department, timestamp in history
            ]
        )

    else:

        history_text = "No previous conversations."

    # ---------------------------------------
    # Prompt
    # ---------------------------------------

    prompt = f"""
You are OnboardAssist_AI, an Enterprise New Joinee Onboarding Assistant.

Your responsibilities are:
- Help employees during onboarding.
- Use previous conversations to maintain continuity.
- Use company documents as the primary source of truth.
- Never invent company policies.

==========================================================
EMPLOYEE PREVIOUS CONVERSATIONS
==========================================================

{history_text}

==========================================================
CURRENT QUESTION
==========================================================

{question}

==========================================================
RELEVANT COMPANY DOCUMENTS
==========================================================

{context}

==========================================================
INSTRUCTIONS
==========================================================

1. First understand the employee's current question.

2. Review the previous conversations to understand what has already been discussed.

3. Do NOT repeat previous explanations unless they are directly relevant.

4. If the employee refers to something discussed earlier (for example "that", "it", "previous step"), use the conversation history to understand the reference.

5. Use ONLY the retrieved company documents to answer policy or process questions.

6. If the answer is not available in the retrieved documents, clearly say:
"I could not find this information in the onboarding documents."

7. Keep the answer concise and professional.

Respond using the following format:

**Clear Answer**

**Important Points**

**Next Steps**
"""

    response = llm.invoke(prompt)

    return response.content