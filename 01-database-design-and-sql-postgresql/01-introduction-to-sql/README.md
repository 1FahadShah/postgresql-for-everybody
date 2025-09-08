# Introduction to SQL

This repository contains the hands-on notebook, built and documented by **Fahad Shah (1FahadShah)**. It represents my personal solutions and learning journey through the *"PostgreSQL for Everybody"* Specialization offered by the University of Michigan on Coursera.

This foundational module covers the initial setup and fundamental commands required to interact with a PostgreSQL server using the `psql` command-line interface.

---

## Notebook Overview 📓

### `01-getting-started-with-postgresql.ipynb`
A step-by-step guide covering the entire initial workflow:
-   Installing and starting the PostgreSQL service.
-   Creating a new user and database.
-   Connecting to the database via `psql`.
-   Defining a table schema with `CREATE TABLE`.
-   Performing basic data operations with `INSERT` and `SELECT`.

---

## Key Concepts Covered ✨

This notebook provides a practical introduction to the core tasks of a database user.

#### 1. Server and User Management
Learn to manage the PostgreSQL service and create new users and databases with specific ownership and permissions.
```sql
CREATE USER fahad WITH PASSWORD 'secret';
CREATE DATABASE people WITH OWNER 'fahad';
```
#### 2. DDL and DML Basics
Get hands-on with the two fundamental sub-languages of SQL:

* **Data Definition Language (DDL)**: Define the structure of your database with `CREATE TABLE`.
* **Data Manipulation Language (DML)**: Interact with the data using `INSERT` to add records and `SELECT` to retrieve them.

---

## Setup Instructions 🛠️
1.  Install PostgreSQL on your system (the notebook provides examples for Linux/Debian).
2.  Ensure the `psql` command-line tool is available in your system's PATH.
3.  Connect to your default database as an admin user (e.g., `postgres`) to perform initial setup.
    ```bash
    # Example for Windows
    psql -U postgres
    ```
4.  Run the commands from the notebook to create your new user and database.

---

## Technologies / Tags
`PostgreSQL` | `SQL` | `psql` | `Database Administration` | `DDL` | `DML` | `Jupyter Notebook`

---
*This notebook is part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning journey.*
