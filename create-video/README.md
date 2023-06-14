# execute these two commands from the root level of the project
docker build -t ppt2pdf -f create-video/Dockerfile .

## adjust the pptx filename to change which pptx is converted
docker run -v "$(pwd)":/app/create-video ppt2pdf 2.2_video_ppt.pptx