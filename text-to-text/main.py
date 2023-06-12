import argparse
import collections.abc
import pptx
import requests
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('input', metavar='INPUT', type=str, help='the input file')
parser.add_argument('-o', '--output', metavar='OUTPUT', default=pathlib.Path("output"), type=pathlib.Path, help='the output directory')
args = parser.parse_args()

prs = pptx.Presentation(args.input)

raw_text_folder = args.output.joinpath("raw_text")
raw_text_folder.mkdir(parents=True, exist_ok=True)

for i, s in enumerate(prs.slides, start=1):
    text = []
    for shape in s.shapes:
        if not shape.has_text_frame or len(shape.text) == 0:
            continue
        if "Title" in shape.name:
            text.append(f"Title: {shape.text}")
            continue
        
        for p in shape.text_frame.paragraphs:
            if len(p.runs) > 0:
                current_text = ""
                for r in p.runs:
                    color_type = str(r.font.color.type)
                    if "SCHEME" in color_type and "BACKGROUND" in str(r.font.color.theme_color):
                        pass
                    elif color_type == "None":
                        current_text += r.text
                    else:
                        current_text += r.text
                if len(current_text) == 0:
                    continue
                text.append(f"{'  ' * p.level}- {current_text}")
            else:    
                if len(p.text) == 0:
                    continue
                text.append(f"{'  ' * p.level}- {p.text}")
        
    with open(raw_text_folder.joinpath(f"slide_{i}.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(text))
