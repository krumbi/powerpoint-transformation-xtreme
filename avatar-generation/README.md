# execute these two commands from the root level of the project

docker build -t avatar-generation .

## adjust the description with the description of the human you want to have
docker run -v "$(pwd)/input:/input" -v "$(pwd)/output:/output" -e API_KEY=<api_key>  avatar-generation