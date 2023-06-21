FROM python:3.10.11

RUN pip install --upgrade pip

WORKDIR /app

RUN git clone https://github.com/justinjohn0306/Wav2Lip

WORKDIR /app/Wav2Lip

RUN wget 'https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA' -O 'checkpoints/wav2lip_gan.pth'
RUN wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "face_detection/detection/sfd/s3fd.pth"

COPY ./Avatar.jpg .
COPY ./Audio.wav .

RUN pip install --no-cache-dir -r requirements.txt


RUN apt-get install ffmpeg

#RUN apt-get update && apt-get install -y libgl1-mesa-glx

#ENTRYPOINT ["tail", "-f", "/dev/null"]
#COPY ./app.py .
#ENTRYPOINT ["python", "app.py"]
#RUN python inference.py --checkpoint_path "checkpoints/wav2lip_gan.pth" --face Avatar.jpg --audio Audio.wav --outfile Test.mp4



