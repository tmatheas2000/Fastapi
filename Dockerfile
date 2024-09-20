# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (Google Cloud Run uses this port by default)
EXPOSE 8080

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "product.main:app", "--host", "0.0.0.0", "--port", "8080"]