# Single Table SQL

This repository contains hands-on `PostgreSQL` notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my personal solutions and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**. The content is designed to be a practical guide for learning essential concepts and demonstrating skills applicable to **real-world backend development**.

## Notebooks Overview

### 1. `01-working-with-sql.ipynb`
- Introduces fundamental SQL commands in PostgreSQL.
- Covers basic CRUD operations (`INSERT`, `SELECT`, `UPDATE`, `DELETE`).
- Demonstrates filtering (`WHERE`, `LIKE`), sorting (`ORDER BY`), and limiting results (`LIMIT`, `OFFSET`).

### 2. `02-datatypes-in-postgresql.ipynb`
- A deep dive into **PostgreSQL data types** with practical examples.
- Demonstrates table creation, data insertion, and querying for each type.
- Highlights:
  - `SERIAL` for auto-incrementing IDs
  - `NUMERIC`, `REAL`, `DOUBLE PRECISION` for numeric precision
  - `CHAR`, `VARCHAR`, `TEXT` for character data
  - `BOOLEAN` for true/false flags
  - `TIMESTAMP`, `TIMESTAMPTZ` for datetime
  - `UUID` for distributed unique identifiers
  - `ARRAY` and `JSON`/`JSONB` for structured data

### 3. `03-indexes-in-postgresql.ipynb`
- Focuses on **database indexes** and performance optimization.
- Explains and demonstrates various types of indexes:
  - Simple (B-Tree) Index
  - Unique Index
  - Multi-Column Index
  - Partial Index
  - Expression Index
- Discusses different index algorithms (`B-TREE`, `GIN`, `GiST`, etc.) and their use cases.

## Key Takeaways
1.  Choose data types wisely to match your application requirements and performance needs.
2.  Indexing is crucial for query optimization, especially with large datasets.
3.  PostgreSQL's support for `JSON`, `ARRAY`, and `UUID` provides flexibility for modern applications.
4.  Practicing with these notebooks prepares you for real-world PostgreSQL tasks and backend development.

## Setup Instructions
1.  Install PostgreSQL and create a database (e.g., `people`).
2.  Install the necessary Python packages for Jupyter integration:
    ```bash
    pip install ipython-sql psycopg2-binary "prettytable<3.0.0"
    ```
3.  Load the SQL extension and connect to your database at the start of your notebook:
    ```python
    %load_ext sql
    %sql postgresql://username:password@localhost:5432/people
    ```
4.  Run each notebook cell-by-cell to replicate the examples.

## Technologies / Tags
`PostgreSQL` | `SQL` | `Datatypes` | `Indexes` | `Jupyter Notebook` | `Database Design` | `Backend Development`

---
*These notebooks are part of my Execution Journey of PostgreSQL for Everybody Specialization*
