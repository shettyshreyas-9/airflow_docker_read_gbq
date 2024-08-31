# app.py
import subprocess
import sys
import os

def setup_airflow_logs_directory(log_directory="/opt/airflow/logs/scheduler"):
    try:
        os.makedirs(log_directory, exist_ok=True)
        os.chmod(log_directory, 0o775)  # Adjust permissions
    except PermissionError:
        print(f"PermissionError: Unable to create or set permissions for {log_directory}")
        # Handle by adjusting the log directory or exiting
        exit(1)

def run_docker_compose():
    # setup_airflow_logs_directory()
    try:
        # Run docker-compose up --build to build and start services
        subprocess.run(["docker-compose", "up", "--build"], check=True)
        
        # Run docker-compose up airflow-init to initialize Airflow
        subprocess.run(["docker-compose", "up", "airflow-init"], check=True)
        
        # Inform the user that services are starting
        print("Airflow webserver and services are starting...")
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running docker-compose: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_docker_compose()
