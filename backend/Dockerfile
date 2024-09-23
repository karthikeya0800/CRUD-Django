# Use a base image that includes necessary build tools
FROM python:3.9-slim-bullseye

# Set the working directory
WORKDIR /app

# Install system dependencies needed for mysqlclient
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    pkg-config \
    libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents to the working directory
COPY . .

# Expose the port Django will run on
EXPOSE 3001

# Run migration commands and then start the server
CMD ["sh", "-c", "python manage.py makemigrations app && python manage.py migrate && gunicorn project.wsgi:application --bind 0.0.0.0:3001"]
