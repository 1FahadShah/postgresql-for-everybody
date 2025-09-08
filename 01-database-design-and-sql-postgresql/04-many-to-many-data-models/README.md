# Many-to-Many Data Models

This repository contains the hands-on notebook, built and documented by **Fahad Shah (1FahadShah)**. It represents my personal learning journey through the *"PostgreSQL for Everybody"* Specialization offered by the University of Michigan on Coursera.

This module focuses on modeling and querying complex, real-world **many-to-many relationships** using a three-table "junction" design.

---

## Notebook Overview 📓

### `many-to-many-data-models.ipynb`
A comprehensive guide to many-to-many relationships using a classic student enrollment scenario.
-   Explains the core concept and the necessity of a **junction table**.
-   Demonstrates how to `CREATE` the three required tables with proper foreign keys and a composite primary key.
-   Provides examples of `INSERT`ing data into the schema.
-   Showcases how to use **three-way `JOIN`s** to retrieve meaningful data.

---

## Highlights From the Notebook ✨

This notebook provides a complete walkthrough of designing and implementing a many-to-many data model.

#### 1. The Junction Table Schema
The core of a many-to-many model is the three-table design. The `enrollment` table serves as the "junction" or "linking" table that connects students and courses.
```sql
-- Main tables
CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL UNIQUE
);

CREATE TABLE course (
    id SERIAL PRIMARY KEY,
    title VARCHAR(128) NOT NULL UNIQUE
);

-- The Junction Table
CREATE TABLE enrollment (
    student_id INTEGER REFERENCES student(id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES course(id) ON DELETE CASCADE,
    role INTEGER,
    PRIMARY KEY (student_id, course_id)
);
```
#### 2. Querying with Three-Way `JOIN`s
Once the data is linked, we can run powerful queries that join all three tables to answer complex questions.

```sql
-- Count the number of students in each course
SELECT
    c.title,
    COUNT(s.id) AS num_students
FROM course AS c
JOIN enrollment AS e ON c.id = e.course_id
JOIN student AS s ON e.student_id = s.id
GROUP BY c.title;
```
---

## Setup Instructions 🛠️
1.  Install PostgreSQL and create a database (e.g., `roster` or `school`).
2.  Install the necessary Python packages for Jupyter integration:
    ```bash
    pip install ipython-sql psycopg2-binary "prettytable<3.0.0"
    ```
3.  Load the SQL extension and connect to your database at the start of your notebook:
    ```python
    %load_ext sql
    %sql postgresql://username:password@localhost:5432/school
    ```
4.  Run each notebook cell-by-cell to replicate the examples.

---

## Technologies / Tags
`PostgreSQL` | `SQL` | `Many-to-Many` | `Junction Table` | `Composite Keys` | `Database Design` | `JOINs` | `Jupyter Notebook`


*This notebook is part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning journey.*
