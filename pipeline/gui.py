from gooey import GooeyParser
import pathlib

def show_ui(voices: list[str]):
    parser = GooeyParser()
    parser.add_argument(
        "pptx_file",
        metavar="PPTX file",
        type=pathlib.Path,
        help="name of the file to read",
        widget="FileChooser",
    )
    parser.add_argument(
        "--output_file",
        metavar="Output file",
        type=pathlib.Path,
        help="name of the file to write",
        widget="FileSaver",
    )
    parser.add_argument(
        "--text_prompt",
        metavar="Text prompt",
        type=str,
        help="Addition to text prompt in order to customize style",
    )
    parser.add_argument(
        "openai_api_key",
        metavar="OpenAI API key",
        type=str,
        help="Key for OpenAI API",
    )
    parser.add_argument(
        "dreamstudio_api_key",
        metavar="DreamStudio API key",
        type=str,
        help="Key for DreamStudio API",
    )
    parser.add_argument(
        "avatar_prompt",
        metavar="Avatar prompt",
        default="professor with glasses",
        type=str,
        help="Avatar prompt in order to customize style",
    )
    parser.add_argument(
        "language",
        metavar="Language",
        choices=["en", "de (not implemented yet)"],
        default="en",
        help="Language of the text of the video",
    )
    parser.add_argument(
        "voice",
        metavar="Voice",
        choices=voices + ["custom"],
        default=voices[0],
        help="Language of the text of the video",
    )
    parser.add_argument(
        "--voice_file",
        metavar="Voice file",
        type=pathlib.Path,
        required=False,
        help="Voice mp3 file. Only necessary when custom voice is selected",
        widget="FileChooser",
    )
    
    return parser