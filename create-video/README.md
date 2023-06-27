# execute these two commands from the root level of the project

docker build -t video

## adjust the pptx filename and mp4 files to change which pptx and mp4 are used
docker run -v "$(pwd)/input:/input" -v "$(pwd)/output:/output" video