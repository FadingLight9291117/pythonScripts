import argparse
import functools
from pathlib import Path


def get_files(directory, regex):
    return list(Path(directory).rglob(regex))


def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return f"File {file_path} not found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    parser = argparse.ArgumentParser(description="Count the number of lines in a file.")
    parser.add_argument("file_path", help="The path to the file.")
    args = parser.parse_args()

    path = args.file_path
    line_count = 0

    if (Path(path).is_dir()):
        files = get_files(path, regex="*.ets")       
        line_count = functools.reduce(
            lambda lines, file: lines + count_lines_in_file(file), 
            files,
            0,
        )
        print(f"The dir has {len(files)} files, {line_count} lines.")
    else:
        line_count = count_lines_in_file(args.file_path)
        print(f"The file has {line_count} lines.")

    

if __name__ == "__main__":
    main()