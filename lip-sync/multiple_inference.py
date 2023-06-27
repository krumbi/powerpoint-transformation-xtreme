import argparse
import subprocess
import os
import glob
import pathlib

def main():
    parser = argparse.ArgumentParser(description='Wav2Lip multiple audio processing script')
    parser.add_argument('input', metavar='INPUT', type=pathlib.Path, help='Input folder containing the audio files')
    parser.add_argument('output', metavar='OUTPUT', type=pathlib.Path, help='Output folder to store the generated videos')

    args = parser.parse_args()

    # Check if input is a valid directory
    if not args.input.is_dir():
        parser.error("Input is not a valid directory")

    # Check if output is a valid directory
    if not args.output.is_dir():
        parser.error("Output is not a valid directory")

    # Get a list of audio files
    audio_files = glob.glob(str(args.input / '*.wav'))

    avatar_file = str(args.input / 'avatar.png')

    for i, audio_file in enumerate(audio_files, start=1):
        # Generate output filename based on the input audio filename
        output_file = str(args.output / f"video_{i}.mp4")
        
        # Adjust lip-sync parameters
        subprocess.run(["python", "inference.py", 
                        "--checkpoint_path", "checkpoints/wav2lip_gan.pth", 
                        "--face", avatar_file, 
                        "--audio", audio_file,
                        "--outfile", output_file
                        ])

if __name__ == "__main__":
    main()
