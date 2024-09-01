# app.py
import subprocess
import sys
import os
import platform

import subprocess
import platform

def install_docker():
    if platform.system() == "Linux":
        # Update package list and install dependencies
        subprocess.run("apt-get update", shell=True, check=True)
        subprocess.run("apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release", shell=True, check=True)
        
        # Download Docker’s official GPG key
        subprocess.run("curl -fsSL -k https://download.docker.com/linux/debian/gpg | apt-key add -", shell=True, check=True)
        
        # Add the GPG key
        subprocess.run("apt-key add /tmp/docker.gpg", shell=True, check=True)
        
        # Set up the Docker repository
        subprocess.run('sh -c "echo deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable > /etc/apt/sources.list.d/docker.list"', shell=True, check=True)
        
        # Update package list and install Docker
        subprocess.run("apt-get update", shell=True, check=True)
        subprocess.run("apt-get install -y docker-ce docker-ce-cli containerd.io", shell=True, check=True)
        
        # Start Docker service using systemctl
        subprocess.run("systemctl start docker", shell=True, check=True)
        
        # Install Docker Compose
        subprocess.run("curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose", shell=True, check=True)
        subprocess.run("chmod +x /usr/local/bin/docker-compose", shell=True, check=True)
        subprocess.run("ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose", shell=True, check=True)
    else:
        print("This script is intended to run on Linux systems only.")


def run_docker_compose():
    # setup_airflow_logs_directory()

    install_docker()
    print ('\n','\n', 'Stage Change' ,'\n','\n')

    try:
        # Run docker-compose up --build to build and start services
        subprocess.run("docker-compose up --build", shell=True, check=True)
        print ('\n','\n', 'Stage Change' ,'\n','\n')

        # Run docker-compose up airflow-init to initialize Airflow
        subprocess.run("docker-compose up airflow-init", shell=True, check=True)
        print ('\n','\n', 'Stage Change' ,'\n','\n')

        # Inform the user that services are starting
        print("Airflow webserver and services are starting...")
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running docker-compose: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_docker_compose()
