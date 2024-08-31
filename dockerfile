# Dockerfile
FROM apache/airflow:2.10.0

# USER root
# RUN pip install --no-cache-dir google-cloud-bigquery
# USER airflow

# Dockerfile

USER airflow
# USER root
RUN mkdir -p /opt/airflow/logs/scheduler && \
    chown -R airflow:airflow /opt/airflow/logs/scheduler

USER airflow

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW_UID=50000
ENV AIRFLOW_GID=50000



# Copy the application files
COPY app.py /opt/airflow/app.py
COPY requirements.txt /opt/airflow/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

EXPOSE 8080

# Set the working directory
WORKDIR /opt/airflow

# Define the command to run the application
CMD ["python", "app.py"]
