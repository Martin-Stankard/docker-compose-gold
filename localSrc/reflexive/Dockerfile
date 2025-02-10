# Use an official Python runtime as a parent image
FROM python:3.13.1-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# need git ...
RUN apk update && apk add git

RUN git clone https://github.com/Martin-Stankard/docker-compose-gold.git

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "testDcReflex.py"] 