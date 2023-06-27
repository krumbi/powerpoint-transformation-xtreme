# import os
# import sys
# import subprocess
# from pdf2image import convert_from_path
# from moviepy.editor import *


# def convert_pptx_to_pdf(input_file, mp4_files):
#     input_path = os.path.join("/app/create-video", input_file)
#     output_file = os.path.splitext(input_file)[0] + ".pdf"
#     output_path = os.path.join("/app/create-video", output_file)

#     subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", "/app/create-video", input_path])

#     print(f"Conversion completed. Output file: {output_file}\n")

#     # Check if the output PDF file exists
#     if os.path.isfile(output_path):
#         # Convert PDF to images
#         images = convert_from_path(output_path)

#         # Save each image as a separate file
#         image_files = []
#         for i, image in enumerate(images):
#             image_path = os.path.join("/app/create-video", f"slide_{i}.jpg")
#             image.save(image_path, "JPEG")
#             image_files.append(image_path)
#             print(f"Image saved: {image_path}")

#         # Adjust the paths of the mp4 files
#         mp4_files = [os.path.join("/app/create-video", mp4_file) for mp4_file in mp4_files]
#         # Create video from images
#         create_video(image_files, mp4_files)

#     else:
#         print(f"Image saved: {image_path}")("Output PDF file not found.\n")




# def create_video(image_files, mp4_files, break_duration=1):
#     if len(image_files) != len(mp4_files):
#         print("Number of images and MP4 files does not match.")
#         return

#     clips = []
#     for i, image_path in enumerate(image_files):
#         mp4_file = mp4_files[i]

#         # Get duration of the MP4 file
#         duration = get_duration(mp4_file)

#         # Load the original mp4 file
#         original_video = VideoFileClip(mp4_file)

#         # Extract the audio from the original video
#         audio = original_video.audio

#         # Create a video clip with the image and duration + break_duration
#         image_clip = ImageClip(image_path, duration=duration + break_duration)

#         # Set the audio for the image clip
#         image_clip = image_clip.set_audio(audio)

#         # Add original video in the bottom right corner with width of 300 pixels
#         original_video = original_video.resize(width=300)
#         original_video = original_video.set_position(("right", "bottom")).set_duration(duration)

#         # Composite the image clip and the original video
#         composite_clip = CompositeVideoClip([image_clip, original_video])

#         clips.append(composite_clip)

#     # Concatenate all clips into a single video
#     final_video = concatenate_videoclips(clips)

#     # Set output filename
#     output_file = os.path.splitext(mp4_files[0])[0] + "_output.mp4"

#     # Write the final video to a file
#     final_video.write_videofile(output_file, codec="libx264", fps=24, audio_codec="aac")

#     print(f"Video created: {output_file}")

# def get_duration(mp4_file):
#     video = VideoFileClip(mp4_file)
#     duration = video.duration
#     video.close()
#     return duration


# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print("Please provide the name of the PPTX file and at least one MP4 file as arguments.")
#         sys.exit(1)

#     input_file = sys.argv[1]
#     mp4_files = sys.argv[2:]
#     print('mp4_files', mp4_files)
#     convert_pptx_to_pdf(input_file, mp4_files)
import argparse
import subprocess
import os
import glob
import pathlib
from pdf2image import convert_from_path
from moviepy.editor import *


def convert_pptx_to_pdf(input_file, output_folder):
    input_filename = os.path.basename(input_file)
    output_file = os.path.join(output_folder, os.path.splitext(input_filename)[0] + ".pdf")

    subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", output_folder, input_file])

    print(f"Conversion completed. Output file: {output_file}\n")

    # Check if the output PDF file exists
    if os.path.isfile(output_file):
        # Convert PDF to images
        images = convert_from_path(output_file)

        # Save each image as a separate file and create video from each image
        image_paths = []
        for i, image in enumerate(images):
            image_path = os.path.join(output_folder, f"slide_{i}.jpg")
            image.save(image_path, "JPEG")
            print(f"Image saved: {image_path}")
            image_paths.append(image_path)

        # Return the list of image paths
        return image_paths

    else:
        print("Output PDF file not found.\n")
        return


def create_video(image_files, mp4_files, output_file, break_duration=1):
    clips = []
    for i, image_path in enumerate(image_files):
        mp4_file = mp4_files[i]

        # Get duration of the MP4 file
        duration = get_duration(mp4_file)

        # Load the original mp4 file
        original_video = VideoFileClip(mp4_file)

        # Extract the audio from the original video
        audio = original_video.audio

        # Create a video clip with the image and duration + break_duration
        image_clip = ImageClip(image_path, duration=duration + break_duration)

        # Set the audio for the image clip
        image_clip = image_clip.set_audio(audio)

        # Add original video in the bottom right corner with width of 300 pixels
        original_video = original_video.resize(width=300)
        original_video = original_video.set_position(("right", "bottom")).set_duration(duration)

        # Composite the image clip and the original video
        composite_clip = CompositeVideoClip([image_clip, original_video])

        clips.append(composite_clip)

    # Concatenate all clips into a single video
    final_video = concatenate_videoclips(clips)

    # Write the final video to a file
    final_video.write_videofile(output_file, codec="libx264", fps=24, audio_codec="aac")

    print(f"Video created: {output_file}")


def get_duration(mp4_file):
    video = VideoFileClip(mp4_file)
    duration = video.duration
    video.close()
    return duration


def main():
    parser = argparse.ArgumentParser(description='PPT to video conversion script')
    parser.add_argument('input', metavar='INPUT', type=str, help='Input directory for PPTX and MP4 files')
    parser.add_argument('output', metavar='OUTPUT', type=str, help='Output directory to store the generated videos')

    args = parser.parse_args()

    input_folder = args.input
    output_folder = args.output

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Find all PPTX and MP4 files in the input folder
    pptx_files = glob.glob(os.path.join(input_folder, "*.pptx"))
    mp4_files = sorted(glob.glob(os.path.join(input_folder, "*.mp4")))

    # Convert each PPTX file to PDF and then to video
    all_image_paths = []
    for input_file in pptx_files:
        image_paths = convert_pptx_to_pdf(input_file, output_folder)
        all_image_paths.extend(image_paths)

    # Create a single video from all images and MP4 files
    if len(all_image_paths) != len(mp4_files):
        print("Number of images and MP4 files does not match.")
    else:
        output_video_file = os.path.join(output_folder, "output.mp4")
        create_video(all_image_paths, mp4_files, output_video_file)

if __name__ == "__main__":
    main()
