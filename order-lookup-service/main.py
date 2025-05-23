from fastapi import FastAPI
import requests
import re

app = FastAPI()

MOCK_API_URL = "http://localhost:8003/data"

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/order-query")
async def order_query(payload: dict):
    user_input = payload.get("query", "").lower()

    customer_id = extract_customer_id(user_input)

    if not customer_id:
        return {"response": "Please provide your Customer ID."}

    response = requests.get(f"{MOCK_API_URL}/customer/{customer_id}")
    data = response.json()

    if "error" in data:
        return {"response": data["error"]}

    if not data:
        return {"response": "No orders found for that Customer ID."}

    # Get the latest order by Order_Date
    latest_order = sorted(data, key=lambda x: x.get("Order_Date", ""), reverse=True)[0]

    return {
        "response": (
            f"Your most recent order was '{latest_order['Product']}' from the '{latest_order['Product_Category']}' "
            f"category on {latest_order['Order_Date']}.\n"
            f"Total: ${latest_order['Sales']}, Shipping: ${latest_order['Shipping_Cost']}, "
            f"Priority: {latest_order['Order_Priority']}, Paid via: {latest_order['Payment_method']}."
        )
    }

def extract_customer_id(text: str):
    match = re.search(r"\b\d{5}\b", text)
    return int(match.group()) if match else None
