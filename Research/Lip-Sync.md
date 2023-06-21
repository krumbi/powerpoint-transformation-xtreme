# Lip-Sync
## Requirements

The following requirements need to be met for the lip-sync model to be usable for the pipeline.

- As an input we want to be able to use image files.
- For audio mp3 or wav files should work.
- The model needs to be able to run on a local machine.


## Research

- Different ways:	
-- Lip-Sync from audio files/from text files.
-> Best solution is to use audio files and find a model to match syllables to lip movement. 
- All in one solution: https://www.synthesia.io/ 
-- Presentations with virtual avatar, tts, artificial voices, lip-sync,…
- Viseme from Microsoft Azure
-- https://learn.microsoft.com/de-de/azure/cognitive-services/speech-service/how-to-speech-synthesis-viseme?pivots=programming-language-python&tabs=visemeid
-- Best solution, however not usable for us because of cost, user-bound api key etc…
- Wav2Lip
-- https://huggingface.co/camenduru/Wav2Lip
-- Best usable solution
-- Part of the paper: A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild published at ACM Multimedia 2020.
-- “Works for any identity, voice, and language. Also works for CGI faces and synthetic voices.”
- LipSync
-- GitHub - huailiang/LipSync: LipSync for Unity3D 根据语音生成口型动画 支持fmod
-- Not relevant because we would need Unity 3D implementation.
