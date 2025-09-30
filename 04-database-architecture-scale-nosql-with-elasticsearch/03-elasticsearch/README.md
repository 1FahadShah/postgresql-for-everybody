# Elasticsearch

This repository contains hands-on Jupyter notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.

This Module provides a comprehensive introduction to **Elasticsearch**, a powerful, distributed search and analytics engine. The notebooks cover its core concepts, how to interact with its REST API, its powerful Query DSL, programmatic use with Python, and its architectural role in a modern, hybrid system alongside PostgreSQL.

---

## Notebooks Overview 📓

### `01-introduction-to-elasticsearch-and-rest-api.ipynb`
- Provides a foundational understanding of what Elasticsearch is and its core concepts (Cluster, Index, Document).
- Maps Elasticsearch terminology to familiar relational database concepts.
- Demonstrates basic CRUD (Create, Read, Update, Delete) operations using `curl` to interact with the REST API.

### `02-deep-dive-into-elasticsearch-search-and-dsl.ipynb`
- A deep dive into Elasticsearch's core strength: its JSON-based **Query DSL (Domain Specific Language)**.
- Explains the critical difference between **Query Context** (for relevance scoring) and **Filter Context** (for yes/no filtering).
- Covers common query types (`match`, `term`) and how to combine them with the powerful `bool` query.

### `03-programming-elasticsearch-with-python-and-demos.ipynb`
- Shows how to interact with Elasticsearch programmatically using the official **Python client**.
- Translates `curl` commands into their Python equivalents for CRUD and search operations.
- Includes practical demos for indexing and searching different types of documents (books, emails, and tweets) using the `elasticsearch-py` library.

### `04-elasticsearch-and-postgresql-a-hybrid-architecture.ipynb`
- A high-level architectural notebook explaining the "why" and "how" of using Elasticsearch and PostgreSQL together.
- Details the **"Search-as-a-Sidecar"** pattern, where PostgreSQL is the source of truth and Elasticsearch is the secondary search index.
- Discusses data synchronization strategies, from simple dual writes to robust, real-time streaming.

---

## Key Takeaways ✨

1.  **Elasticsearch is a Search Engine First:** Its primary purpose is fast, scalable, and relevant full-text search, not to be a primary transactional database.
2.  **Interaction is via REST API:** All operations are done over standard HTTP, making Elasticsearch language-agnostic and easy to integrate with any application stack.
3.  **The Query DSL is Extremely Powerful:** The JSON-based Query DSL allows for incredibly complex and fine-tuned search queries that blend full-text relevance with structured filtering.
4.  **Use the Python Client for Applications:** The official Python client provides a clean and robust way to integrate Elasticsearch's advanced search capabilities into an application.
5.  **PostgreSQL + Elasticsearch is a Powerful Hybrid:** The best-practice architecture uses PostgreSQL for data integrity (ACID) and Elasticsearch for powerful search. This is a classic example of **Polyglot Persistence**.

---

## Setup Instructions 🛠️

1.  These notebooks are designed to be a self-contained, conceptual reference.
2.  All commands (`curl`, Python) and their expected outputs are "hardcoded" into the markdown.
3.  No live Elasticsearch instance is required to read and learn from these notebooks.

---

## Technologies / Tags

`Elasticsearch` | `NoSQL` | `Search Engine` | `Full-Text Search` | `REST API` | `curl` | `Query DSL` | `Python` | `PostgreSQL` | `System Design` | `Database Architecture` | `Polyglot Persistence` | `ACID` | `BASE`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.* 
