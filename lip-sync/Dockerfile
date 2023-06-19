# Verwenden Sie eine Python-Basisimage als Grundlage
FROM python:3.10

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

RUN git clone https://github.com/Markfryazino/wav2lip-hq.git
# Kopieren Sie die Anforderungen des Projekts in den Container

RUN cd wav2lip-hq
RUN pip install gdown
RUN pip install librosa==0.8.0
RUN wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "face_detection/detection/sfd/s3fd.pth"

# Installieren Sie die Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

COPY ./GdriveDown.py .
RUN python GdriveDown.py 

RUN python inference.py \
        --checkpoint_path "checkpoints/wav2lip_gan.pth" \
        --segmentation_path "checkpoints/face_segmentation.pth" \
        --sr_path "checkpoints/esrgan_max.pth" \
        --no_sr\
        --no_segmentation\
        --face "videos/Avatar.jpg" \
        --audio "videos/Audio3.wav" \
        --outfile "results/Test.mp4"



