# Python base image
FROM python

# Set the working directory
WORKDIR /app

# Copy the application files
COPY main.py food.py snake.py /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install pygame

# Expose port 8000
EXPOSE 8000

# Set the entry point command
CMD ["python", "./main.py"]
