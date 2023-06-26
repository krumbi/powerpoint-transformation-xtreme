import os
import io
import warnings
import argparse
import pathlib
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import glob

# Argument parsing
parser = argparse.ArgumentParser(description='Name')
parser.add_argument('input', metavar='INPUT', type=pathlib.Path, help='Input folder containing the description files')
parser.add_argument('output', metavar='OUTPUT', type=pathlib.Path, help='Output folder to store the generated images')
parser.add_argument('api_key', metavar='API_KEY', type=str, help='API key to interact with stability.ai')
args = parser.parse_args()

# Check if input is a valid directory
if not args.input.is_dir():
    parser.error("Input is not a valid directory")

# Check if output is a valid directory
if not args.output.is_dir():
    parser.error("Output is not a valid directory")

# Set up our environment variables
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = args.api_key

# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],  # API Key reference.
    verbose=True,  # Print debug messages.
    engine="stable-diffusion-xl-beta-v2-2-2",
)

# Get a list of input files
input_files = glob.glob(str(args.input / '*.txt'))

for input_file in input_files:
    # Read input text
    with open(input_file, "r", encoding='utf-8') as f:
        description = f.read().strip()  # Assuming the input file contains the description

    # Set up our initial generation parameters.
    answers = stability_api.generate(
        prompt=f"frontal portrait of a {description}, midshot intensity, white studio background, white background, relaxed mimic, photo taken with provia --ar 2:3 --style raw",
        steps=50,
        cfg_scale=12.0,
        width=512,
        height=512,
        samples=1,
        sampler=generation.SAMPLER_K_DPMPP_2M
    )

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                output_filename = os.path.splitext(os.path.basename(input_file))[0] + '.png'
                img = Image.open(io.BytesIO(artifact.binary))
                img.save(str(args.output / output_filename))  # Save image to the output directory with the corresponding filename

