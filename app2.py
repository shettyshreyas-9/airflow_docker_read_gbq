from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import subprocess
import sys

app = FastAPI()

def run_docker_commands():
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

@app.get("/")
def start_services(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_docker_commands)
    return {"message": "Docker commands are being executed in the background"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
