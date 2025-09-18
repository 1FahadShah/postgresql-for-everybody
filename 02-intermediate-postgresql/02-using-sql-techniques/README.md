# Using SQL Techniques

This repository contains hands-on PostgreSQL notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.

This Module transitions from foundational SQL syntax to practical, business-oriented applications. It demonstrates how to build a relational database schema from scratch and leverage advanced queries, transactions, and procedures to solve real-world problems.

---

## Notebooks Overview 📓

### `01-simple-business.ipynb`
- Designs and implements a complete relational schema for a simple e-commerce business (`customers`, `products`, `orders`, `order_items`).
- Covers fundamental DDL (`CREATE TABLE`) and DML (`INSERT`) operations to populate the database.
- Demonstrates basic business reporting using multi-table `JOIN`s.
- Applies aggregation (`GROUP BY`, `SUM`) to derive insights like total customer spending.

### `02-advanced-queries-and-subqueries.ipynb`
- Focuses on advanced data retrieval techniques using the business schema.
- Implements **inline subqueries** (`IN`, `HAVING`) to filter data based on aggregate conditions.
- Demonstrates **correlated subqueries** to compare row-level data against category averages.
- Uses advanced aggregation (`STRING_AGG`) and derived tables (subqueries in `FROM`) for complex reporting.

### `03-transactions-concurrency-and-procedures.ipynb`
- Explores enterprise-level features for ensuring data integrity and automating logic.
- Implements **transactions** to guarantee atomic operations using `BEGIN`, `COMMIT`, and `ROLLBACK`.
- Demonstrates **concurrency control** by simulating row-level locking with `SELECT FOR UPDATE`.
- Encapsulates reusable business logic by creating **stored functions** (`CREATE FUNCTION`) in `plpgsql`.
- Shows how to automate actions using **triggers** that respond to data modifications.

---

## Key Takeaways ✨

1.  **Relational Schema Design** is the foundation of any robust database application, linking business entities logically.
2.  **Advanced Queries** and **Subqueries** are essential for extracting deep, specific insights that simple queries cannot provide.
3.  **Transactions** are critical for maintaining data integrity (ACID properties) in any application that performs multiple, related database writes.
4.  **Stored Functions and Triggers** allow business logic to be embedded directly within the database, promoting code reuse, security, and efficiency.
5.  This module bridges the gap between knowing basic SQL syntax and applying it to build and manage **real-world, data-driven business systems**.

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
4.  Run each notebook **cell-by-cell** to replicate all examples and hands-on exercises. The notebooks are designed to be run in sequential order.

---

## Technologies / Tags

`PostgreSQL` | `SQL` | `Business Intelligence` | `Database Schema` | `JOINs` | `Subqueries` | `Transactions` | `Stored Procedures` | `Triggers` | `Jupyter Notebook` | `Data Analysis` | `Backend Development`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.*
