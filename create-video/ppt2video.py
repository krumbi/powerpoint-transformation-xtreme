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

#         # Resize the image clip to fit the resolution of the MP4 file (optional)
#         # image_clip = image_clip.resize(height=480)  # Adjust the height as needed

#         # Add original video in the bottom right corner with width of 300 pixels
#         original_video = original_video.resize(width=300)
#         original_video = original_video.set_position(("right", "bottom")).set_duration(duration)

#         # Composite the image clip and the original video
#         composite_clip = CompositeVideoClip([image_clip, original_video])

#         clips.append(composite_clip)

#         # Add a small break after each MP4 file
#         break_clip = ColorClip(duration=break_duration, color=(0, 0, 0), size=(1920, 1080))
#         clips.append(break_clip)

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




import os
import sys
import subprocess
from pdf2image import convert_from_path
from moviepy.editor import *


def convert_pptx_to_pdf(input_file, mp4_files):
    input_path = os.path.join("/app/create-video", input_file)
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    output_path = os.path.join("/app/create-video", output_file)

    subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", "/app/create-video", input_path])

    print(f"Conversion completed. Output file: {output_file}\n")

    # Check if the output PDF file exists
    if os.path.isfile(output_path):
        # Convert PDF to images
        images = convert_from_path(output_path)

        # Save each image as a separate file
        image_files = []
        for i, image in enumerate(images):
            image_path = os.path.join("/app/create-video", f"slide_{i}.jpg")
            image.save(image_path, "JPEG")
            image_files.append(image_path)
            print(f"Image saved: {image_path}")

        # Adjust the paths of the mp4 files
        mp4_files = [os.path.join("/app/create-video", mp4_file) for mp4_file in mp4_files]
        # Create video from images
        create_video(image_files, mp4_files)

    else:
        print(f"Image saved: {image_path}")("Output PDF file not found.\n")




def create_video(image_files, mp4_files, break_duration=1):
    if len(image_files) != len(mp4_files):
        print("Number of images and MP4 files does not match.")
        return

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

        # Resize the image clip to fit the resolution of the MP4 file (optional)
        # image_clip = image_clip.resize(height=480)  # Adjust the height as needed

        # Add original video in the bottom right corner with width of 300 pixels
        original_video = original_video.resize(width=300)
        original_video = original_video.set_position(("right", "bottom")).set_duration(duration)

        # Composite the image clip and the original video
        composite_clip = CompositeVideoClip([image_clip, original_video])

        clips.append(composite_clip)

    # Concatenate all clips into a single video
    final_video = concatenate_videoclips(clips)

    # Set output filename
    output_file = os.path.splitext(mp4_files[0])[0] + "_output.mp4"

    # Write the final video to a file
    final_video.write_videofile(output_file, codec="libx264", fps=24, audio_codec="aac")

    print(f"Video created: {output_file}")

def get_duration(mp4_file):
    video = VideoFileClip(mp4_file)
    duration = video.duration
    video.close()
    return duration


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide the name of the PPTX file and at least one MP4 file as arguments.")
        sys.exit(1)

    input_file = sys.argv[1]
    mp4_files = sys.argv[2:]
    print('mp4_files', mp4_files)
    convert_pptx_to_pdf(input_file, mp4_files)

