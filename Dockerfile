FROM python:3.11-slim-bookworm

ENV SNOWFLAKE_HOME=/app

WORKDIR /app

# COPY connections.toml /app/connections.toml
# COPY client.properties /app/client.properties

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt --no-cache-dir


COPY ./utils /app/utils

ENV PYTHONPATH=/app/utils/:$PYTHONPATH

COPY ./shopileft_src/consumer_shopileft.py /app/shopileft_src/consumer_shopileft.py
# COPY snowflake_connect.py /app/snowflake_connect.py 
# COPY confluent_data_loader.py /app/confluent_data_loader.py
# COPY main.py /app/main.py

# RUN echo ${PYTHONPATH}

ENTRYPOINT ["python", "shopileft_src/consumer_shopileft.py"]