from pathlib import Path

file = 'photo_man.png'


def path(file_name):
    return str(Path(__file__).parent.joinpath(f'files/{file_name}'))
