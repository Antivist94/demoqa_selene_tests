from pathlib import Path
import files


def path():
    return str(Path(__file__).parent.joinpath('files'))
