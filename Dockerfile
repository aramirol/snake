# Use a base Python image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the application files to the container
COPY main.py food.py snake.py /app/

# Install the necessary dependencies
RUN pip install pygame

# Expose port 8000
EXPOSE 8000

# Run the command to start the application
CMD ["python", "main.py"]
