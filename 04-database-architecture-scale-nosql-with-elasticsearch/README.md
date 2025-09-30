# Course 4: Database Architecture, Scale, and NoSQL with Elasticsearch
[![Coursera Certificate](https://img.shields.io/badge/Coursera-Certificate-blue?logo=coursera)](https://www.coursera.org/account/accomplishments/verify/YOUR-CERTIFICATE-ID-HERE)

This repository contains hands-on Jupyter notebooks built and documented by **Fahad Shah (1FahadShah)**. It represents my personal learning journey and practical solutions for **[Course 4: Database Architecture, Scale, and NoSQL with Elasticsearch](https://www.coursera.org/learn/database-architecture-scale-nosql)** from the **PostgreSQL for Everybody Specialization** offered by the **University of Michigan** on Coursera.

This course moves beyond a single database to cover high-level architectural patterns for building scalable, resilient, and high-performance systems. It explores fundamental scaling strategies, cloud-native application design, and the integration of specialized NoSQL systems like Elasticsearch.

---

## 📚 Course Structure

This course consists of **three main modules**, each documented with conceptual notebooks that explain modern system design principles.

| Module      | Notebook(s)                                                                                                                                                                                                                                                             | Key Topics Covered                                                                                                           |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| **Module&nbsp;1** | `01-scaling-up-vs-scaling-out.ipynb`<br>`02-database-replication-for-read-scalability.ipynb`<br>`03-sharding-for-write-scalability.ipynb`<br>`04-caching-strategies-to-reduce-database-load.ipynb`                                                                      | Vertical vs. Horizontal Scaling, Database Replication for read scalability, Sharding for write scalability, and Caching strategies. |
| **Module&nbsp;2** | `01-evolution-of-cloud-applications-and-nosql.ipynb`<br>`02-stateless-architecture-and-microservices.ipynb`<br>`03-decoupling-with-queues-and-object-storage.ipynb`<br>`04-global-performance-with-caching-and-cdns.ipynb`<br>`05-polyglot-persistence-the-modern-database-landscape.ipynb` | Cloud-native architecture, statelessness, microservices, message queues, object storage, CDNs, and Polyglot Persistence.      |
| **Module&nbsp;3** | `01-introduction-to-elasticsearch-and-rest-api.ipynb`<br>`02-deep-dive-into-elasticsearch-search-and-dsl.ipynb`<br>`03-programming-elasticsearch-with-python-and-demos.ipynb`<br>`04-elasticsearch-and-postgresql-a-hybrid-architecture.ipynb`                                | Core Elasticsearch concepts, REST API interaction, the Query DSL, programming with the Python client, and hybrid architectures with PostgreSQL. |

---

## 📓 Notebook Overviews

### 1. Scaling Databases
**Highlights:**
* **Scale Up vs. Scale Out**: Understanding the fundamental trade-offs between making one server more powerful (vertical) and adding more servers (horizontal).
* **Replication for Reads**: Using a Primary-Replica architecture to handle high-volume read traffic.
* **Sharding for Writes**: Exploring the complex but powerful technique of sharding to scale write-heavy workloads.
* **Caching is King**: Implementing caching strategies as the most effective first step to reduce database load.

### 2. Cloud Scale Applications
**Highlights:**
* **Stateless Architecture**: Learning why statelessness is the absolute prerequisite for effective horizontal scaling and high availability.
* **Microservices**: Contrasting the monolith and microservice patterns to build agile and resilient systems.
* **Decoupling Components**: Using Message Queues for asynchronous communication and Object Storage for large files to build robust applications.
* **Global Performance**: Leveraging Content Delivery Networks (CDNs) and a multi-layered caching strategy to reduce latency for users worldwide.
* **Polyglot Persistence**: Embracing the modern "right tool for the right job" approach by using multiple, specialized data stores in a single application.

### 3. Elasticsearch
**Highlights:**
* **Search Engine Fundamentals**: An introduction to Elasticsearch as a dedicated, document-oriented search engine and its core concepts.
* **REST API and Query DSL**: Interacting with Elasticsearch via its API and building complex, fine-tuned search queries with its powerful JSON-based Query DSL.
* **Application Integration**: Using the official Python client to programmatically index data and perform searches.
* **Hybrid Architecture**: Designing a robust "Search-as-a-Sidecar" pattern, using PostgreSQL as the source of truth and Elasticsearch as the powerful, secondary search index.

---

### 🚀 Technologies / Tags
`System Design` | `Database Architecture` | `Cloud Architecture` | `Scalability` | `High Availability` | `Microservices` | `Stateless` | `PostgreSQL` | `Elasticsearch` | `NoSQL` | `Polyglot Persistence` | `Database Replication` | `Sharding` | `Caching` | `Redis` | `CDN` | `Message Queues` | `Object Storage` | `AWS S3`| `REST API` | `Query DSL` | `Python`

---

This repository is part of my Execution Journey through the PostgreSQL for Everybody Specialization, documented by **1FahadShah**. It serves as a practical portfolio showcasing my understanding of advanced database architecture, scaling patterns, and the integration of NoSQL technologies.
