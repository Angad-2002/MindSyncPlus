# Use a Python base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the entire Flask application to the container
COPY . .

# Expose the port the Flask app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=your_app_name.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["flask", "run"]
