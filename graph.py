from langgraph.graph import StateGraph, END

from state import OnboardingState

from agents.memory_agent import (
    get_previous_conversations,
    save_conversation,
    save_tasks
)

from agents.supervisor_agent import (
    classify_department
)

from agents.retriever_agent import (
    retrieve_context
)

from agents.response_agent import (
    generate_response
)

from agents.recommendation_agent import (
    generate_recommendations
)


# ==========================================
# Memory Node
# ==========================================

def memory_node(state):

    history = get_previous_conversations(
        state["employee_id"]
    )

    state["history"] = history

    return state


# ==========================================
# Supervisor Node
# ==========================================

def supervisor_node(state):

    department = classify_department(
        state["question"]
    )

    state["department"] = department

    return state


# ==========================================
# Retriever Node
# ==========================================

def retriever_node(state):

    context = retrieve_context(
        state["question"],
        state["department"]
    )

    state["context"] = context

    return state


# ==========================================
# Response Node
# ==========================================

def response_node(state):

    answer = generate_response(
        state["question"],
        state["context"],
        state["history"]
    )

    state["answer"] = answer

    return state


# ==========================================
# Recommendation Node
# ==========================================

def recommendation_node(state):

    recommendations = generate_recommendations(
        state["department"]
    )

    state["recommendations"] = recommendations

    return state


# ==========================================
# Task Node
# ==========================================

def task_node(state):

    save_tasks(
        state["employee_id"],
        state["recommendations"]
    )

    return state


# ==========================================
# Save Memory Node
# ==========================================

def save_memory_node(state):

    save_conversation(
        state["employee_id"],
        state["employee_name"],
        state["question"],
        state["department"]
    )

    return state


# ==========================================
# Build Workflow
# ==========================================

workflow = StateGraph(OnboardingState)

workflow.add_node("memory", memory_node)
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("retriever", retriever_node)
workflow.add_node("response", response_node)
workflow.add_node("recommendation", recommendation_node)
workflow.add_node("task", task_node)
workflow.add_node("save_memory", save_memory_node)

# ==========================================
# Graph Flow
# ==========================================

workflow.set_entry_point("memory")

workflow.add_edge("memory", "supervisor")
workflow.add_edge("supervisor", "retriever")
workflow.add_edge("retriever", "response")
workflow.add_edge("response", "recommendation")
workflow.add_edge("recommendation", "task")
workflow.add_edge("task", "save_memory")
workflow.add_edge("save_memory", END)

# ==========================================
# Compile Graph
# ==========================================

graph = workflow.compile()