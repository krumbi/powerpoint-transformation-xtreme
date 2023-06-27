
import numpy as np
import soundfile as sf
import os
import sys
import glob
from encoder import inference as encoder
from synthesizer.inference import Synthesizer
from vocoder import inference as vocoder
import argparse
import re

# Define paths for model weights
current_dir = os.path.dirname(os.path.abspath(__file__))
encoder_weights_path = os.path.join(current_dir, "models_CorentinJ", "encoder.pt")
synthesizer_weights_path = os.path.join(current_dir, "models_CorentinJ", "synthesizer.pt")
vocoder_weights_path = os.path.join(current_dir, "models_CorentinJ", "vocoder.pt")

# Load the pre-trained models
encoder.load_model(encoder_weights_path)
synthesizer = Synthesizer(synthesizer_weights_path)
vocoder.load_model(vocoder_weights_path)


def clone_voice(input_audio_path, text, output_audio_dir, index):
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

    # Construct the output file path
    output_file_path = os.path.join(output_audio_dir, f"slide-{index}.wav")

    # Save the generated audio file
    sf.write(output_file_path, scaled_audio, synthesizer.sample_rate)
    print("Output audio file should be in:", output_file_path)


def main():
    parser = argparse.ArgumentParser(description='Voice cloning script')
    parser.add_argument('input', metavar='INPUT', type=str, help='Input directory for TXT and MP3 files')
    parser.add_argument('output', metavar='OUTPUT', type=str, help='Output directory to store the generated audio files')

    args = parser.parse_args()

    input_folder = args.input
    output_folder = args.output

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Find all TXT and MP3 files in the input folder
    file_regex = re.compile(r"slide_(\d+).txt")
    text_files = [file, file_regex.match(os.path.basename(file)).groups[1] for file in glob.glob(os.path.join(input_folder, "*.txt"))]
    text_files = sorted(text_files, key=lambda x: x[1])
    mp3_files = sorted(glob.glob(os.path.join(input_folder, "*.mp3")))

    # Check if there is at least one mp3 file in the input folder
    if not mp3_files:
        raise ValueError("No mp3 files found in the input directory.")

    # Use the first mp3 file found as the input audio
    mp3_file = mp3_files[0]

    # Clone voice
    for index, text_file in enumerate(text_files, start=1):
        with open(text_file, 'r') as file:
            text = file.read()
            clone_voice(mp3_file, text, output_folder, index)

if __name__ == "__main__":
    main()
