# How to use docker to test locally:
docker build -t lipsync .

docker run -it -v "$(pwd)/results:/app/Wav2Lip/results" -v "$(pwd)/slide-1.wav:/app/Wav2Lip/slide-1.wav" -v "$(pwd)/slide-2.wav:/app/Wav2Lip/slide-2.wav" lipsync slide-1.wav slide-2.wav