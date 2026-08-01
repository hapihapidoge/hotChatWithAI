# OceanBase 4.3.x: Hybrid query (ANN_SEARCH + WHERE clause) forces full table scan instead of Vector Index Pre-filtering

Curated at: `2026-08-01T03:49:58.778019+00:00`
Model: `Public Q&A`
Author: `Dmitry543`
Tags: `public-q&a, Stack Overflow, vector-database, rag, query-planner, oceanbase`
Source: https://stackoverflow.com/questions/79986462/oceanbase-4-3-x-hybrid-query-ann-search-where-clause-forces-full-table-scan


## Why It Is Good

- Public Q&A from Stack Overflow.
- Question score: 1; answer score: 1.
- Viewed 57 times on the source site.

## Question

We are building a multi-tenant enterprise RAG system using OceanBase 4.3.x (MySQL mode). Our table stores 1536-dimensional embeddings with a native VSAG vector index, along with a standard tenant_id integer column which has a normal B-tree index. We are experiencing a severe performance issue when running hybrid queries that combine vector similarity search with a strict scalar filter for tenant isolation. Here is the exact query structure: SELECT doc_id, chunk_text FROM enterprise_knowledge_base WHERE tenant_id = 10025 AND status = 'ACTIVE' ORDER BY APPROX_DISTANCE(embedding_data, \[0.015, -0.023, 0.112, 0.045\]) APPROX_TOP 5;

## Answer

The likely issue is that OceanBase uses the VSAG index first, then applies tenant_id and status afterward. The B-tree and vector index are not efficiently combined. Check with: EXPLAIN SELECT doc_id, chunk_text FROM enterprise_knowledge_base WHERE tenant_id = 10025 AND status = 'ACTIVE' ORDER BY APPROX_DISTANCE(embedding_data, '[...]') APPROX_TOP 5; A composite index helps normal filtering, but not ANN pre-filtering: CREATE INDEX idx_tenant_status ON enterprise_knowledge_base (tenant_id, status);
