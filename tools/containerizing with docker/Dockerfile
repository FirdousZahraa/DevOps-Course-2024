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
