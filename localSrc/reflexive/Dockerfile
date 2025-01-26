# Use an official Python runtime as a parent image
FROM python:3.13.1-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
# EXPOSE 80 #TODO clean this up if it works out in the docker-c.yml as "127.0.0.1:8080:80"  a la https://www.bitdoze.com/docker-bypasses-firewall/

# Define environment variable. FINAL only ? service specifoc 
ENV PROFILE REFLEXIVE

# Run app.py when the container launches
CMD ["python", "testDcReflex.py"] 