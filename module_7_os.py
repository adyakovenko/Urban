import os
import time


def is_good_path(path):
    return (len(path) == 1 or path[2] != '.') and '__' not in path


def is_good_string(name):
    return name[0] != '.' and '__' not in name


def get_data_tree():
    data_tree = []
    for root, _, files in os.walk('.'):
        if is_good_path(root):
            root_files = []
            for name in files:
                if is_good_string(name):
                    root_files.append(name)
            if len(root_files) > 0:
                data_tree.append([root, root_files])
    return data_tree

def print_files_info(project_path, data_tree):
    for folder, files in data_tree:
        if folder != []:
            for file in files:
                filepath = os.path.join(project_path, folder[2::], file)
                filetime = os.path.getmtime(filepath)
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
                filesize = os.path.getsize(filepath)
                parent_dir = os.path.dirname(filepath)
                print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

os.chdir('.')
project_path = os.getcwd()
data_tree = get_data_tree()
print_files_info(project_path, data_tree)
