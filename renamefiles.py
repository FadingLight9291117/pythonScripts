from pathlib import Path
import shutil
import click


def change_filename(file, origin, target):
    """
        批量替换文件名中特定的符号
        比如：将'/tmp/2020.10.11test.md'更改为'/tmp/2020-10-11test.md'
    """
    file_path = Path(file)
    file_stem = file_path.stem
    file_suffix = file_path.suffix
    file_stem = target.join(file_stem.split(origin))

    new_filename = (file_path.parent / file_stem).__str__() + file_suffix
    shutil.move(file, new_filename)


@click.command()
@click.argument('path')
@click.option('-o', '--pattern', type=str, default='', help="需要替换的字符")
@click.option('-s', '--chars', type=str, default='', help="替换成的字符")
def main(path, pattern, chars):
    for file in Path(path).glob('*'):
        change_filename(file, pattern, chars)


if __name__ == '__main__':
    main()
