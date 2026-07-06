from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
from dotenv import load_dotenv
from litellm import completion
from pydantic import BaseModel

load_dotenv(override=True)
model="groq/openai/gpt-oss-120b"
db_path="cv_chromadb"
collection_name="cv_text_embeddings"
embedding_model="all-MiniLM-L6-v2"

chroma = PersistentClient(path=db_path)
collection = chroma.get_collection(collection_name)
embedder=SentenceTransformer(embedding_model)


SYSTEM_PROMPT = """
You are an assistant that analyzes Ahmet's CV. You must provide answers when the user asks questions about Ahmet's resume. 
Do NOT provide any extra information outside the context, and do NOT delete any information.
If you dont know about the question, politely say you don't know.

Context from CV:
{context}
"""

def fetch_context(question, k=5):
    vector = embedder.encode([question]).tolist()
    results = collection.query(query_embeddings=vector,n_results=k)
    return "\n\n".join(results["documents"][0])

def make_rag_messages(question,context,history):
    system_prompt=SYSTEM_PROMPT.format(context=context)
    messages=([{"role":"system","content":system_prompt}]+history+[{"role":"user","content":question}])
    return messages

def answer(question,history):
    context=fetch_context(question)
    messages=make_rag_messages(question,context,history)
    response=completion(model=model,messages=messages)
    return response.choices[0].message.content    
    
    
    