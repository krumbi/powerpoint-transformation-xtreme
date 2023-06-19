# execute these two commands from the root level of the project

docker build -t avatargen -f avatar-generation/Dockerfile .

## adjust the description with the description of the human you want to have
docker run -e DESCRIPTION="woman with glasses" -v "$(pwd)/output:/app/avatar" avatargen