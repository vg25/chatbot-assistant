# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy everything from your local folder into the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir fastapi uvicorn pandas

# Expose the port your service will run on
EXPOSE 8001

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
