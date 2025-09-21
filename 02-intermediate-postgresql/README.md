# Course 2: Intermediate PostgreSQL
[![Coursera Certificate](https://img.shields.io/badge/Coursera-Certificate-blue?logo=coursera)](https://www.coursera.org/account/accomplishments/verify/WXWIF14TTCCU)

This repository contains hands-on Jupyter notebooks built and documented by **Fahad Shah (1FahadShah)**. It represents my personal learning journey and practical solutions for **[Course 2: Intermediate PostgreSQL](https://www.coursera.org/account/accomplishments/verify/WXWIF14TTCCU)** from the **PostgreSQL for Everybody Specialization**
offered by the **University of Michigan** on Coursera.

The notebooks build upon foundational knowledge to cover advanced SQL techniques, including schema evolution, complex queries, transaction management, text processing, and performance optimization—skills essential for building robust, real-world applications.

---

## 📚 Course Structure

This course consists of **four main modules**, each documented with dedicated notebooks that transition from theory to practical application.

| Module     | Notebook(s)                                                                                                                                                             | Key Topics Covered                                                                      |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| **Module&nbsp;1** | `01-alter-table-schema.ipynb`<br>`02-dates.ipynb`<br>`03-distinct-group-by.ipynb`<br>`04-subqueries.ipynb`<br>`05-concurrency-and-transactions.ipynb`<br>`06-stored-procedures.ipynb` | Schema evolution with `ALTER TABLE`, date/time functions, aggregation, subqueries, transactions, stored procedures |
| **Module&nbsp;2** | `01-simple-business.ipynb`<br>`02-advanced-queries-and-subqueries.ipynb`<br>`03-transactions-concurrency-and-procedures.ipynb`                                          | Building a business schema, advanced queries (`STRING_AGG`), practical transaction control, triggers         |
| **Module&nbsp;3** | `01-text-in-databases.ipynb`<br>`02-text-functions.ipynb`<br>`03-character-sets.ipynb`<br>`04-inside-hashes.ipynb`<br>`05-index-choices-and-techniques.ipynb`     | Text manipulation, `UTF-8`, cryptographic hashing with `pgcrypto`, indexing for text (`GIN`, `GiST`)       |
| **Module&nbsp;4** | `01-regular-expressions.ipynb`<br>`02-regular-expressions-quick-guide.ipynb`                                                                                        | Regular expression syntax (`^`, `$`, `[]`, `*`, `+`), pattern matching operators (`~`, `~*`), regex functions |

---

## 📓 Notebook Overviews

### 1. SQL Techniques
**Notebooks:**
* `01-alter-table-schema.ipynb`
* `02-dates.ipynb`
* `03-distinct-group-by.ipynb`
* `04-subqueries.ipynb`
* `05-concurrency-and-transactions.ipynb`
* `06-stored-procedures.ipynb`

**Highlights:**
* **Schema Evolution**: Using `ALTER TABLE` to add, modify, and drop columns and constraints.
* **Temporal Data**: Handling `DATE`, `TIMESTAMP`, and `INTERVAL` with functions like `EXTRACT()` and `AGE()`.
* **Data Aggregation**: Grouping with `GROUP BY`, filtering groups with `HAVING`, and using aggregate functions (`COUNT`, `SUM`, `AVG`).
* **Advanced Queries**: Writing nested and scalar subqueries with `IN`, `EXISTS`, and `FROM` clauses.
* **Data Integrity**: Managing transactions with `BEGIN`, `COMMIT`, `ROLLBACK`, and understanding concurrency.
* **Encapsulation**: Creating and managing **stored procedures** to reuse SQL logic.

### 2. Business Applications with SQL
**Notebooks:**
* `01-simple-business.ipynb`
* `02-advanced-queries-and-subqueries.ipynb`
* `03-transactions-concurrency-and-procedures.ipynb`

**Highlights:**
* **Practical Data Modeling**: Designing a complete e-commerce schema (`customers`, `products`, `orders`).
* **Business Intelligence Queries**: Applying correlated subqueries and advanced aggregation (`STRING_AGG`) to derive business insights.
* **Enterprise Features**: Using **transactions**, row-level locking (`SELECT FOR UPDATE`), and **triggers** in a practical business context to ensure data integrity and automate logic.

### 3. Advanced Text Handling & Hashing
**Notebooks:**
* `01-text-in-databases.ipynb`
* `02-text-functions.ipynb`
* `03-character-sets.ipynb`
* `04-inside-hashes.ipynb`
* `05-index-choices-and-techniques.ipynb`

**Highlights:**
* **Text Manipulation**: A deep dive into string functions for cleaning, parsing, and formatting (`TRIM`, `SUBSTRING`, `REPLACE`).
* **Character Encoding**: Understanding **`UTF-8`** for multilingual data and comparing `ASCII()`/`CHR()` in SQL with Python's `ord()`/`chr()` and `.encode()`/`.decode()`.
* **Cryptographic Hashing**: Securing data with the **`pgcrypto`** extension (`digest()`, `crypt()`) and understanding hash collisions.
* **Full-Text Search**: Optimizing text queries with specialized indexes like **`GIN`** and **`GiST`**.

### 4. Regular Expressions
**Notebooks:**
* `01-regular-expressions.ipynb`
* `02-regular-expressions-quick-guide.ipynb`

**Highlights:**
* **Advanced Pattern Matching**: Mastering **Regular Expressions (Regex)** syntax, including anchors, quantifiers, character classes, grouping, and alternation.
* **Regex in PostgreSQL**: Using the `~` and `~*` operators for powerful text searches.
* **Practical Reference**: A "cheat sheet" notebook with a summary table and ready-to-use patterns for common tasks like validating emails and dates.

---

### 🚀 Technologies / Tags
`PostgreSQL` | `SQL` | `Backend Development` | `Database Design` | `DDL` | `DML` | `ALTER TABLE` | `Subqueries` | `Transactions` | `Stored Procedures` | `Triggers` | `Business Intelligence` | `Text Manipulation` | `Character Sets` | `UTF-8` | `Hashing` | `pgcrypto` | `Database Indexing` | `B-Tree` | `GIN Index` | `Full-Text Search` | `Regular Expressions` | `Regex` | `Performance Tuning` | `Jupyter Notebook`

This repository is part of my Execution Journey through the PostgreSQL for Everybody Specialization, documented by **1FahadShah**.
It serves as a practical portfolio showcasing my progress in advanced SQL, text processing, and database optimization.
