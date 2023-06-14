import subprocess
import os
import sys
from pdf2image import convert_from_path

def convert_pptx_to_pdf(input_file):
    input_path = os.path.join("/app/create-video", input_file)
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    output_path = os.path.join("/app/create-video", output_file)

    subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", "/app/create-video", input_path])

    print(f"Conversion completed. Output file: {output_file}")

    # Check if the output PDF file exists
    if os.path.isfile(output_path):
        # Convert PDF to images
        images = convert_from_path(output_path)

        # Save each image as a separate file
        for i, image in enumerate(images):
            image_path = os.path.join("/app/create-video", f"{os.path.splitext(output_file)[0]}_{i}.jpg")
            image.save(image_path, "JPEG")
            print(f"Image saved: {image_path}")
    else:
        print("Output PDF file not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the name of the PPTX file as an argument.")
        sys.exit(1)
    
    input_file = sys.argv[1]
    convert_pptx_to_pdf(input_file)
