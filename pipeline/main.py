import gui

from gooey import Gooey

import pathlib
import shutil
import subprocess
import shlex

steps = ["text-to-text", "text-to-speech", "avatar-generation", "lip-sync", "video-generation"]
data_folder = pathlib.Path("data")
resource_folder = pathlib.Path("resources")


@Gooey(program_name="PowerPoint Transformation Xtreme",
       progress_regex=r"^pptx-step-(?P<step>\d+)-(.+) exited with code 0$",
       progress_expr="step / 5 * 100",
       disable_progress_bar_animation=False,
       show_restart_button=False)
def main():
    clear_data_folder()
    generate_folders()
    voices = get_voices()
    parser = gui.show_ui(voices)
    args = parser.parse_args()
    
    copy_slides_file(args.pptx_file)
    create_avatar_prompt_file(args.avatar_prompt)
    copy_voice_file(args.voice, args.voice_file)
    create_env_file(args)

    code = run_docker()

    if code != 0:
        raise Exception("Run Docker failed")
    
    code = stop_docker()

    if code != 0:
        raise Exception("Stop Docker failed")

    copy_output_file(args.output_file, args.pptx_file)


def stop_docker():
    command = "docker compose -f compose.yaml rm -f -s -v"
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)

    return_code = None

    while return_code is None:
        return_code = process.poll()
        output = process.stdout.readline().decode("utf-8").strip()

        if (len(output) > 0):
            print(output)
    
    return return_code


def run_docker():
    command = "docker compose -f compose.yaml up"
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)

    return_code = None

    while return_code is None:
        return_code = process.poll()
        output = process.stdout.readline().decode("utf-8").strip()

        if (len(output) > 0):
            print(output)
    
    return return_code


def create_env_file(args):
    lines = [
       f"OUTPUT_LANG={args.language}\n",
       f"OPENAI_API_KEY={args.openai_api_key}\n",
       f"DREAMSTUDIO_API_KEY={args.dreamstudio_api_key}\n",
    ]

    if args.text_prompt is not None:
        lines.append(f"PROMPT_ADDITION={args.text_prompt}\n")

    with open("run.env", "w", encoding='utf-8') as f:
        f.writelines(lines)


def copy_output_file(output_file: pathlib.Path, input_file: pathlib.Path):
    current_output_file_path = data_folder.joinpath("video-generation").joinpath("output").joinpath("output.mp4")

    if output_file is None:
        output_file = input_file.parent.joinpath(input_file.stem + "_transformed.mp4")
    
    shutil.copy(current_output_file_path, output_file)


def copy_voice_file(voice: str, voice_file: pathlib.Path):
    voice_file_path = data_folder.joinpath("text-to-speech").joinpath("input").joinpath("voice.mp3")
    
    if voice == "custom":
        shutil.copy(voice_file, voice_file_path)
    else:
        shutil.copy(resource_folder.joinpath("voices").joinpath(voice + ".mp3"), voice_file_path)


def copy_slides_file(pptx_file: pathlib.Path):
    shutil.copy(pptx_file, data_folder.joinpath("text-to-text").joinpath("input").joinpath("slides.pptx"))
    shutil.copy(pptx_file, data_folder.joinpath("video-generation").joinpath("input").joinpath("slides.pptx"))


def create_avatar_prompt_file(avatar_prompt: str):
    with open(data_folder.joinpath("avatar-generation").joinpath("input").joinpath("avatar.txt"), "w", encoding='utf-8') as f:
        f.write(avatar_prompt)


def get_voices() -> list[str]:
    return sorted([file.stem for file in resource_folder.joinpath("voices").glob("*.mp3")])


def clear_data_folder():
    shutil.rmtree("data", ignore_errors=True)
    data_folder.mkdir(parents=False, exist_ok=False)


def generate_folders():
    for step in steps:
        data_folder.joinpath(step).joinpath("input").mkdir(parents=True, exist_ok=False)
        data_folder.joinpath(step).joinpath("output").mkdir(parents=False, exist_ok=False)


if __name__ == "__main__":
    main()
