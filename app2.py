import subprocess
import os

def install_docker():
    try:
        print("Installing Docker...")
        subprocess.run(
            ["apt-get", "update"], check=True
        )
        subprocess.run(
            ["apt-get", "install", "-y", "apt-transport-https", "ca-certificates", "curl", "gnupg-agent", "software-properties-common"],
            check=True
        )
        subprocess.run(
            ["curl", "-fsSL", "https://download.docker.com/linux/debian/gpg", "|", "apt-key", "add", "-"],
            check=True,
            shell=True
        )
        subprocess.run(
            ["add-apt-repository", "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"],
            check=True
        )
        subprocess.run(
            ["apt-get", "update"], check=True
        )
        subprocess.run(
            ["apt-get", "install", "-y", "docker-ce", "docker-ce-cli", "containerd.io"],
            check=True
        )
        print("Docker installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Docker: {e}")

def install_docker_compose():
    try:
        print("Installing Docker Compose...")
        subprocess.run(
            ["curl", "-L", "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)", "-o", "/usr/local/bin/docker-compose"],
            check=True
        )
        subprocess.run(
            ["chmod", "+x", "/usr/local/bin/docker-compose"], check=True
        )
        subprocess.run(
            ["ln", "-s", "/usr/local/bin/docker-compose", "/usr/bin/docker-compose"],
            check=True
        )
        print("Docker Compose installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Docker Compose: {e}")

def check_and_install():
    try:
        # Check if Docker is installed
        subprocess.run(["docker", "--version"], check=True)
        install_docker()
    except subprocess.CalledProcessError:
        install_docker()

    try:
        # Check if Docker Compose is installed
        subprocess.run(["docker-compose", "--version"], check=True)
        install_docker_compose()
    except subprocess.CalledProcessError:
        install_docker_compose()

def run_docker_compose():
    print("Running Docker Compose...")
    subprocess.run(["docker-compose", "up", "--build"], check=True)

if __name__ == "__main__":
    check_and_install()
    run_docker_compose()
