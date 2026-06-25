from typing import TypedDict


class OnboardingState(TypedDict):

    employee_id: str

    employee_name: str

    question: str

    history: list

    department: str

    context: str

    answer: str

    recommendations: list