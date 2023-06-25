# FROM python:3.9

# # Set working directory
# WORKDIR /app

# RUN apt-get update && apt-get install -y libsndfile1

# # Copy requirements.txt and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the source code
# COPY . .

# # Run the voice cloning script
# CMD ["python", "voice_cloning_tts.py"]

FROM python:3.9

# Set working directory
WORKDIR /app

RUN apt-get update && apt-get install -y libsndfile1

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Run the voice cloning script with text files as arguments
CMD ["python", "voice_cloning_tts.py"]
