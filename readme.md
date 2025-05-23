# 🎧 E-Commerce Expert Chatbot (Engineering Challenge 2025)

A modular chatbot built with FastAPI and microservices that can:
- 🛒 Recommend and search products using Retrieval-Augmented Generation (RAG)
- 📦 Answer order-related queries using a mock order API
- 🧠 Route user messages smartly based on intent

---

## 🧱 Architecture Overview

This chatbot follows a microservice architecture:

User Query → [chat-service] ──┬──> [product-search-service] → product CSV
└──> [order-lookup-service] → mock API → order CSV

Each service runs independently on a different port.

---

## 📁 Folder Structure

chatbot-assistant/
├── chat-service/
├── order-lookup-service/
├── product-search-service/
├── mock-api/
├── README.md
├── sample_questions.md

---

## 🚀 How to Run

You will run each service in its own terminal window.

### ✅ 1. `mock-api` (Port: 8003)

cd mock-api
venv\Scripts\activate.bat
uvicorn main:app --reload --port 8003


✅ 2. product-search-service (Port: 8001)
cd product-search-service
venv\Scripts\activate.bat
uvicorn main:app --reload --port 8001

✅ 3. order-lookup-service (Port: 8002)
cd order-lookup-service
venv\Scripts\activate.bat
uvicorn main:app --reload --port 8002

✅ 4. chat-service (Port: 8000)
cd chat-service
venv\Scripts\activate.bat
uvicorn main:app --reload --port 8000

🧪 Example Queries
Test using curl or Postman by sending POST requests to:

👉 http://localhost:8000/chat

🔹 Product Query:
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d "{\"message\": \"What are the best guitar strings under $10?\"}"

🔹 Order Query:
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d "{\"message\": \"What is my last order? My customer ID is 37077\"}"
