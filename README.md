# 🤖 Smart Customer Support AI
A full-stack AI-powered customer support application that answers user queries using a fine-tuned LLM, stores conversations and feedback in Redis, and offers an intuitive Streamlit UI for interaction and feedback collection.

## ✨ Features
✅ LLM-powered real-time Q&A engine using Ollama (LLaMA3)

✅ Redis for persistent storage of Q&A and feedback data

✅ LangChain & FAISS-based semantic search

✅ Streamlit frontend for user interaction

✅ FastAPI backend to serve AI and feedback endpoints

✅ Feedback loop for continuous improvement

✅ Dockerized microservice architecture

## 🛠️ Tech Stack

| **Layer**	| **Technology** |
| :---:          |   :---:          |
| Frontend | 	Streamlit |
| Backend	| FastAPI |
| LLM Engine |	Ollama (LLaMA3) |
| Vector Store |	FAISS + LangChain |
|Database |	Redis |
| DevOps |	Docker, Docker Compose |

## 📁 Project Structure
```
llm-support-ai/
│
├── backend/              # FastAPI backend service
│   ├── main.py
│   ├── model.py
│   ├── feedback.py
│   └── dockerfile
│
├── frontend/             # Streamlit frontend service
│   └── streamlit_app.py
|   └── Dockerfile
│
├── requirements.txt      # Common dependencies
├── docker-compose.yml    # Multi-service container orchestration
└── README.md             # Project documentation
```

## 🧑‍💻 Running Locally (Dev Setup)

### ✅ Prerequisites

1. Python 3.11+
2. Redis running on localhost:6379
3. Ollama with LLaMA3 model installed (ollama pull llama3)


### 🚀 Step-by-step

**1. Clone the repository**

```
git clone https://github.com/your-username/llm-support-ai.git
```

```
cd llm-support-ai
```

**2. Install dependencies**

```
pip install -r requirements.txt
```

**3. Start Backend**

```
cd backend
uvicorn main:app --reload
```

**4. Start Frontend**

```
cd frontend
streamlit run app.py
```

**Test the App**

Open http://localhost:8501 in your browser and start interacting!

## 🐳 Running with Docker (Prod Setup)
### ✅ Prerequisites

1. Docker
2. Docker Compose
3. Ollama running locally (or modify to use Ollama container)

### 🚀 Start the Application

```
docker-compose up --build
```
This will:
Start the FastAPI backend on http://localhost:8000
Start the Streamlit frontend on http://localhost:8501

### 🧠 Ensure Ollama is Running
If you’re running Ollama locally:

```
ollama run llama3
```
Or include Ollama in the docker-compose.yml if you want a complete containerized setup.

