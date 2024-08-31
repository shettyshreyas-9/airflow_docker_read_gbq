# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /opt/airflow

# Copy the current directory contents into the container
COPY . .

# Install pip requirements
RUN pip install --no-cache-dir -r requirements.txt

# Install Docker Compose
RUN apt-get update && \
    apt-get install -y curl && \
    curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]
