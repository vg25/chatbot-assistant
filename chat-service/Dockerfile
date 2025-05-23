FROM python:3.11-slim

WORKDIR /app

COPY . .

# Install system dependencies required by transformers and torch
RUN apt-get update && apt-get install -y git && apt-get clean

# Install Python dependencies
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    transformers \
    huggingface_hub \
    requests \
    torch

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
