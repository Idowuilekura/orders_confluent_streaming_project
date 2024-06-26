# Shopileft Orders Streaming Project
Overview
The Confluent Data Streaming Project is a comprehensive data pipeline solution designed to stream orders data from Confluent, process it with Kafka, and then load it into Snowflake for storage and analysis. Additionally, a Change Data Capture (CDC) mechanism is implemented to synchronize the data with an analytical Snowflake database table in real-time. The entire solution is containerized using Docker and deployed on Kubernetes for scalability and fault tolerance. Data transformation and warehousing are managed using dbt (data build tool). The kafka cluster is monitored with datadog to ensure the process runs as expected. 

Components
1. Confluent:
Purpose: Source of orders data.
Description: Confluent provides real-time streaming data platform built on Apache Kafka. It acts as the source for streaming order data.
2. Kafka:
Purpose: Processing and streaming data.
Description: Kafka reads and processes orders data streamed from Confluent. It acts as the intermediary for data processing and transformation.
3. Snowflake:
Purpose: Data warehousing and storage.
Description: Snowflake is a cloud-based data warehousing platform that stores and analyses structured and semi-structured data. Orders data processed by Kafka is loaded into Snowflake for storage and further analysis.
4. Analytical Postgres:
Purpose: Real-time analytics.
Description: The Analytical Postgres database is used for real-time analytics and reporting. Data from Snowflake is synchronized with the analytical Postgres database using CDC mechanisms to provide up-to-date insights.
5. Docker:
Purpose: Containerization.
Description: The entire project, including the code for processing order data, is containerized using Docker. This ensures consistency across environments and facilitates easy deployment.
6. Kubernetes:
Purpose: Orchestration and deployment.
Description: Kubernetes orchestrates and manages the deployment of Docker containers. It ensures the data streaming solution's high availability, scalability, and fault tolerance.
7. Github Actions:
Purpose: For continuous integration and deployment of the codebase
Deployment
The project is deployed on Kubernetes for continuous operation. Docker containers containing the application code are deployed as Kubernetes pods, ensuring the availability and scalability of the data streaming solution, and GithubActions is used for continuous integration and deployment. 

Usage
Setup Confluent: Configure Confluent to stream order data.
Deploy Kafka: Deploy Kafka to process and stream the order data.
Load Data into Snowflake: Load the processed orders data into Snowflake for storage and analysis.
Implement CDC to Analytical Postgres: Implement Change Data Capture (CDC) to synchronize the data with an analytical Postgres database for real-time analytics.
Containerize with Docker: Containerize the application code using Docker for consistency and portability.
Deploy on Kubernetes: Deploy the Docker containers for orchestration and management.
Use dbt for Data Warehousing: Use dbt to create and manage data warehouses, enabling efficient data transformation and analysis.

## Data Architecture 
![image](https://github.com/Idowuilekura/orders_confluent_streaming_project/assets/38056084/c33b26db-3245-431a-9f73-76ed4806888d)

### Data Dog Kafka Cluster Monitoring
![image](https://github.com/Idowuilekura/orders_confluent_streaming_project/assets/38056084/723494aa-b671-48ee-ad6d-9d5793abfee1)


