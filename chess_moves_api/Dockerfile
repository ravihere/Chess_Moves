# Use official Python runtime as base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the working directory
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8001

# Run Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
