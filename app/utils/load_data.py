import os
from typing import List
import tiktoken
import chromadb
from sentence_transformers import SentenceTransformer
from app.conf.settings import Settings

settings = Settings()

CHUNK_SIZE = settings.chunk_size  
CHUNK_OVERLAP = settings.chunk_overlap  
encoding = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str) -> int:
    return len(encoding.encode(text))

def split_text_to_chunks(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        current_text = " ".join(current_chunk)
        if count_tokens(current_text) >= chunk_size:
            chunks.append(current_text)
            current_chunk = current_chunk[-overlap:]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def load_and_chunk(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return split_text_to_chunks(text)

def main():
    FILE_PATH = "french_tour_guide.txt"  
    DB_PATH = "./chroma_db"

    chunks = load_and_chunk(FILE_PATH)

    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection(name="france_tourism")

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embedding_model.encode(chunks).tolist()

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"doc_{i}" for i in range(len(chunks))]
    )

    print(f"Loaded {len(chunks)} chunks into vector DB at '{DB_PATH}'")

if __name__ == "__main__":
    main()

