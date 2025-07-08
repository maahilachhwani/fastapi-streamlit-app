import os

import streamlit as st

from transformers import pipeline

from sentence_transformers import SentenceTransformer, util

import faiss

import numpy as np

def load_documents(directory):
    documents = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                documents.append(file.read())
                filenames.append(filename)
    return documents, filenames

def summarize_documents(documents):
    summarizer = pipeline("summarization")
    summaries = [summarizer(doc, max_length=150, min_length=30, do_sample=False)[0]['summary_text'] for doc in documents]
    return summaries

def embed_documents(documents):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(documents, convert_to_tensor=True)
    return embeddings, model

def build_faiss_index(embeddings):
    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    faiss.normalize_L2(embeddings.numpy())
    index.add(embeddings.numpy())
    return index

def retrieve_documents(query, model, index, documents, k=5):
    query_embedding = model.encode(query, convert_to_tensor=True)
    faiss.normalize_L2(query_embedding.numpy())
    D, I = index.search(query_embedding.numpy(), k)
    retrieved_docs = [documents[i] for i in I[0]]
    return retrieved_docs

def generate_response(retrieved_docs, query):
    generator = pipeline("text-generation", model="gpt-2")
    context = " ".join(retrieved_docs)
    prompt = f"Contesxt: {context}\n\nQuestion: {query}\nAnswer:"
    response = generator(prompt, max_length=150, num_return_sequences=1)
    return response[0]['generated_text']

def main():
    st.title("Smart Document Assistant")

    directory = st.text_input("Enter the path to your document directory:", "C:/Users/Admin/Downloads")
    if st.button("Load and Summarize Documents"):
        with st.spinner("Loading documents..."):
            documents, filenames = load_documents(directory)
        with st.spinner("Summarizing documents..."):
            summaries = summarize_documents(documents)
        
        for i, summary in enumerate(summaries):
            st.subheader(f"Summary of {filenames[i]}")
            st.write(summary)

        embeddings, model = embed_documents(documents)
        index = build_faiss_index(embeddings)
        
        st.success("Documents loaded and summarized successfully!")

    query = st.text_input("Ask a question about the documents:")
    if query:
        retrieved_docs = retrieve_documents(query, model, index, documents)
        response = generate_response(retrieved_docs, query)
        st.subheader("Response")
        st.write(response)

if __name__ == "__main__":
    main()
