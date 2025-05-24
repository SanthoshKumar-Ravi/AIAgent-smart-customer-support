import os
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama

def get_qa_chain():
    index_path = "../vector_db"
    embeddings = OllamaEmbeddings(model="llama3")

    if not os.path.exists(f"{index_path}/index.faiss"):
        loader = TextLoader("data/banking_faq.txt")
        docs = loader.load()
        splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        db = FAISS.from_documents(chunks, embeddings)
        db.save_local(index_path)
    else:
        db = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

    retriever = db.as_retriever()
    llm = ChatOllama(model="llama3")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
