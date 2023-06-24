import numpy as np
import soundfile as sf
import os

from encoder import inference as encoder
from synthesizer.inference import Synthesizer
from vocoder import inference as vocoder



# Usage example - parameters to be adjusted
text = "This is a test text. Made for Power Point Transformation Xtreme" # text to be spoken
audio_input_file =  "samples_1320_00000.mp3" # sample audio file name 
audio_output_file = "sample_output_vc.wav" # output file name


# Construct the path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define audio file paths
input_audio_path = os.path.join(current_dir, "input_audio", audio_input_file)
output_audio_path = os.path.join(current_dir, "output_audio", audio_output_file)

# Define file paths for model weights
encoder_weights_path = os.path.join(current_dir, "models_CorentinJ", "encoder.pt")
synthesizer_weights_path = os.path.join(current_dir, "models_CorentinJ", "synthesizer.pt")
vocoder_weights_path = os.path.join(current_dir, "models_CorentinJ", "vocoder.pt")

# Load the pre-trained models
encoder.load_model(encoder_weights_path)
synthesizer = Synthesizer(synthesizer_weights_path)
vocoder.load_model(vocoder_weights_path)


# Function for voice cloning
def clone_voice(input_audio_path, text, output_audio_path):

    # Load input audio
    input_audio, sr = sf.read(input_audio_path)

    # Preprocess input audio
    preprocessed_audio = encoder.preprocess_wav(input_audio, sr)

    # Encode preprocessed audio
    embeddings = encoder.embed_utterance(preprocessed_audio)

    # Generate speech spectrograms
    specs = synthesizer.synthesize_spectrograms([text], [embeddings])

    # Convert spectrograms to waveform
    generated_wav = vocoder.infer_waveform(specs[0])

    # Pad the waveform to match the desired length
    generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode="constant")

    # Scale the waveform and save as an audio file
    scaled_audio = np.int16(generated_wav / np.max(np.abs(generated_wav)) * 32767)

    # Save the generated audio file
    sf.write(output_audio_path, scaled_audio, synthesizer.sample_rate)
    print("Output audio file should be in: ", output_audio_path) 

    

# Clone voice
clone_voice(input_audio_path, text, output_audio_path)

