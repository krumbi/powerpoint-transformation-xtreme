FROM python:3.10.11

RUN pip install --upgrade pip

WORKDIR /app

RUN git clone https://github.com/justinjohn0306/Wav2Lip

WORKDIR /app/Wav2Lip

RUN wget 'https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA' -O 'checkpoints/wav2lip_gan.pth'
RUN wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "face_detection/detection/sfd/s3fd.pth"

RUN pip install --no-cache-dir -r requirements.txt

RUN apt update && apt install -y ffmpeg

WORKDIR /app/Wav2Lip

# ENTRYPOINT ["python", "inference.py", "--checkpoint_path", "checkpoints/wav2lip_gan.pth", "--face", "Avatar.png", "--audio", "Audio.wav"]

COPY multiple_inference.py /app/Wav2Lip

# ENTRYPOINT ["python", "multiple_inference.py", "/input", "/output"]
ENTRYPOINT python multiple_inference.py input output