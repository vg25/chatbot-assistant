from fastapi import FastAPI
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

app = FastAPI()

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load product data
df = pd.read_csv("Product_Information_Dataset.csv")
df["text"] = df["title"].fillna('') + " - " + df["description"].fillna('')


# Generate embeddings
embeddings = model.encode(df["text"].tolist(), show_progress_bar=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/product-query")
async def product_query(payload: dict):
    query = payload.get("query", "")
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k=3)

    results = []
    for idx in I[0]:
        product = df.iloc[idx]
        results.append({
            "title": product["title"],
            "price": product.get("price", ""),
            "rating": product.get("average_rating", ""),
            "description": product.get("description", "")
        })

    response = "Here are some relevant products:\n"
    for prod in results:
        response += f"- {prod['title']} (${prod['price']}) – {prod['rating']} stars\n"
    return {"response": response}
