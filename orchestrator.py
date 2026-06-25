from agents.supervisor_agent import classify_department
from agents.retriever_agent import retrieve_context
from agents.response_agent import generate_response
from agents.recommendation_agent import generate_recommendations

from agents.memory_agent import (
    save_conversation,
    get_previous_conversations
)


def process_employee_query(
    employee_id,
    employee_name,
    question
):

    # Load History
    history = get_previous_conversations(
        employee_id
    )

    # Department Classification
    department = classify_department(
        question
    )

    # Retrieve Context
    context = retrieve_context(
        question,
        department
    )

    # Generate Answer
    answer = generate_response(
        question,
        context
    )

    # Recommendations
    recommendations = generate_recommendations(
        department
    )

    # Save Conversation
    save_conversation(
        employee_id,
        employee_name,
        question,
        department
    )

    return {
        "history": history,
        "department": department,
        "answer": answer,
        "recommendations": recommendations
    }