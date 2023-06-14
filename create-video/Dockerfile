# FROM python:3.9

# WORKDIR /app

# # Install LibreOffice, Poppler, and necessary tools
# RUN apt-get update \
#     && apt-get install -y unoconv libreoffice poppler-utils \
#     && apt-get clean

# # Copy script and install dependencies
# COPY ppt2pdf.py .

# RUN pip install pdf2image

# ENTRYPOINT ["python", "ppt2pdf.py"]
FROM python:3.9

WORKDIR /app

# Install LibreOffice, Poppler, and necessary tools
RUN apt-get update \
    && apt-get install -y unoconv libreoffice poppler-utils \
    && apt-get clean

# Copy script and install dependencies
COPY create-video/ppt2image.py /app
COPY 2.2_video_ppt.pptx /app

RUN pip install pdf2image

ENTRYPOINT ["python", "ppt2image.py"]
