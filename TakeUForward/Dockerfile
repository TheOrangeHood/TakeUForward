# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app/TakeUForward

# Install dependencies
COPY requirements.txt /app/TakeUForward/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /app/TakeUForward/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
