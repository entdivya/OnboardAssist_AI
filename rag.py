from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import FAISS

import os


def create_vector_store():

    documents = []

    folders = [
        "documents/hr",
        "documents/it",
        "documents/compliance"
    ]

    for folder in folders:

        for file in os.listdir(folder):

            if file.endswith(".pdf"):

                pdf_path = os.path.join(
                    folder,
                    file
                )

                loader = PyPDFLoader(
                    pdf_path
                )

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

    embeddings = HuggingFaceEmbeddings(
        model_name=
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(
        "vector_store"
    )

    return vector_store