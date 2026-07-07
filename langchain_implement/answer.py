from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv(override=True)


db_path = Path(__file__).parent.parent / "langchain_db"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
vectorstore = Chroma(persist_directory=str(db_path), embedding_function=embeddings)
retriever = vectorstore.as_retriever()

SYSTEM_PROMPT = """
You are an assistant that analyzes Ahmet's CV. You must provide answers when the user asks questions about Ahmet's resume. 
Do NOT provide any extra information outside the context, and do NOT delete any information.
If you dont know about the question, politely say you don't know.

Context from CV:
{context}
"""

def answer_cv_question(question: str, history: list[dict] = []):
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    system_message = SystemMessage(content=SYSTEM_PROMPT.format(context=context))
    messages=[system_message]+history+[HumanMessage(content=question)]
    response=llm.invoke(messages)
    return response.content
