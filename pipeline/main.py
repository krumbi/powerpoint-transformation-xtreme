import gui

from gooey import Gooey

import pathlib
import shutil

steps = ["text-to-text", "voice-cloning", "avatar-generation", "lip-sync", "video-generation"]
data_folder = pathlib.Path("data")
resource_folder = pathlib.Path("resources")


@Gooey(program_name="PowerPoint Transformation Xtreme",
       progress_regex=r"^Step (\d+)/(\d+) done$",
       progress_expr="x[0] / x[1] * 100",
       disable_progress_bar_animation=False)
def main():
    print("Running main")
    clear_data_folder()
    generate_folders()
    voices = get_voices()
    parser = gui.show_ui(voices)
    args = parser.parse_args()
    
    print(args)
    parser.error("This is a demo error message")


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
