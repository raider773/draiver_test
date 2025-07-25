from sentence_transformers import SentenceTransformer
import chromadb

def search_similar_docs(query: str, top_k: int = 5):
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="france_tourism")

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = embedding_model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]

def get_france_weather(date: str) -> str:
    return f"In {date}, the weather is expected to be sunny with temperatures around 28–35°C."


def make_reservation(activity: str, date: str) -> str:
    return f"Reservation confirmed for '{activity}' on {date}."