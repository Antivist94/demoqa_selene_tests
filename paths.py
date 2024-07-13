from pathlib import Path


def path():
    return str(Path(__file__).parent.joinpath(f'files/photo_man.png'))
