# One-to-Many Data Models

## Relational Design, Normalization, and JOINs

This repository contains **hands-on PostgreSQL notebooks** built and documented by **Fahad Shah (1FahadShah)**. They represent my personal learning journey through the *"PostgreSQL for Everybody"* Specialization offered by the University of Michigan on Coursera.

This module focuses on the complete workflow of relational database design: from conceptual modeling and normalization to practical implementation and querying with `JOIN`s.

---

## Notebooks Overview 📓

* **`01-relational-database-design.ipynb`** → Covers the core concepts of relational modeling, including entities, attributes, and relationships using Primary and Foreign Keys.
* **`02-database-normalization.ipynb`** → A step-by-step tutorial on applying 1NF, 2NF, and 3NF to transform a "flat" table into a clean, multi-table schema.
* **`03-create-table-insert-data-use-join.ipynb`** → A practical guide to building tables, inserting data, and querying across them using various `JOIN` operations.

---

## Highlights From the Notebooks ✨

### 1. The Normalization Process (0NF → 3NF)
The notebooks demonstrate how to take a messy, un-normalized table with repeated data...

**Un-Normalized Data (0NF):**
| track_title        | track_len | artist_name  | album_title     | genre_name |
| :----------------- | :-------- | :----------- | :-------------- | :--------- |
| Black Dog          | 296       | Led Zeppelin | Led Zeppelin IV | Rock       |
| Stairway to Heaven | 482       | Led Zeppelin | Led Zeppelin IV | Rock       |

...and apply the rules of normalization to create a clean, efficient, and robust multi-table schema.

**Final Normalized Schema (3NF):**
```sql
CREATE TABLE artist ( ... );
CREATE TABLE genre ( ... );
CREATE TABLE album ( ... );
CREATE TABLE track ( ... );

*(Full schema and step-by-step process are detailed in the `02-database-normalization.ipynb` notebook.)*
```
### 2. Practical JOIN Queries
Once the schema is built and populated, the notebooks showcase powerful `JOIN` queries to retrieve meaningful data.

**Example: List Albums with Track Counts (`LEFT JOIN`)**
```sql
SELECT
    a.title AS album,
    ar.name AS artist,
    COUNT(t.id) AS track_count
FROM album AS a
JOIN artist AS ar ON a.artist_id = ar.id
LEFT JOIN track AS t ON a.id = t.album_id
GROUP BY a.id, ar.name
ORDER BY a.title;
```
*(More query examples, including INNER JOIN, GROUP BY, and WHERE clauses, are in the `03-create-table-insert-data-use-join.ipynb` notebook.)*

---

## Setup Instructions 🛠️

1. Install PostgreSQL and create a database (e.g., `music`).

2. Install the necessary Python packages for Jupyter integration:

```bash
pip install ipython-sql psycopg2-binary "prettytable<3.0.0"
```
3. Load the SQL extension and connect to your database at the start of your notebook:

```python
%load_ext sql
%sql postgresql://username:password@localhost:5432/music
```
4. Run each notebook cell-by-cell to replicate the examples.

---

## Technologies / Tags

`PostgreSQL` | `SQL` | `Relational Databases` | 'One-to-Many' | `Normalization` | `1NF` | `2NF` | `3NF` | `JOINs` | `Jupyter Notebook` | `Database Design`

