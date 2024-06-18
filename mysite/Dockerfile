# Use the official Python image as a parent image
FROM python:3.12.3

# Set environment variable to ensure Python output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start the Django app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
