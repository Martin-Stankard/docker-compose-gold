# Use an official Python runtime as a parent image
FROM python:3.13.1-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable. TODO, this should be a parameter passed in from the docker-compose.yml file/profile would be ideal.
ENV PROFILE REFLEXIVE

# Run app.py when the container launches
CMD ["python", "hello.py"] 