# test_complete_task.py

from agents.memory_agent import (
    complete_task,
    get_pending_tasks,
    get_completed_tasks
)

complete_task(
    "EMP1001",
    "Configure Outlook Email"
)

print("\nCompleted Tasks:\n")

for task in get_completed_tasks("EMP1001"):
    print(task[0])

print("\nPending Tasks:\n")

for task in get_pending_tasks("EMP1001"):
    print(task[0])