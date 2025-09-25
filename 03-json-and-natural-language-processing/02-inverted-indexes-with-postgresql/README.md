# Inverted Indexes with PostgreSQL

This repository contains hands-on PostgreSQL notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.

This Module takes a deep dive into the mechanics of inverted indexes, focusing on the powerful **GIN (Generalized Inverted Index)**. The notebooks explore GIN's versatility beyond text, the specifics of natural language configurations, advanced query functions, and the production-ready workflows for implementing high-performance Full-Text Search.

---

## Notebooks Overview 📓

### `01-gin-based-inverted-index.ipynb`
- Explores the "Generalized" nature of GIN indexes by applying them to non-text data.
- Demonstrates how to create a GIN index on an `integer[]` array to rapidly search for elements within rows.
- Uses `EXPLAIN ANALYZE` to contrast a slow `Seq Scan` on an array with a fast `Bitmap Index Scan` using GIN.

### `02-natural-language-index.ipynb`
- Implements a complete, practical Full-Text Search workflow from start to finish.
- Covers creating a table with a dedicated `tsvector` column and populating it using `to_tsvector`.
- Builds a GIN index on the `tsvector` column to accelerate queries.
- Demonstrates searching with `to_tsquery` and ranking results by relevance using `ts_rank`.

### `03-tsquery-tsvector-functions.ipynb`
- Dives deeper into the functions available for handling user search input.
- Introduces `plainto_tsquery` for simple keyword searches where boolean operators aren't needed.
- Explains `phraseto_tsquery` for exact phrase matching, which is more precise than `to_tsquery` with the `<->` operator.

### `04-gin-tsvector-index.ipynb`
- Consolidates all learnings into a production-ready, automated FTS system.
- Implements a **PL/pgSQL function** and **trigger** to automatically update the `tsvector` column on any `INSERT` or `UPDATE`.
- Provides a clear comparison of **GIN vs. GiST** indexes, outlining the trade-offs between query speed and update speed.

---

## Key Takeaways ✨

1.  **GIN is a Versatile Tool:** GIN is a general-purpose inverted index designed for "composite" data types. Its ability to index individual items within a larger object (like elements in an `array` or lexemes in a `tsvector`) is what makes it so powerful.
2.  **FTS Configurations are Crucial:** The "language" (`'english'`, `'french'`, etc.) is a full configuration dictating stop words and stemming. Choosing the right configuration is critical for search accuracy.
3.  **Query Functions Match Use Cases:** PostgreSQL provides multiple functions to parse search strings (`to_tsquery`, `plainto_tsquery`, `phraseto_tsquery`), allowing you to choose the right tool for the type of search you are offering.
4.  **Automation is the Production Standard:** The most robust and efficient way to implement FTS is to use a dedicated `tsvector` column that is automatically kept in sync with source data using a **database trigger**.
5.  **GIN is the Default for FTS Performance:** For most search applications where data is read more often than written, a GIN index provides the best query performance.

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

`PostgreSQL` | `SQL` | `Full-Text Search` | `FTS` | `GIN Index` | `Inverted Index` | `tsvector` | `tsquery` | `plainto_tsquery` | `phraseto_tsquery` | `Triggers` | `PL/pgSQL` | `Arrays` | `Database Indexing` | `Performance Tuning` | `Jupyter Notebook`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.*
