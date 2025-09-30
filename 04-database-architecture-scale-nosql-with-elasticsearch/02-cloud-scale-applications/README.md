# Cloud Scale Applications

This repository contains hands-on Jupyter notebooks built and documented by **Fahad Shah (1FahadShah)**. They represent my execution and learning journey through the **"PostgreSQL for Everybody" Specialization** offered by the **University of Michigan** on **Coursera**.

This Module covers the fundamental architectural patterns and technologies used to build modern, scalable, and resilient cloud-native applications. The notebooks explain the evolution from traditional architectures to the distributed systems that power today's largest web services.

---

## Notebooks Overview 📓

### `01-evolution-of-cloud-applications-and-nosql.ipynb`
- Traces the history from "Lift and Shift" (First Generation) to "Cloud-Native" (Second Generation) applications.
- Explains the database bottleneck that led to the rise of **NoSQL** and the **BASE** consistency model.
- Discusses how PostgreSQL reacted by evolving into a multi-model database with features like `JSONB`.

### `02-stateless-architecture-and-microservices.ipynb`
- Provides a deep dive into **stateless architecture** as the key enabler for horizontal scaling.
- Contrasts the traditional **Monolith** pattern with the modern **Microservices** architecture.
- Includes a detailed pros-and-cons comparison of monoliths vs. microservices.

### `03-decoupling-with-queues-and-object-storage.ipynb`
- Explains how to build resilient systems using **Message Queues** for asynchronous communication, preventing cascading failures.
- Details the best practice of offloading large files (images, videos) to **Object Storage** (like AWS S3) to keep the primary database lean and fast.

### `04-global-performance-with-caching-and-cdns.ipynb`
- Focuses on strategies for reducing latency for a global user base.
- Explains the role of **Content Delivery Networks (CDNs)** in caching static assets at edge locations close to users.
- Presents the full **hierarchy of caching**, from the user's browser all the way down to the database disk.

### `05-polyglot-persistence-the-modern-database-landscape.ipynb`
- Synthesizes all module concepts into the modern architectural pattern of **Polyglot Persistence**.
- Explains the "right tool for the right job" approach to using multiple database technologies (PostgreSQL, Redis, Elasticsearch, etc.) in a single system.
- Provides a detailed example of a cloud-native e-commerce architecture.

---

## Key Takeaways ✨

1.  **Statelessness Enables Scale:** A stateless application tier is the absolute prerequisite for effective horizontal scaling and high availability.
2.  **Microservices Provide Agility:** Breaking down a monolith into independent microservices allows for granular scaling, independent deployments, and improved fault tolerance.
3.  **Decouple for Resilience:** Asynchronous communication via **message queues** prevents cascading failures and allows components to scale independently.
4.  **Use the Right Storage for the Right Data:** Relational databases are for structured, transactional data. Large binary files belong in **object storage**.
5.  **Cache Aggressively at Every Layer:** The most effective way to improve performance is to answer a request as close to the user as possible, utilizing browser, **CDN**, and application caches.
6.  **Embrace Polyglot Persistence:** The modern "SQL vs. NoSQL" debate is over. The winning strategy is to use a hybrid of multiple specialized data stores, often with PostgreSQL at the core for transactional integrity.

---

## Setup Instructions 🛠️

1.  These notebooks are conceptual and written entirely in Markdown to explain architectural patterns.
2.  No special setup or code execution is required.

---

## Technologies / Tags

`Cloud Architecture` | `System Design` | `Microservices` | `Stateless` | `Message Queues` | `RabbitMQ` | `SQS` | `Object Storage` | `AWS S3` | `CDN` | `Caching` | `NoSQL` | `BASE` | `ACID` | `Polyglot Persistence` | `High Availability` | `Fault Tolerance`

---

*These notebooks are part of the PostgreSQL for Everybody Specialization, documented and adapted by Fahad Shah (1FahadShah) as part of his personal learning and execution journey.*
