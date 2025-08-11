import requests
import chromadb
from sentence_transformers import SentenceTransformer
import re
from chromadb import Documents, EmbeddingFunction, Embeddings
import json
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"
CHROMA_DB_DIR = "./chroma_wwi"
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50

def get_wiki_titles(query):
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 20 
    }
    resp = requests.get(WIKI_API_URL, params=params)
    resp.raise_for_status()
    return [item["title"] for item in resp.json()["query"]["search"]]


def get_wiki_text(title):
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": True,
        "titles": title,
        "format": "json"
    }
    resp = requests.get(WIKI_API_URL, params=params)
    resp.raise_for_status()
    pages = resp.json()["query"]["pages"]
    return list(pages.values())[0].get("extract", "")



def clean_text(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks


def load_data_in_chroma():
    world_war_1_data = get_wiki_titles("World War 1")
    great_war = get_wiki_titles("The Great War")
    time_period = get_wiki_titles("1914-1918")
    first_world_war = get_wiki_titles("First World War")

    titles = set()
    
    for title in world_war_1_data:
        titles.add(title)
    for title in great_war:
        titles.add(title)
    for title in time_period:
        titles.add(title)
    for title in first_world_war:
        titles.add(title)

    print(f"Found {len(titles)} articles")
    doc_id = 0

    for title in titles:
        print(f"Processing: {title}")
        text = get_wiki_text(title)
        text = clean_text(text)
        chunks = chunk_text(text)
        for chunk in chunks:
            doc_id += 1
            collection.add(
                ids=[str(doc_id)],
                documents=[chunk],
                metadatas=[{"title": title}]
            )

class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, text: Documents) -> Embeddings:
        return model.encode(text).tolist()

if __name__ == "__main__":
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

    collection = client.get_or_create_collection(name="ww1", embedding_function=MyEmbeddingFunction())

    load_data_in_chroma()

    query = "List the important events from World War 1"
    results = collection.query(query_texts=[query],n_results=3)
    output_file_path = "chroma_query_results.json"

    with open(output_file_path, 'w') as f:
        json.dump(results, f, indent=4)
    print(f"Query results saved to {output_file_path}")

