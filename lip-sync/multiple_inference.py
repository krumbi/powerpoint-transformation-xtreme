# import argparse
# import subprocess
# import os

# def main():
#     parser = argparse.ArgumentParser(description='Wav2Lip multiple audio processing script')
#     parser.add_argument('audios', metavar='N', type=str, nargs='+',
#                         help='audio files to process')

#     args = parser.parse_args()

#     for audio in args.audios:
#         if not os.path.isfile(audio):
#             print(f"File {audio} not found.")
#             continue

#         # Generate output filename based on the input audio filename
#         basename = os.path.basename(os.path.splitext(audio)[0])  # Extract filename without extension
#         output_file = "results/" + basename + '.mp4'  # Add results/ directory and extension
        
#         # You might need to modify the command based on how you can specify the output file in inference.py
#         subprocess.run(["python", "inference.py", 
#                         "--checkpoint_path", "checkpoints/wav2lip_gan.pth", 
#                         "--face", "Avatar.png", 
#                         "--audio", audio,
#                         "--outfile", output_file])  # assuming --outfile is used to specify output file

# if __name__ == "__main__":
#     main()





# import argparse
# import subprocess
# import os
# import glob
# import pathlib

# def main():
#     parser = argparse.ArgumentParser(description='Wav2Lip multiple audio processing script')
#     parser.add_argument('input', metavar='INPUT', type=pathlib.Path, help='Input folder containing the audio files')
#     parser.add_argument('output', metavar='OUTPUT', type=pathlib.Path, help='Output folder to store the generated videos')

#     args = parser.parse_args()

#     # Check if input is a valid directory
#     if not args.input.is_dir():
#         parser.error("Input is not a valid directory")

#     # Check if output is a valid directory
#     if not args.output.is_dir():
#         parser.error("Output is not a valid directory")

#     # Get a list of audio files
#     audio_files = glob.glob(str(args.input / '*.wav'))

#     avatar_file = str(args.input / 'avatar.png')

#     for audio_file in audio_files:
#         # Generate output filename based on the input audio filename
#         # basename = os.path.basename(os.path.splitext(audio_file)[0])  # Extract filename without extension
#         # output_file = str(args.output / (basename + '.mp4'))  # Add results/ directory and extension
#         output_file = str(args.output / os.path.basename(audio_file))
#         subprocess.run(["python", "inference.py", 
#                         "--checkpoint_path", "checkpoints/wav2lip_gan.pth", 
#                         "--face", avatar_file, 
#                         "--audio", audio_file,
#                         "--outfile", output_file])

# if __name__ == "__main__":
#     main()







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

    for audio_file in audio_files:
        # Generate output filename based on the input audio filename
        basename = os.path.basename(os.path.splitext(audio_file)[0])  # Extract filename without extension
        output_file = str(args.output / (basename + '.mp4'))  # Add results/ directory and extension
        
        # Adjust lip-sync parameters
        subprocess.run(["python", "inference.py", 
                        "--checkpoint_path", "checkpoints/wav2lip_gan.pth", 
                        "--face", avatar_file, 
                        "--audio", audio_file,
                        "--outfile", output_file
                        ])

if __name__ == "__main__":
    main()
