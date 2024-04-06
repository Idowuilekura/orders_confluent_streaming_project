FROM python:3.11-slim-bookworm

ENV SNOWFLAKE_HOME=/app

WORKDIR /app

# COPY connections.toml /app/connections.toml
# COPY client.properties /app/client.properties

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt --no-cache-dir


COPY ./utils /app/utils
COPY ./consumer_conflu.py /app/consumer_conflu.py
# COPY snowflake_connect.py /app/snowflake_connect.py 
# COPY confluent_data_loader.py /app/confluent_data_loader.py
# COPY main.py /app/main.py

ENTRYPOINT ["python", "consumer_conflu.py"]