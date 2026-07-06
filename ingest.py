from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
from dotenv import load_dotenv
from litellm import completion


#constants
load_dotenv(override=True)
pdf= "cv.pdf"
embedding_model="all-MiniLM-L6-v2"
collection_name="cv_text_embeddings"
db_path = "cv_chromadb"
model="groq/openai/gpt-oss-120b"

#reading cv.pdf
reader=PdfReader(pdf)
text="\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

#creating chunks 
def create_chunk(text, chunk_size=500, overlap=75):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks

#creating embeddings and saving to chromadbs
def create_embeddings(chunks):
    embedder=SentenceTransformer(embedding_model)
    vectors = embedder.encode(chunks).tolist()
    
    chroma=PersistentClient(path=db_path)
    if collection_name in [c.name for c in chroma.list_collections()]:
        chroma.delete_collection(collection_name)
    
    collection=chroma.create_collection(name=collection_name)
    collection.add(documents=chunks,embeddings=vectors,ids=[str(i) for i in range(len(chunks))])
    print(f"Created {collection.count()} embeddings")

if __name__ == "__main__":
    chunks = create_chunk(text)
    create_embeddings(chunks)
    