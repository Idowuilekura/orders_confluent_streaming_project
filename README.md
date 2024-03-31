# orders_confluent_streaming_project
A project that streams orders data from Confluent, reads the data with kafka, pushes the data to snowflake and implement a CDC to push the data to analytical postgres. The code is containerized inside a docker container and pushed to kubernetes to keep running and dbt is then used to create data warehouses 
