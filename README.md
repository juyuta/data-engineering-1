# Realtime Data Streaming | End-to-End Data Engineering Project

## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [What was done](#what-was-done)
- [Technologies](#technologies)
- [Getting Started](#getting-started)

## Introduction

My first built of an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. Everything is containerized using Docker for ease of deployment and scalability.

## System Architecture

![System Architecture](https://github.com/juyuta/data-engineering-1/blob/main/Data%20engineering%20architecture.png)

The project is designed with the following components:

- **Data Source**: We use `randomuser.me` API to generate random user data for our pipeline.
- **Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
- **Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
- **Apache Spark**: For data processing with its master and worker nodes.
- **Cassandra**: Where the processed data will be stored.

## What was done

- Setting up a data pipeline with Apache Airflow
- Real-time data streaming with Apache Kafka
- Distributed synchronization with Apache Zookeeper
- Data processing techniques with Apache Spark
- Data storage solutions with Cassandra and PostgreSQL
- Containerizing your entire data engineering setup with Docker

## File Structures

```
root/ 
├──  dags/ 
│    └──  kafka-stream.py 
├──  script/ 
│    ├── entrypoint.sh
│    └── requirements.txt
├──  docker-compose.yml
├──  README.md
├──  requirements.txt
└──  spark_stream.py
```

## Technologies

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker

## Getting Started

1. Clone the repository:
    ```
    git clone https://github.com/juyuta/data-engineering-1.git
    ```

2. Navigate to the project directory:
    ```
    cd data-engineering-1
    ```

3. Run Docker Compose to spin up the services:
    ```
    docker-compose up -d
    ```

4. Create & Activate the virtal environment with all the dependencies to run .py files:
   ```
   python venv venv
   venv\Scripts\activate.bat
   ```
