from fastapi import FastAPI
import requests
from transformers import pipeline
import os

app = FastAPI()

# ✅ Load Hugging Face API token from environment
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print("Token in ENV:", token)

# ✅ Load emotion classifier
classifier = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    top_k=1,
    token=token
)

# ✅ External service URLs (local fallback for testing)
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8001")
ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL", "http://localhost:8002")

def detect_intent(user_input: str) -> str:
    try:
        result = classifier(user_input)[0][0]
        print("Classifier result:", result)

        label = result["label"].lower()
        print("Detected label:", label)

        # ✅ Intent classification
        if any(x in label for x in ["joy", "admiration", "excitement", "gratitude", "neutral", "desire", "curiosity", "optimism", "love"]):
            return "product"
        elif any(x in label for x in ["fear", "anger", "disappointment", "remorse", "confusion", "nervousness"]):
            return "order"
        else:
            return "unknown"
    except Exception as e:
        print("Intent detection error:", e)
        return "unknown"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat_handler(payload: dict):
    message = payload.get("message", "")
    intent = detect_intent(message)

    try:
        if intent == "product":
            response = requests.post(f"{PRODUCT_SERVICE_URL}/product-query", json={"query": message})
        elif intent == "order":
            response = requests.post(f"{ORDER_SERVICE_URL}/order-query", json={"query": message})
        else:
            return {"response": "I'm not sure what you're asking. Please mention a product or your customer ID."}

        return {"response": response.json()["response"]}
    except Exception as e:
        print("Error contacting microservice:", e)
        return {"response": "Service error. Please try again later."}
