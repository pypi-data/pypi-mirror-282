import subprocess
import pathlib


class Converter:

    @staticmethod
    def convert_model(
        input_file: str, output_file: str, blender_path="blender"
    ) -> None:
        SCRIPT_PATH = pathlib.Path(__file__).parent / "blender_scripts" / "main.py"

        blender_command = [
            blender_path,
            "-b",
            "-noaudio",
            "--python",
            SCRIPT_PATH.resolve().as_posix(),
            "--",
            input_file,
            output_file,
        ]

        subprocess.run(blender_command)
