from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(override=True)

pdf_path = Path(__file__).parent.parent / "cv.pdf"
db_path = Path(__file__).parent.parent / "langchain_db"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

loader = PyPDFLoader(str(pdf_path))
documents = loader.load()
print(documents)

def create_chunks():
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=75)
    chunks = splitter.split_documents(documents)
    return chunks

def create_embeddings(chunks):
    if os.path.exists(db_path):
        Chroma(persist_directory=str(db_path), embedding_function=embeddings).delete_collection()

    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=str(db_path))
    return vectorstore    

if __name__ == "__main__":
    chunks = create_chunks()
    vectorstore = create_embeddings(chunks)
    print("Ingestion complete")    