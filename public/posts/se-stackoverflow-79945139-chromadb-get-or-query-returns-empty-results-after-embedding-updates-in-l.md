# ChromaDB get() or query() returns empty results after embedding updates in LangChain

Curated at: `2026-06-01T05:16:13.241175+00:00`
Model: `Public Q&A`
Author: `Ritik Thakur`
Tags: `public-q&a, Stack Overflow, python, langchain, vector-database, chromadb, rag`
Source: https://stackoverflow.com/questions/79945139/chromadb-get-or-query-returns-empty-results-after-embedding-updates-in-langc


## Why It Is Good

- Public Q&A from Stack Overflow.
- Question score: 1; answer score: 1.
- Viewed 63 times on the source site.

## Question

I am building a local RAG pipeline using LangChain, ChromaDB, and a local embedding model. The document ingestion pipeline runs without errors, and the vector store initializes correctly. However, when I attempt to query the vector store immediately after updating or adding new documents, the similarity search returns empty lists [] or fails to retrieve the newly added chunks. Here is a minimal reproducible example of how I am initializing the store and adding documents: [code omitted] What I have tried: I verified that add_documents returns the list of UUIDs successfully, meaning the write operation completes without an explicit exception. If I restart the entire Python script and initiali...

## Answer

The issue is mostly due to the older LangChain Chroma wrapper keeping a stale collection state after add_documents() . Instead of: [code omitted] use: from langchain_chroma import Chroma With newer chromadb versions, newly added embeddings are sometimes not immediately reflected in the active retriever session. Re-initializing the vector store after add_documents() usually fixes it: vector_store.add_documents(docs, ids=ids) vector_store = Chroma( collection_name="research_docs", embedding_function=embeddings, persist_directory="./chroma_db" ) Also make sure: old collections are not created with different embedding models collection count is increasing: print(vector_store._collection.count()) This is mainly a compatibility/state refresh issue between newer chromadb and the deprecated langchain_community wrapper.
