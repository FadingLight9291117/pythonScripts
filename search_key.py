from pathlib import Path
import re
import os


def replace_txt(content: str, txt='QingServiceContext.QingCommonService()'):
    new_txt = txt.replace(txt,  txt[:-2] + '(getContext())')
    content = content.replace(txt, new_txt)
    return content


def search_file(filepath, pattern=''):
    count = 0
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            count += len(re.findall(pattern, content))

    except Exception as e:
        print(file_path)
        print(e)
        exit(1)
    
    if count > 5:
        print(str(filepath) + ': ' + str(count))

    return count


def search_in_dir(dir_path):
    excludes = ['build', 'oh_modules']
    suffixes = ['.ets', '.tx']

    for path in os.listdir(dir_path):
        full_path: Path = Path(dir_path) / path
        if Path(full_path).name in excludes:
            continue

        if full_path.is_dir():
            for i in search_in_dir(full_path):
                yield i
        else:
            if full_path.suffix in suffixes:
                yield full_path


if __name__ == '__main__':
    project_path = r'C:\Users\wps\Projects\moffice'
    txt = r'KText\('

    count = 0
    for file_path in search_in_dir(project_path):
        count += search_file(filepath=file_path, pattern=txt)

    print(f'count: {count}')