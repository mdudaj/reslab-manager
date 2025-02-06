FROM python:3.10-slim

# Set the working directory
WORKDIR /reslab_app

# Set the environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install the dependencies
COPY ./requirements.txt /reslab_app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY src/ .

# Expose the port
EXPOSE 8000

# Run the application using gunicorn
CMD ["gunicorn", "--config", "gunicorn_config.py", "reslab_manager.wsgi:application"]

