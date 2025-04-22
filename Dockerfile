# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Install Python dependencies
# First copy only the requirements file, to cache the pip install layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container (after pip install to utilize Docker cache)
COPY . .
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

ENV PYTHONPATH /app

# Run app.py when the container launches
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "src.app:app"]
