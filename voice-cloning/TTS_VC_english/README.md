# Using english voice cloning and text to speech model

This application is build with resources from [CorentinJ Github Repository](https://github.com/CorentinJ/Real-Time-Voice-Cloning/wiki/Pretrained-models). 

After downloading the folder 'TTS_VC_english' please switch to the subfolder 'models_CorentinJ' and download the pretrained models of encoder, synthesizer and vocoder. After that you should be able to build and run the application in a Docker Container.



# how to start the docker 

docker build -t voice .

docker run -v "$(pwd)":/app/voice-cloning -v "$(pwd)/output_audio:/app/output_audio" voice python voice_cloning_tts.py slide-1.txt slide-2.txt