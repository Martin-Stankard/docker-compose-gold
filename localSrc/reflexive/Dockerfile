# This 

image: alpine









command: sh -c "echo 'Running script in my_profile...some day I will say docker compose up!!!!!! TODO...close off the ports of whatever THIS docker compose ups like a super hero' && sleep 10"



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

# Define environment variable. FINAL only ? service specifoc 
ENV PROFILE REFLEXIVE

# Run app.py when the container launches
CMD ["python", "testDcReflex.py.py"] 