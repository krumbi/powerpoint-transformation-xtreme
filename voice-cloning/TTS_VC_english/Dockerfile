# Use a base image with Python installed
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the required dependencies
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . .

# Run the python script
CMD ["python", "voice_cloning_with_tts.py"]
