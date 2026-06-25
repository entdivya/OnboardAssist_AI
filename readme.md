# 🚀 OnboardAssist_AI

### Personalized Employee Onboarding Agentic RAG Assistant

OnboardAssist_AI is an AI-powered, memory-enabled onboarding assistant that helps new employees navigate their onboarding journey by answering questions from enterprise policy documents, remembering previous interactions, tracking onboarding progress, and providing personalized recommendations.

The application combines **Retrieval-Augmented Generation (RAG)**, **Agentic AI**, **LangGraph orchestration**, and **persistent memory** to deliver an intelligent and personalized onboarding experience.

---

# 🎯 Project Objective

New employees often struggle with:

* Understanding company policies
* Configuring VPN and email access
* Completing mandatory trainings
* Knowing onboarding procedures and next steps
* Finding information across multiple documents

OnboardAssist_AI simplifies the onboarding process by acting as an intelligent onboarding companion that provides contextual answers and personalized guidance throughout the employee's onboarding journey.

---

# 💡 Key Features

✅ Employee Identification using Employee Name and Employee ID

✅ Memory-enabled conversations

✅ Personalized onboarding recommendations

✅ Enterprise document search using RAG

✅ Onboarding progress tracking

✅ Multi-agent orchestration using LangGraph

✅ Context-aware responses from enterprise policies

✅ Persistent employee conversation history

✅ Streamlit-based interactive interface

---

# 🏗️ System Architecture

```text
Employee Name + Employee ID
              ↓
        Streamlit Interface
              ↓
         Profile Agent
              ↓
    Retrieve Employee Memory
              ↓
      Retriever Agent (RAG)
              ↓
      FAISS / Chroma Vector Store
              ↓
       Response Agent
              ↓
    Recommendation Agent
              ↓
      Save Memory & Progress
              ↓
              END
```

---

# 🧠 Agent Architecture

## 1. Profile Agent

Responsibilities:

* Capture Employee Name and Employee ID
* Retrieve previous conversations
* Retrieve onboarding progress
* Retrieve pending activities

---

## 2. Retriever Agent (RAG)

Responsibilities:

* Search enterprise policy documents
* Retrieve relevant document chunks
* Provide contextual information to the LLM

---

## 3. Response Agent

Responsibilities:

* Generate contextual answers using:

  * Employee Query
  * Retrieved Context
  * Previous Conversation History

---

## 4. Recommendation Agent

Responsibilities:

* Identify completed onboarding activities
* Identify pending activities
* Recommend personalized next steps

---

## 5. Memory Agent

Responsibilities:

* Store employee conversations
* Store onboarding progress
* Store completed and pending tasks
* Maintain employee-specific memory

---

# 📚 Knowledge Base Documents

The system can utilize enterprise onboarding documents such as:

* IT_Policy.pdf
* Employee_Handbook.pdf
* Leave_Policy.pdf
* Benefits_Policy.pdf
* Onboarding_Checklist.pdf

---

# 🔄 LangGraph Workflow

```text
START
   ↓
Profile Agent
   ↓
Retriever Agent
   ↓
Response Agent
   ↓
Recommendation Agent
   ↓
Memory Agent
   ↓
END
```

---

# 🗂️ Shared State

The application maintains the following state:

```python
{
    "employee_id": "",
    "employee_name": "",
    "question": "",
    "context": "",
    "response": "",
    "completed_tasks": [],
    "pending_tasks": [],
    "recommendations": ""
}
```

---

# 🛠️ Technology Stack

### Frontend

* Streamlit

### Frameworks

* LangChain
* LangGraph

### LLM

* Cohere Command-R
  or
* Groq LLaMA3

### RAG Components

* HuggingFace Embeddings
* FAISS / Chroma Vector Database

### Memory

* SQLite
* LangGraph State

### Document Processing

* PyPDF
* RecursiveCharacterTextSplitter

### Programming Language

* Python

---

# 📂 Project Structure

```text
OnboardAssist_AI/
│
├── app.py
├── graph.py
├── state.py
├── rag.py
├── llm_factory.py
├── config.py
│
├── agents/
│   ├── profile_agent.py
│   ├── retriever_agent.py
│   ├── response_agent.py
│   ├── recommendation_agent.py
│   └── memory_agent.py
│
├── documents/
│   ├── IT_Policy.pdf
│   ├── Employee_Handbook.pdf
│   ├── Leave_Policy.pdf
│   ├── Benefits_Policy.pdf
│   └── Onboarding_Checklist.pdf
│
├── vector_store/
├── memory/
│   └── onboarding_memory.sqlite
│
├── requirements.txt
└── README.md
```

---

# 🌟 Example User Journey

### First Login

Employee: Divya (EMP1001)

Question:

> How do I set up VPN?

Response:

* Install GlobalProtect VPN Client
* Configure company credentials
* Enable Multi-Factor Authentication

Recommended Next Steps:
✓ Configure Outlook
✓ Review IT Policy
✓ Complete Cyber Security Training

---

### Returning Employee

Employee: Divya (EMP1001)

Question:

> What should I do next?

Response:
Welcome back, Divya.

Completed:
✓ VPN Setup

Pending:
✓ Outlook Configuration
✓ Cyber Security Training
✓ Benefits Enrollment

---

# 🎯 Project Goals

This project demonstrates:

✓ Retrieval-Augmented Generation (RAG)

✓ Agentic AI

✓ Multi-Agent Systems

✓ LangGraph Orchestration

✓ Persistent Memory

✓ Personalized Recommendations

✓ Enterprise Workflow Automation

✓ End-to-End AI Application Development
