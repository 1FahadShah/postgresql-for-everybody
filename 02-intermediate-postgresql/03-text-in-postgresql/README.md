# Text in PostgreSQL

This repository contains hands-on PostgreSQL notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.

This Module dives deep into advanced text manipulation, data generation, security through hashing, and critical performance optimization techniques using database indexes. The notebooks bridge the gap between basic data storage and building efficient, secure, and robust database applications.

---

## Notebooks Overview 📓

### `01-text-in-databases.ipynb`
- Explores functions for programmatic data generation, essential for testing and prototyping.
- Demonstrates `repeat()` to create patterned string data.
- Uses `random()` to populate columns with pseudo-random numbers.
- Covers `generate_series()` to create and insert sequential data sets efficiently.

### `02-text-functions.ipynb`
- Provides a comprehensive guide to PostgreSQL's built-in string manipulation functions.
- Covers text cleaning and formatting, including case conversion (`UPPER`, `LOWER`) and trimming (`TRIM`).
- Demonstrates parsing and extraction with `SUBSTRING`, `SPLIT_PART`, and `POSITION`.
- Shows how to modify strings using `REPLACE`, `TRANSLATE`, and `REGEXP_REPLACE`.

### `03-character-sets.ipynb`
- Explains character encoding (`UTF-8`) and its importance for handling multilingual data and emojis.
- Compares PostgreSQL's `ASCII()` and `CHR()` with Python's `ord()` and `chr()`.
- Demonstrates how Python handles Unicode strings and byte conversion using `.encode()` and `.decode()`.

### `04-inside-hashes.ipynb`
- Introduces cryptographic hashing for data integrity and security.
- Shows how to enable and use the **`pgcrypto`** extension in PostgreSQL.
- Implements `digest()` to create `MD5` and `SHA256` hashes and compares them with Python's `hashlib`.
- Illustrates the concept of **hash collisions** with a simple, non-cryptographic example.

### `05-index-choices-and-techniques.ipynb`
- Focuses on database performance, demonstrating the crucial role of indexes for text-based queries.
- Explains and creates the standard **B-Tree** index and its use cases with `LIKE`/`ILIKE`.
- Introduces **Full-Text Search** concepts (`to_tsvector`, `to_tsquery`).
- Implements advanced index types like **GIN** and **GiST** to dramatically accelerate full-text search queries.

---

## Key Takeaways ✨

1.  **Effective Data Generation:** SQL is not just for querying; it has powerful tools to generate large, structured datasets for testing and development.
2.  **Mastery of Text Manipulation:** Real-world data is messy. Knowing how to clean, parse, and format strings directly in the database is a highly efficient skill.
3.  **Encoding is Fundamental:** A solid grasp of **UTF-8** and how both the database and application layer (Python) handle it is essential for building modern, global applications.
4.  **Hashing is the Standard for Security:** Plaintext passwords or sensitive data are unacceptable. Using cryptographic extensions like **`pgcrypto`** is a fundamental security practice.
5.  **Indexes are Not Optional:** For any table of significant size, the difference between an indexed and unindexed query can be seconds versus hours. Choosing the right index type (**B-Tree** vs. **GIN**) for the query is a critical performance tuning skill.

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

`PostgreSQL` | `SQL` | `Text Manipulation` | `Data Generation` | `Character Sets` | `UTF-8` | `Hashing` | `pgcrypto` | `Database Indexing` | `B-Tree` | `GIN Index` | `Full-Text Search` | `Performance Tuning` | `Jupyter Notebook`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.*
