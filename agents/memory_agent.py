import sqlite3

DB_PATH = "memory/onboarding.db"


# ==========================================
# Initialize Database
# ==========================================

def initialize_db():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    # --------------------------------------
    # Conversations Table
    # --------------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT,
        employee_name TEXT,
        question TEXT,
        department TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # --------------------------------------
    # Tasks Table
    # --------------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT,
        task_name TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


# ==========================================
# Save Conversation
# ==========================================

def save_conversation(
    employee_id,
    employee_name,
    question,
    department
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations
        (
            employee_id,
            employee_name,
            question,
            department
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            employee_id,
            employee_name,
            question,
            department
        )
    )

    conn.commit()
    conn.close()


# ==========================================
# Get Previous Conversations
# ==========================================

def get_previous_conversations(
    employee_id
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT question,
               department,
               timestamp
        FROM conversations
        WHERE employee_id = ?
        ORDER BY timestamp DESC
        """,
        (employee_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================================
# Save Recommended Tasks
# ==========================================

def save_tasks(
    employee_id,
    tasks
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    for task in tasks:

        # Avoid duplicate pending tasks

        cursor.execute(
            """
            SELECT *
            FROM tasks
            WHERE employee_id = ?
            AND task_name = ?
            """,
            (
                employee_id,
                task
            )
        )

        existing = cursor.fetchone()

        if not existing:

            cursor.execute(
                """
                INSERT INTO tasks
                (
                    employee_id,
                    task_name,
                    status
                )
                VALUES (?, ?, ?)
                """,
                (
                    employee_id,
                    task,
                    "Pending"
                )
            )

    conn.commit()
    conn.close()


# ==========================================
# Get Pending Tasks
# ==========================================

def get_pending_tasks(
    employee_id
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT task_name
        FROM tasks
        WHERE employee_id = ?
        AND status = 'Pending'
        """,
        (employee_id,)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


# ==========================================
# Get Completed Tasks
# ==========================================

def get_completed_tasks(
    employee_id
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT task_name
        FROM tasks
        WHERE employee_id = ?
        AND status = 'Completed'
        """,
        (employee_id,)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


# ==========================================
# Mark Task Completed
# ==========================================

def complete_task(
    employee_id,
    task_name
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET status = 'Completed'
        WHERE employee_id = ?
        AND task_name = ?
        """,
        (
            employee_id,
            task_name
        )
    )

    conn.commit()
    conn.close()


# ==========================================
# Get All Tasks
# ==========================================

def get_all_tasks(
    employee_id
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT task_name,
               status
        FROM tasks
        WHERE employee_id = ?
        """,
        (employee_id,)
    )

    tasks = cursor.fetchall()

    conn.close()



    return tasks

# ==========================================
# Initialize Default Employee Tasks
# ==========================================

def initialize_employee_tasks(employee_id):
    """
    Creates the default onboarding checklist for a new employee.

    Since save_tasks() already checks for duplicate tasks,
    this function can safely be called every time the
    employee logs in.
    """

    default_tasks = [

        "Configure Outlook Email",

        "Enable Multi-Factor Authentication",

        "Review IT Security Policy"

    ]

    save_tasks(
        employee_id,
        default_tasks
    )
