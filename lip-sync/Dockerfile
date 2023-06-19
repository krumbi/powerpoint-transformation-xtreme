FROM python:3.8

RUN pip install --upgrade pip

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx

RUN git clone https://github.com/Markfryazino/wav2lip-hq.git

WORKDIR /app/wav2lip-hq

RUN wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "face_detection/detection/sfd/s3fd.pth"

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gdown
RUN pip install librosa==0.8.0
RUN pip install numba==0.53.1

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



