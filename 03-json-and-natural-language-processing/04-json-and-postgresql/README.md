# JSON and PostgreSQL

This repository contains hands-on Jupyter notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.

This Module covers the end-to-end lifecycle of modern data. We start by understanding fundamental data interchange formats (JSON and XML), learn to manipulate them in an application layer with Python, store and query them efficiently in PostgreSQL using the `JSONB` data type, and finally, serve that data to the world through a web API.

---

## Notebooks Overview 📓

### `01-data-formats-json-vs-xml.ipynb`
- Provides a foundational understanding of data interchange formats.
- Compares the syntax, structure, pros, and cons of **XML (Extensible Markup Language)** and **JSON (JavaScript Object Notation)**.
- Includes a side-by-side comparison, explaining why JSON has become the dominant standard for web APIs.

### `02-working-with-json-in-python.ipynb`
- A practical guide to Python's built-in **`json` library**.
- Covers **Serialization**: Converting Python objects (dictionaries, lists) into JSON strings (`dumps`) and files (`dump`).
- Covers **Deserialization**: Parsing JSON strings (`loads`) and files (`load`) back into native Python objects.

### `03-storing-and-querying-json-in-postgresql.ipynb`
- Dives into PostgreSQL's powerful features for handling schemaless data.
- Explains the critical difference between the `JSON` and **`JSONB`** data types.
- Demonstrates querying with path operators (`->`, `->>`, `#>>`) and the powerful containment operator (`@>`).
- Proves the necessity of using a **GIN index** for high-performance `JSONB` queries.

### `04-building-a-simple-json-api-with-python-and-postgresql.ipynb`
- A capstone project that ties all concepts together by building a functional web API.
- Uses the **Flask** micro-framework to create API endpoints.
- Connects to PostgreSQL using **`psycopg2`** to fetch `JSONB` data.
- Serves the database results as a standard JSON response, completing the full-stack pipeline.

---

## Key Takeaways ✨

1.  **JSON is the Lingua Franca of APIs:** Its lightweight syntax and direct mapping to native data structures in most languages make it the ideal choice for modern web services.
2.  **Master Python's `json` Library:** The ability to serialize (Python to JSON) and deserialize (JSON to Python) is a fundamental skill for any developer working with APIs or web data.
3.  **Always Prefer `JSONB` in PostgreSQL:** For any serious application, the decomposed, binary, and indexable `JSONB` data type is vastly superior to the plain text `JSON` type.
4.  **GIN Indexes are Essential for `JSONB` Performance:** To efficiently query `JSONB` data using operators like containment (`@>`), a **GIN index** is not optional—it's a requirement for scalability.
5.  **The Full Stack Connects:** A complete application involves a client consuming a **JSON API**, which is powered by an application server (like **Flask**) that in turn queries a database (like **PostgreSQL**) to retrieve and serve data.

---

## Setup Instructions 🛠️

1.  Ensure you have a local PostgreSQL instance running with a database created (e.g., `people`).
2.  Install the required Python packages:
    ```bash
    pip install psycopg2-binary pandas Flask
    ```
3.  For the SQL notebooks, load the `ipython-sql` extension and connect to your database.
4.  For the Python notebooks, update the connection variables to match your local database credentials.
5.  Run each notebook **cell-by-cell** to replicate all examples and exercises.

---

## Technologies / Tags

`PostgreSQL` | `Python` | `JSON` | `JSONB` | `XML` | `API` | `Flask` | `Web Development` | `psycopg2` | `GIN Index` | `Database Design` | `Data Interchange Formats` | `Backend Development`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.*
