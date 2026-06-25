from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import FAISS


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def retrieve_context(
    question,
    department
):

    store_path = (
        f"vector_store/{department.lower()}"
    )

    vector_store = FAISS.load_local(
        store_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vector_store.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    return context