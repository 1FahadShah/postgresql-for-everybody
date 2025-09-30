# PostgreSQL for Everybody - University of Michigan
This repository represents the complete execution journey and portfolio of **Fahad Shah ([1FahadShah](https://github.com/1FahadShah))** through the entire **[PostgreSQL for Everybody Specialization](https://www.coursera.org/specializations/postgresql-for-everybody)** offered by the **University of Michigan** on Coursera.

It contains a meticulously documented collection of hands-on Jupyter notebooks that cover a wide spectrum of database engineering. The curriculum progresses from foundational SQL and relational data modeling, through advanced application integration with Python, to high-level system architecture, scalability patterns, and the integration of NoSQL technologies like Elasticsearch.

---
## ✨ Specialization Overview
This four-course journey provides a comprehensive, practical education in modern database systems, designed to build skills for backend development, data engineering, and system architecture.

* **[Course 1: Database Design and Basic SQL in PostgreSQL](#-course-1--database-design-and-basic-sql-in-postgresql)**: The fundamentals of relational databases, data modeling, and core SQL.
* **[Course 2: Intermediate PostgreSQL](#-course-2--intermediate-postgresql)**: A deep dive into advanced SQL techniques, text processing, and database optimization.
* **[Course 3: JSON and Natural Language Processing in PostgreSQL](#-course-3--json-and-natural-language-processing-in-postgresql)**: Bridging the database with the application layer, handling semi-structured data, and building APIs.
* **[Course 4: Database Architecture, Scale, and NoSQL with Elasticsearch](#-course-4--database-architecture-scale-and-nosql-with-elasticsearch)**: Exploring high-level architectural patterns for building scalable, resilient, and high-performance systems.

---
## 📚 Course Summaries & Notebooks

### 🎓 Course 1: Database Design and Basic SQL in PostgreSQL
[![Coursera Certificate](https://img.shields.io/badge/Coursera-Certificate-blue?logo=coursera)](https://www.coursera.org/account/accomplishments/verify/DA030CWS5KNC)

This course lays the groundwork for the entire specialization, covering the essential concepts of relational database design and the core SQL commands required for any database-driven application.

| Module | Notebook(s) | Highlights |
| :--- | :--- | :--- |
| **Getting Started** | `01-getting-started-with-postgresql.ipynb` | Installation, user/database creation, `psql` usage, basic DDL/DML. |
| **Single Table SQL** | `01-working-with-sql.ipynb`<br>`02-datatypes-in-postgresql.ipynb`<br>`03-indexes-in-postgresql.ipynb` | Full CRUD operations, filtering (`WHERE`), sorting (`ORDER BY`), PostgreSQL data types, and core indexing strategies (B-Tree, GIN). |
| **One-to-Many Models**| `01-relational-database-design.ipynb`<br>`02-database-normalization.ipynb`<br>`03-create-table-insert-data-use-join.ipynb` | Relational modeling, normalization to 3NF, primary & foreign keys, `INNER JOIN`, and `LEFT JOIN`. |
| **Many-to-Many Models**| `many-to-many-data-models.ipynb` | Designing junction tables with composite keys to model many-to-many relationships and performing three-way `JOIN`s. |

<br>

### 🎓 Course 2: Intermediate PostgreSQL
[![Coursera Certificate](https://img.shields.io/badge/Coursera-Certificate-blue?logo=coursera)](https://www.coursera.org/account/accomplishments/verify/WXWIF14TTCCU)

Building on the basics, this course explores the advanced SQL techniques and internal features of PostgreSQL that are essential for building robust, real-world applications and optimizing performance.

| Module | Notebook(s) | Highlights |
| :--- | :--- | :--- |
| **SQL Techniques** | `01-alter-table-schema.ipynb`<br>`02-dates.ipynb`<br>`03-distinct-group-by.ipynb`<br>`04-subqueries.ipynb` | Schema evolution with `ALTER TABLE`, date/time functions, advanced aggregation (`GROUP BY`, `HAVING`), and complex subqueries. |
| **Business Applications** | `01-simple-business.ipynb`<br>`02-advanced-queries-and-subqueries.ipynb`<br>`03-transactions-concurrency-and-procedures.ipynb` | Practical data modeling, transaction management (`BEGIN`, `COMMIT`, `ROLLBACK`), concurrency control, stored procedures, and triggers. |
| **Text & Hashing** | `01-text-in-databases.ipynb`<br>`02-text-functions.ipynb`<br>`03-character-sets.ipynb`<br>`04-inside-hashes.ipynb`<br>`05-index-choices-and-techniques.ipynb` | Advanced text manipulation, character sets (`UTF-8`), cryptographic hashing with `pgcrypto`, and using GIN/GiST indexes for Full-Text Search. |
| **Regular Expressions** | `01-regular-expressions.ipynb`<br>`02-regular-expressions-quick-guide.ipynb` | Mastering pattern matching (`~`, `~*`) and complex text validation directly within the database using the SQL regular expression engine. |

<br>

### 🎓 Course 3: JSON and Natural Language Processing in PostgreSQL
[![Coursera Certificate](https://img.shields.io/badge/Coursera-Certificate-blue?logo=coursera)](https://www.coursera.org/account/accomplishments/verify/VD8ZWISGEXQX)

This course bridges the gap between the database and the application layer, covering modern data formats, application integration with Python, and building functional web APIs.

| Module | Notebook(s) | Highlights |
| :--- | :--- | :--- |
| **Natural Language** | `01-allocating-rows-to-blocks-in-postgresql.ipynb` to `05-sql-natural-language.ipynb` | Database internals (`ctid`), Full-Text Search (FTS) engine, `tsvector`, `tsquery`, result ranking (`ts_rank`), and highlighting (`ts_headline`). |
| **Inverted Indexes** | `01-gin-based-inverted-index.ipynb` to `04-gin-tsvector-index.ipynb` | Deep dive into GIN indexes, FTS configurations for different languages, advanced `tsquery` operators, and production FTS with triggers. |
| **Python & PostgreSQL**| `01-connecting-to-postgresql-with-psycopg2.ipynb` to `04-advanced-python-postgresql-integration.ipynb` | Python integration with `psycopg2`, transaction control, **SQL injection prevention**, Pandas DataFrame integration, and connection pooling. |
| **JSON & APIs** | `01-data-formats-json-vs-xml.ipynb` to `04-building-a-simple-json-api-with-python-and-postgresql.ipynb` | Data formats (JSON vs. XML), PostgreSQL's `JSONB` data type, querying JSON (`->>`, `@>`), GIN indexing for `JSONB`, and building a **Flask** API. |

<br>

### 🎓 Course 4: Database Architecture, Scale, and NoSQL with Elasticsearch
[![Coursera Certificate](https://img.shields.io/badge/Coursera-Certificate-blue?logo=coursera)](https://www.coursera.org/account/accomplishments/verify/YOUR-CERTIFICATE-ID-HERE)

The final course moves beyond a single database to cover the high-level architectural patterns required to build scalable, resilient, and high-performance distributed systems.

| Module | Notebook(s) | Highlights |
| :--- | :--- | :--- |
| **Scaling Databases** | `01-scaling-up-vs-scaling-out.ipynb` to `04-caching-strategies-to-reduce-database-load.ipynb` | **Vertical vs. Horizontal Scaling**, database **replication** for read scalability, **sharding** for write scalability, and **caching** strategies. |
| **Cloud Scale Apps**| `01-evolution-of-cloud-applications-and-nosql.ipynb` to `05-polyglot-persistence-the-modern-database-landscape.ipynb`| **Stateless architecture**, **microservices**, decoupling with **message queues**, offloading files to **object storage**, and global caching with **CDNs**. |
| **Elasticsearch** | `01-introduction-to-elasticsearch-and-rest-api.ipynb` to `04-elasticsearch-and-postgresql-a-hybrid-architecture.ipynb` | Introduction to **Elasticsearch**, its REST API, the Query DSL, Python client integration, and designing a hybrid architecture with PostgreSQL. |

---
## 🚀 Core Skills & Technologies Master List
`ACID` | `API` | `ALTER TABLE` | `Arrays` | `AWS S3` | `B-Tree` | `Backend Development` | `BASE` | `Business Intelligence` | `Caching` | `CAP Theorem` | `CDN` | `Character Sets` | `Cloud Architecture` | `Composite Keys` | `Connection Pooling` | `CRUD` | `curl` | `Data Interchange Formats` | `Data Modeling` | `Database Administration` | `Database Architecture` | `Database Design` | `Database Indexing` | `Database Internals` | `Database Replication` | `DataFrames` | `Datatypes` | `DDL` | `DML` | `Elasticsearch` | `Fault Tolerance` | `Flask` | `Full-Text Search` | `FTS` | `GIN Index` | `GiST Index` | `Hashing` | `High Availability` | `Horizontal Scaling` | `Inverted Index` | `JOINs` | `JSON` | `JSONB` | `Junction Table` | `Jupyter Notebook` | `Many-to-Many` | `Message Queues` | `Microservices` | `Natural Language Processing` | `NLP` | `NoSQL` | `Normalization` | `Object Storage` | `Pandas` | `Performance Tuning` | `pgcrypto` | `phraseto_tsquery` | `plainto_tsquery` | `PL/pgSQL` | `Polyglot Persistence` | `PostgreSQL` | `psql` | `psycopg2` | `Python` | `Query DSL` | `RabbitMQ` | `Redis` | `Regular Expressions` | `Relational Databases` | `REST API` | `Scalability` | `Search Engine` | `Sharding` | `SQL` | `SQL Injection` | `SQS` | `Stateless` | `Stored Procedures` | `Subqueries` | `System Design` | `Text Manipulation` | `Transactions` | `Triggers` | `tsquery` | `tsvector` | `UTF-8` | `Vertical Scaling` | `Web Development` | `XML`

---
## Portfolio Statement
This repository represents a comprehensive, hands-on execution of the entire PostgreSQL for Everybody Specialization. It showcases not just theoretical knowledge, but the practical application of concepts ranging from foundational SQL to complex, cloud-scale system design. Each notebook is a testament to a deep, practical understanding of modern data engineering and backend development principles, forming a complete portfolio of my skills in this domain.

*Documented by **Fahad Shah (1FahadShah)***
