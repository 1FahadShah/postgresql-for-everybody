# Natural Language

This repository contains hands-on PostgreSQL notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.

This Module provides a deep dive into how PostgreSQL handles text, from the fundamental physical storage of data to building a high-performance, production-ready Full-Text Search engine. The notebooks demonstrate the core principles of database indexing and natural language processing.

---

## Notebooks Overview 📓

### `01-allocating-rows-to-blocks-in-postgresql.ipynb`
- Explores the physical storage layer of PostgreSQL, including **pages (blocks)** and **tuples (rows)**.
- Introduces the `ctid` system column as the physical address of a row.
- Covers **TOAST** (The Oversized-Attribute Storage Technique) for handling large data.

### `02-index-implementation.ipynb`
- Explains the theory and implementation of standard **B-Tree indexes**.
- Uses `EXPLAIN ANALYZE` to contrast slow **Sequential Scans** with fast **Index Scans**.
- Demonstrates how indexes map data values to `ctid`s to accelerate queries.

### `03-building-an-inverted-index.ipynb`
- Provides a step-by-step guide to manually building an **Inverted Index**, the core data structure for text search.
- Covers tokenizing documents into words and populating the index table.
- Uses the manual index to perform and retrieve text-based search results.

### `04-building-natural-language-index.ipynb`
- Introduces PostgreSQL's powerful, built-in **Full-Text Search (FTS)** engine.
- Explains the core components: `tsvector` for documents and `tsquery` for queries.
- Demonstrates how FTS automatically handles **stemming** and **stop-word removal**.

### `05-sql-natural-language.ipynb`
- Covers advanced, real-world FTS features for building search applications.
- Implements **result ranking** with `ts_rank_cd` to show the most relevant matches first.
- Uses `ts_headline` to create highlighted snippets of search results.
- Supercharges FTS performance with specialized **GIN (Generalized Inverted Index)** indexes.

---

## Key Takeaways ✨

1.  **Physical Storage is the Foundation:** Understanding how data is stored in **pages** with unique `ctid`s is the key to understanding all database performance.
2.  **Indexes are Not Optional:** For any non-trivial amount of data, the difference between a `Seq Scan` and an `Index Scan` is the difference between an unusable and a high-performance application.
3.  **Inverted Indexes Power Search:** The concept of mapping terms to documents is the fundamental principle behind all text search, and building one manually provides crucial insight.
4.  **PostgreSQL FTS is Production-Ready:** The built-in engine (`tsvector`, `tsquery`) provides a sophisticated solution that handles stemming, stop words, ranking, and complex queries out of the box.
5.  **Use the Right Index for the Job:** While **B-Tree** is the default for most data types, a **GIN** index is essential for making `tsvector`-based searches fast and efficient.

---

## Setup Instructions 🛠️

1.  Install PostgreSQL and create a database (e.g., `people`).
2.  Install required Python packages for Jupyter integration:
    ```bash
    pip install ipython-sql psycopg2-binary "prettytable<3.0.0"
    ```
3.  Load the SQL extension and connect to your database at the start of each notebook:
    ```python
    %load_ext sql
    %sql postgresql://fahad:secret@localhost:5432/people
    ```
4.  Run each notebook **cell-by-cell** to replicate all examples and hands-on exercises.

---

## Technologies / Tags

`PostgreSQL` | `SQL` | `Full-Text Search` | `FTS` | `Natural Language Processing` | `NLP` | `tsvector` | `tsquery` | `GIN Index` | `Inverted Index` | `B-Tree` | `Database Internals` | `Performance Tuning` | `Jupyter Notebook`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.*
