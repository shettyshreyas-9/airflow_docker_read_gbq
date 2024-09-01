# Use the official Python image as the base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /opt/airflow

# Copy the current directory contents into the container
COPY . .

# Install any needed Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]
