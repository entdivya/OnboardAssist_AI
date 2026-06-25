from llm_factory import llm


def classify_department(question):

    prompt = f"""
    You are an onboarding supervisor.

    Classify the employee question into one of these departments:

    HR
    IT
    Compliance

    Return ONLY the department name.

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content.strip()