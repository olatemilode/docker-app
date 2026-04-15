# Use an official lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy files from local machine into container
COPY . .

# Install dependencies listed in requirements.txt
RUN pip install -r requirement.txt

# Specify command to run your app inside the container
CMD ["python", "app.py"]
