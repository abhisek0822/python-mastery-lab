from pathlib import Path
import os


def pwd():
    return Path.cwd()


def ls():
    files = []

    for item in Path.cwd().iterdir():
        files.append(item.name)

    return files


def cd(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print("Directory does not exist.")

    except NotADirectoryError:
        print("Not a directory.")


def mkdir(directory):
    try:
        Path(directory).mkdir(exist_ok=True)
        print(f"Directory '{directory}' created.")
    except Exception as error:
        print(error)


def touch(filename):
    try:
        Path(filename).touch(exist_ok=True)
        print(f"File '{filename}' created.")
    except Exception as error:
        print(error)


def cat(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return "File not found."

    except IsADirectoryError:
        return "Cannot read a directory."


def clear():
    os.system("cls" if os.name == "nt" else "clear")