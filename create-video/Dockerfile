# FROM python:3.9

# WORKDIR /app

# # Install system dependencies
# RUN apt-get update \
#     && apt-get install -y libreoffice poppler-utils ffmpeg \
#     && apt-get clean

# # Copy script and install Python dependencies
# COPY create-video/requirements.txt /app
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy script
# COPY create-video/ppt2video.py /app

FROM python:3.9

WORKDIR /app

# Install system dependencies
RUN apt-get update --fix-missing
RUN apt update \
    && apt install -y libreoffice poppler-utils ffmpeg \
    && apt clean

# Copy script and install Python dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy script
COPY ppt2video.py /app

ENTRYPOINT ["python", "ppt2video.py", "/input", "/output"]
