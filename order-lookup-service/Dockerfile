# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy local files into the container
COPY . .

# Install required packages
RUN pip install --no-cache-dir fastapi uvicorn pandas requests

# Expose the port
EXPOSE 8002

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
