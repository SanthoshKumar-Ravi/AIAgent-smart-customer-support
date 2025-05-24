FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt from the parent directory
COPY ../requirements.txt ./requirements.txt
COPY ../data ./data

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code from the context (./backend in build) to /app/backend
COPY backend/ ./

# Run FastAPI app using package-style import
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
