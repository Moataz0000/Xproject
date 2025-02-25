# Use official Python image as a base
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update

# Copy the requirements file
COPY requirements.txt .

RUN  pip install --upgrade pip
# Install dependencies with verbose output for debugging
RUN pip install --no-cache-dir -r requirements.txt --verbose --timeout 120 --index-url https://pypi.org/simple/

# Copy the project files
COPY . .

# Expose the port Django runs on
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]