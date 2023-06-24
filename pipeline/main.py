import sys
from time import sleep
from gooey import Gooey, GooeyParser
import pathlib


@Gooey(program_name="PowerPoint Transformation Xtreme",
       progress_regex=r"^Step (\d+)/(\d+) done$",
       progress_expr="x[0] / x[1] * 100",
       disable_progress_bar_animation=False)
def main():
    parser = GooeyParser()
    parser.add_argument(
        "pptx_file",
        metavar="PPTX file",
        type=pathlib.Path,
        help="name of the file to read",
        widget="FileChooser",
    )
    parser.add_argument(
        "output_file",
        metavar="Output file",
        type=pathlib.Path,
        help="name of the file to write",
        widget="FileSaver",
    )
    parser.add_argument(
        "text_prompt",
        metavar="Text prompt",
        type=str,
        help="Addition to text prompt in order to customize style",
    )
    parser.add_argument(
        "avatar_prompt",
        metavar="Avatar prompt",
        default="professor with glasses",
        type=str,
        help="Addition to avatar prompt in order to customize style",
    )
    parser.add_argument(
        "language",
        metavar="Language",
        choices=["en", "de (not implemented yet)"],
        default="en",
        help="Language of the text of the video",
    )
    args = parser.parse_args()

    for i in range(10):
        print("progress: {}/{}".format(i + 1, 10))
        sys.stdout.flush()
        sleep(1)
        print("Other message")
        sys.stdout.flush()
        sleep(1)


if __name__ == "__main__":
    main()
