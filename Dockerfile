# Use an official Python runtime as a parent image
FROM python:3.11.9-alpine3.19

# Set the working directory to /app
WORKDIR /app

# Copy the application code into the container at /app
COPY app.py /app/app.py
COPY static /app/static
COPY templates /app/templates

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
