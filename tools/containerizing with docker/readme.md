# Guess the Number Game - Dockerized

A step-by-step guide to containerizing a simple Python game using Docker.

## Prerequisites
- Docker installed on your machine.
  - [Docker Desktop for Windows](https://docs.docker.com/desktop/windows/install/)
  - [Docker Desktop for macOS](https://docs.docker.com/desktop/mac/install/)
  - [Docker Engine for Linux](https://docs.docker.com/engine/install/)

## Steps to Set Up

### Step 1: Set Up the Project Directory
1. Create a directory for your project:

    ```bash
    mkdir guess-the-number
    cd guess-the-number
    ```

2. Save your game code in a file named `game.py`.

### Step 2: Write a Requirements File (Optional)
This game doesn’t require any third-party libraries, so `requirements.txt` is not necessary. However, if you expand the game with additional libraries, list them in this file:

    ```plaintext
    # requirements.txt
    # Add any Python dependencies here, e.g.,
    # requests==2.26.0
    ```

### Step 3: Create a Dockerfile
In the project directory, create a `Dockerfile` with the following content. This file contains the instructions Docker needs to build the container.

    ```dockerfile
    # Dockerfile

    # Use a lightweight Python image as the base
    FROM python:3.9-slim

    # Set the working directory inside the container
    WORKDIR /app

    # Copy the game script into the container
    COPY game.py .

    # (Optional) Copy the requirements file and install dependencies
    # COPY requirements.txt .
    # RUN pip install -r requirements.txt

    # Command to run the game
    CMD ["python", "game.py"]
    ```

Explanation:
- `FROM python:3.9-slim`: Starts with a minimal Python 3.9 image.
- `WORKDIR /app`: Sets `/app` as the working directory within the container.
- `COPY game.py .`: Copies `game.py` from your local directory to the container.
- `CMD ["python", "game.py"]`: Command to run the game when the container starts.

### Step 4: Build the Docker Image
In the terminal, run the following command to build the Docker image:

```bash
docker build -t guess-the-number-game .
```

Here’s what this does:

- ```docker build```: Command to build a Docker image.
- ```-t guess-the-number-game```: Tags the image with the name guess-the-number-game.
- ```.```: Specifies the current directory as the build context (where Docker will find the Dockerfile).

### Step 5: Run the Docker Container
Once the image is built, you can run the container:

```bash
docker run -it guess-the-number-game
```
Here’s what each part does:

- ```docker run```: Runs a Docker container from an image.
- ```it```: Opens an interactive terminal in the container.
- ```guess-the-number-game```: The name of the image to run.

### Step 6: Play the Game in the Container
After running the container, you should see the game prompt in your terminal, and you can play the game directly from inside the container!

### Summary
You’ve now containerized your Python game! Here’s a quick recap:

1. Created a Dockerfile with instructions to build the image.
2. Built the Docker image.
3. Ran the container to play the game.

