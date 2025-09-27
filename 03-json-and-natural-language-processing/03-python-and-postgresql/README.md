# Python and PostgreSQL

This repository contains hands-on Jupyter notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.

This Module bridges the gap between the database and the application layer. It provides a comprehensive guide to interacting with a PostgreSQL database using Python, covering everything from establishing a connection and performing basic operations to critical security practices and advanced, production-level techniques.

---

## Notebooks Overview 📓

### `01-connecting-and-basic-queries.ipynb`
- Introduces the **`psycopg2`** library, the standard PostgreSQL adapter for Python.
- Explains the core concepts of `connection` and `cursor` objects for managing sessions and executing commands.
- Demonstrates how to fetch data using `fetchone()` and `fetchall()`.
- Establishes the best practice of using **`with` statements** for safe, automatic resource management.

### `02-crud-and-transaction-management.ipynb`
- Provides a practical guide to all four **CRUD** (Create, Read, Update, Delete) operations.
- Covers the critical concept of **database transactions**, explaining why changes are not permanent until committed.
- Demonstrates the use of `connection.commit()` to save a transaction and `connection.rollback()` to discard it.

### `03-preventing-sql-injection-and-handling-data.ipynb`
- Features a live demonstration of a **SQL injection attack** to show the dangers of improper query building.
- Teaches the single most important security practice: using **parameterized queries** (placeholders) to prevent SQL injection.
- Explores efficient data handling techniques, including using `DictCursor` for dictionary-like rows and loading data directly into a **Pandas DataFrame**.

### `04-advanced-techniques-and-best-practices.ipynb`
- Covers advanced topics for building robust applications.
- Implements specific **error handling** to gracefully manage database exceptions.
- Demonstrates efficient bulk data insertion using `executemany()` and proves its performance benefits.
- Explains how to call **stored procedures** from Python and introduces the concept of **connection pooling** for scalable applications.

---

## Key Takeaways ✨

1.  **`psycopg2` is the Standard:** It's the essential library for connecting any Python application to a PostgreSQL database.
2.  **Transactions are Explicit:** Database changes are atomic and are not saved until you explicitly `commit()` them. This is a core feature for ensuring data integrity.
3.  **Parameterization is Non-Negotiable Security:** Never use string formatting (like f-strings) to inject user data into queries. Always use the library's parameterization (`%s` placeholders) to make SQL injection impossible.
4.  **Handle Data Intelligently:** Move beyond simple tuples. Use `DictCursor` for readable code or load data directly into a **Pandas DataFrame** for powerful analysis.
5.  **Build for Production:** For real-world applications, use `executemany()` for bulk operations and understand the critical need for **connection pooling** to handle concurrent requests efficiently.

---

## Setup Instructions 🛠️

1.  Ensure you have a local PostgreSQL instance running with a database created (e.g., `people`).
2.  Install the required Python packages:
    ```bash
    pip install psycopg2-binary pandas
    ```
3.  Update the connection variables at the top of each notebook to match your local database credentials.
4.  Run each notebook **cell-by-cell** to replicate all examples and hands-on exercises.

---

## Technologies / Tags

`PostgreSQL` | `Python` | `psycopg2` | `CRUD` | `Transactions` | `SQL Injection` | `Database Security` | `Pandas` | `DataFrames` | `Stored Procedures` | `Connection Pooling` | `Backend Development` | `Database Administration`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.*
