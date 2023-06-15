# FROM python:3.9

# WORKDIR /app

# # Install LibreOffice, Poppler, and necessary tools
# RUN apt-get update \
#     && apt-get install -y unoconv libreoffice poppler-utils \
#     && apt-get clean

# # Copy script and install dependencies
# COPY create-video/ppt2image.py /app
# COPY 2.2_video_ppt.pptx /app

# RUN pip install pdf2image

# ENTRYPOINT ["python", "ppt2image.py"]

# FROM python:3.9

# WORKDIR /app

# # Install LibreOffice, Poppler, and necessary tools
# RUN apt-get update \
#     && apt-get install -y unoconv libreoffice poppler-utils \
#     && apt-get clean

# # Install moviepy
# RUN pip install moviepy

# # Copy script and install dependencies
# COPY create-video/ppt2image.py /app
# COPY 2.2_video_ppt.pptx /app

# RUN pip install pdf2image

# ENTRYPOINT ["python", "ppt2image.py"]

FROM python:3.9

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y libreoffice poppler-utils ffmpeg \
    && apt-get clean

# Copy script and install Python dependencies
COPY create-video/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy script
COPY create-video/ppt2video.py /app

ENTRYPOINT ["python", "ppt2video.py"]