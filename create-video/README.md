# execute these two commands from the root level of the project

docker build -t ppt2video -f create-video/Dockerfile .

## adjust the pptx filename and mp4 files to change which pptx and mp4 are used
docker run -v "$(pwd)":/app/create-video ppt2video test.pptx mp4_1.mp4 mp4_2.mp4