# Course 3 - JSON and Natural Language Processing in PostgreSQL
[![Coursera Certificate](https://img.shields.io/badge/Coursera-Certificate-blue?logo=coursera)](https://www.coursera.org/account/accomplishments/verify/VD8ZWISGEXQX)

This repository contains hands-on Jupyter notebooks built and documented by **Fahad Shah (1FahadShah)**. It represents my personal learning journey and practical solutions for **[Course 3: JSON and Natural Language Processing in PostgreSQL](https://www.coursera.org/account/accomplishments/verify/VD8ZWISGEXQX)** from the **PostgreSQL for Everybody Specialization** offered by the **University of Michigan** on Coursera.

This course covers a wide range of advanced topics, bridging the gap between the database and application. It starts with a deep dive into database internals and Full-Text Search, then moves to application development with Python, data interchange formats like JSON, and finally culminates in building a functional web API.

---

## 📚 Course Structure

This course consists of **four main modules**, each documented with dedicated notebooks that build from foundational theory to practical, real-world application.

| Module      | Notebook(s)                                                                                                                                                                                             | Key Topics Covered                                                                                                           |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------- |
| **Module&nbsp;1** | `01-allocating-rows-to-blocks-in-postgresql.ipynb`<br>`02-index-implementation.ipynb`<br>`03-building-an-inverted-index.ipynb`<br>`04-building-natural-language-index.ipynb`<br>`05-sql-natural-language.ipynb` | Physical storage (`ctid`), B-Tree vs. GIN indexes, manual inverted index, Full-Text Search (FTS) basics, ranking, and highlighting. |
| **Module&nbsp;2** | `01-gin-based-inverted-index.ipynb`<br>`02-natural-language-index.ipynb`<br>`03-tsquery-tsvector-functions.ipynb`<br>`04-gin-tsvector-index.ipynb`                                                     | Deep dive into GIN indexes, FTS configurations for different languages, advanced `tsquery` operators, and production FTS with triggers. |
| **Module&nbsp;3** | `01-connecting-to-postgresql-with-psycopg2.ipynb`<br>`02-crud-and-transaction-management.ipynb`<br>`03-preventing-sql-injection-and-handling-data.ipynb`<br>`04-advanced-python-postgresql-integration.ipynb` | Python integration with `psycopg2`, CRUD, transactions, SQL injection prevention, Pandas integration, and connection pooling. |
| **Module&nbsp;4** | `01-data-formats-json-vs-xml.ipynb`<br>`02-working-with-json-in-python.ipynb`<br>`03-storing-and-querying-json-in-postgresql.ipynb`<br>`04-building-a-simple-json-api-with-python-and-postgresql.ipynb` | Data interchange formats (JSON vs. XML), Python's `json` library, PostgreSQL's `JSONB` data type, querying JSON, GIN indexing for `JSONB`, and building a Flask API. |

---

## 📓 Notebook Overviews

### 1. Natural Language in PostgreSQL
**Highlights:**
* **Physical Storage is the Foundation:** Understanding how data is stored in **pages** with unique `ctid`s is the key to all database performance.
* **Indexes are Not Optional:** The difference between a `Seq Scan` and an `Index Scan` is the difference between an unusable and a high-performance application.
* **Inverted Indexes Power Search:** The concept of mapping terms to documents is the fundamental principle behind all text search.
* **PostgreSQL FTS is Production-Ready:** The built-in engine (`tsvector`, `tsquery`) provides a sophisticated solution that handles stemming, stop words, ranking, and complex queries.
* **Use the Right Index for the Job:** While **B-Tree** is the default for most data types, a **GIN** index is essential for making `tsvector`-based searches fast and efficient.

### 2. Inverted Indexes with PostgreSQL
**Highlights:**
* **GIN is a Versatile Tool:** GIN is a general-purpose inverted index designed for "composite" data types like `array`, `JSONB`, and `tsvector`.
* **FTS Configurations are Crucial:** The "language" (`'english'`, `'french'`) is a full configuration that dictates stop words and stemming, and choosing the right one is critical for accuracy.
* **Query Functions Match Use Cases:** PostgreSQL provides multiple functions (`to_tsquery`, `plainto_tsquery`, `phraseto_tsquery`) to parse search strings for different scenarios.
* **Automation is the Production Standard:** The most robust way to implement FTS is with a dedicated `tsvector` column automatically kept in sync using a **database trigger**.

### 3. Python and PostgreSQL
**Highlights:**
* **`psycopg2` is the Standard:** It's the essential library for connecting any Python application to a PostgreSQL database.
* **Transactions are Explicit:** Database changes are atomic and are not saved until you explicitly `commit()` them, ensuring data integrity.
* **Parameterization is Non-Negotiable Security:** Always use placeholders (`%s`) to pass data into queries to make SQL injection impossible.
* **Handle Data Intelligently:** Use `DictCursor` for readable code or load data directly into a **Pandas DataFrame** for powerful analysis.
* **Build for Production:** Use `executemany()` for bulk operations and understand the critical need for **connection pooling**.

### 4. Data Formats, Python, and PostgreSQL APIs
**Highlights:**
* **JSON is the Lingua Franca of APIs:** Its lightweight syntax and direct mapping to native data structures make it the ideal choice for modern web services.
* **Always Prefer `JSONB` in PostgreSQL:** For any serious application, the binary, indexable `JSONB` type is vastly superior to the plain text `JSON` type.
* **GIN Indexes are Essential for `JSONB` Performance:** To efficiently query `JSONB` data using operators like containment (`@>`), a **GIN index** is a requirement for scalability.
* **The Full Stack Connects:** A complete application involves a client consuming a **JSON API**, powered by a server (like **Flask**) that in turn queries a database (like **PostgreSQL**).

---

### 🚀 Technologies / Tags
`PostgreSQL` | `Python` | `SQL` | `Full-Text Search` | `FTS` | `Natural Language Processing` | `NLP` | `JSON` | `JSONB` | `XML` | `API` | `Flask` | `psycopg2` | `Pandas` | `GIN Index` | `Inverted Index` | `B-Tree` | `Triggers` | `PL/pgSQL` | `Database Internals` | `SQL Injection` | `Performance Tuning` | `Jupyter Notebook` | `Backend Development` | `Database Administration`

---

This repository is part of my Execution Journey through the PostgreSQL for Everybody Specialization, documented by **1FahadShah**. It serves as a practical portfolio showcasing my progress in advanced database features, application integration, and API development.
