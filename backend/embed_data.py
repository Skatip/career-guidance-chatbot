
from backend.db_config import get_chroma_collection
from backend.utils import load_csv_data, clean_text
from models.embedder import get_embedder

def embed_dataset(file_path):
    collection = get_chroma_collection()
    embedder = get_embedder()
    data = load_csv_data(file_path)

    for item in data:
        content = clean_text(item["content"])
        embedding = embedder.encode(content).tolist()
        metadata = {"title": item["title"], "source": item["source"]}
        collection.add(documents=[content], embeddings=[embedding], metadatas=[metadata])

if __name__ == "__main__":
    embed_dataset("data/processed/career_guidance.csv")
