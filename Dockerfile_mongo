# Use the official MongoDB image as the base image
FROM mongo

# Install MongoDB shell
RUN apt-get update && apt-get install -y wget gnupg && \
    wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add - && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list && \
    apt-get update && apt-get install -y mongodb-org-shell

# Copy the initialization script into the container
COPY init.js /docker-entrypoint-initdb.d/

# Define environment variable for MongoDB database
ENV MONGO_INITDB_DATABASE=ProfileApp

# Expose MongoDB port
EXPOSE 27017
