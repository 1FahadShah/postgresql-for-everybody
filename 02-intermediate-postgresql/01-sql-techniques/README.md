# SQL Techniques

This repository contains hands-on PostgreSQL notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.  

This Module covers **fundamental SQL operations, table management, queries, transactions, and stored procedures** — providing a solid foundation for real-world backend development and database-driven tools.

---

## Notebooks Overview 📓

### `01-alter-table-schema.ipynb`
- Covers altering table structures using `ALTER TABLE`.
- Demonstrates adding, modifying, and dropping columns.
- Shows renaming tables and columns.
- Explains constraints like `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, and `NOT NULL`.

### `02-dates.ipynb`
- Focuses on handling **date and time** in PostgreSQL.
- Demonstrates `DATE`, `TIMESTAMP`, `INTERVAL`.
- Shows date arithmetic, formatting, and extraction.
- Covers functions like `NOW()`, `CURRENT_DATE`, `EXTRACT()`, and `AGE()`.

### `03-distinct-group-by.ipynb`
- Explains data aggregation using `GROUP BY`.
- Shows `DISTINCT` for unique records.
- Covers aggregation functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
- Combines filtering with `HAVING` for group-level conditions.

### `04-subqueries.ipynb`
- Teaches nested queries for advanced filtering and aggregation.
- Covers scalar subqueries, `IN`, `EXISTS`, `ANY`, and `ALL`.
- Demonstrates using subqueries in `SELECT`, `FROM`, and `WHERE` clauses.

### `05-concurrency-and-transactions.ipynb`
- Explains **transaction management** with `BEGIN`, `COMMIT`, `ROLLBACK`.
- Demonstrates isolation levels and concurrency control.
- Shows practical examples of `SERIALIZABLE` and `REPEATABLE READ` modes.
- Covers locking strategies: row-level and table-level locks.

### `06-stored-procedures.ipynb`
- Covers creating, calling, and managing **stored procedures**.
- Demonstrates `IN`, `OUT`, `INOUT` parameters.
- Shows dynamic SQL inside procedures for flexible table/column handling.
- Highlights best practices for encapsulating SQL logic in real-world applications.

---

## Key Takeaways ✨

1. Mastering **DDL** and **DML** operations is essential for database design and manipulation.
2. Understanding **dates, aggregates, and subqueries** is crucial for building accurate queries and reports.
3. **Transactions and concurrency** ensure data integrity and consistency in multi-user environments.
4. **Stored procedures** allow encapsulating logic, improving code reuse, security, and maintainability.
5. These notebooks prepare you for **real-world backend development**, FAANG-style database systems, and building your own data-driven tools.

---

## Setup Instructions 🛠️

1. Install PostgreSQL and create a database (e.g., `people`).
2. Install required Python packages for Jupyter integration:
    ```bash
    pip install ipython-sql psycopg2-binary "prettytable<3.0.0"
    ```
3. Load the SQL extension and connect to your database at the start of each notebook:
    ```python
    %load_ext sql
    %sql postgresql://fahad:secret@localhost:5432/people
    ```
4. Run each notebook **cell-by-cell** to replicate all examples and hands-on exercises.

---

## Technologies / Tags

`PostgreSQL` | `SQL` | `DDL` | `DML` | `Transactions` | `Stored Procedures` | `Aggregation` | `Subqueries` | `Dates` | `Jupyter Notebook` | `Database Design` | `Backend Development`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.*
