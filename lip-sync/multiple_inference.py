import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description='Wav2Lip multiple audio processing script')
    parser.add_argument('audios', metavar='N', type=str, nargs='+',
                        help='audio files to process')

    args = parser.parse_args()

    for audio in args.audios:
        if not os.path.isfile(audio):
            print(f"File {audio} not found.")
            continue

        # Generate output filename based on the input audio filename
        basename = os.path.basename(os.path.splitext(audio)[0])  # Extract filename without extension
        output_file = "results/" + basename + '.mp4'  # Add results/ directory and extension
        
        # You might need to modify the command based on how you can specify the output file in inference.py
        subprocess.run(["python", "inference.py", 
                        "--checkpoint_path", "checkpoints/wav2lip_gan.pth", 
                        "--face", "Avatar.png", 
                        "--audio", audio,
                        "--outfile", output_file])  # assuming --outfile is used to specify output file

if __name__ == "__main__":
    main()
