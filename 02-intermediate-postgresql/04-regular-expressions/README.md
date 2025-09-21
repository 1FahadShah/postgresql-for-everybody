# Regular Expressions

This repository contains hands-on PostgreSQL notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.

This Module provides a comprehensive introduction to **Regular Expressions (Regex)**, a powerful and essential tool for advanced text processing and pattern matching directly within the database.

---

## Notebooks Overview 📓

### `01-regular-expressions.ipynb`
- A detailed, step-by-step tutorial on using regular expressions in PostgreSQL.
- Introduces the core pattern matching operators `~` (case-sensitive) and `~*` (case-insensitive).
- Covers fundamental building blocks: **anchors** (`^`, `$`), **character classes** (`[]`, `.`), and **quantifiers** (`*`, `+`, `?`).
- Explains how to build complex patterns using **grouping** `()` and **alternation** `|`.
- Provides practical examples for finding specific patterns in textual data.

### `02-regular-expressions-quick-guide.ipynb`
- Serves as a concise "cheat sheet" for quick reference and review.
- Features a well-formatted markdown table summarizing all key regex metacharacters and their functions.
- Includes a section with ready-to-use patterns for common tasks like validating emails and dates.
- Briefly demonstrates the use of regex in powerful SQL functions like `SUBSTRING` and `REGEXP_REPLACE`.

---

## Key Takeaways ✨

1.  **Regex is a Universal Tool:** The core concepts of regular expressions learned here are applicable not just in SQL but across many programming languages and tools.
2.  **Pattern Matching is Powerful:** Regular expressions allow you to validate data formats, extract specific information, and perform complex searches that go far beyond simple `LIKE` clauses.
3.  **Core Components are Key:** Mastering the fundamental building blocks (anchors, quantifiers, classes) allows you to construct patterns for almost any text-processing challenge.
4.  **PostgreSQL Integration is Seamless:** PostgreSQL provides excellent, built-in support for regular expressions, making it a powerful tool for data cleaning and analysis at the database level.

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

`PostgreSQL` | `SQL` | `Regular Expressions` | `Regex` | `Pattern Matching` | `Text Processing` | `Data Cleaning` | `Data Validation` | `Jupyter Notebook`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.*
