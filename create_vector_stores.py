from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import os


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def build_store(pdf_folder, save_path):

    documents = []

    for file in os.listdir(pdf_folder):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(
                pdf_folder,
                file
            )

            loader = PyPDFLoader(pdf_path)

            documents.extend(
                loader.load()
            )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        documents
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(
        save_path
    )

    print(f"Created: {save_path}")


build_store(
    "documents/hr",
    "vector_store/hr"
)

build_store(
    "documents/it",
    "vector_store/it"
)

build_store(
    "documents/compliance",
    "vector_store/compliance"
)

print("All vector stores created successfully!")