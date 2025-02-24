# Use official Python image as a base
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies (optional, add only what you need)
RUN apt-get update

# Copy the requirements file
COPY requirements.txt .

# Install dependencies with verbose output for debugging
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Copy the project files
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Run the Django server (overridden by docker-compose command)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]