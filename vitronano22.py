import os
import sys
import json
import shutil
from re import search

def resolve_path(path):
    if getattr(sys, "frozen", False):
        #bundled mode
        resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, path))
    else:
        #normal mode
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path

#копируем файлы vitro в директории nanocad
def copy_vitro_files(files, source_path, dest_path):
    for file in files:
        full_file_name = os.path.join(source_path, file)
        shutil.copy(full_file_name, dest_path)

#определяем какая версия nanocad прописана по-умолчанию в ini файле
def get_vitroini_ver(version_list, directory):
    ini = os.path.join(directory, 'vitro.ini')
    for ver in version_list:
        with open(ini, encoding="utf-8") as file:
            if ver in file.read():
                return ver

#определяем какая версия nanaocad прописана по-умолчанию в ini файле
def get_vitroini_arch(arch_list, directory):
    ini = os.path.join(directory, 'vitro.ini')
    for arch in arch_list:
        with open(ini, encoding="utf-8") as file:
            if arch in file.read():
                return arch

#заменяем версию по-умолчанию на соответствующую в уже перенесенном vitro.ini файле 
def change_vitroini_files_ver(version_list, directory, currver):
    ini = os.path.join(directory, 'vitro.ini')
    for ver in version_list:
        if search(ver, directory):

            with open(ini, "rt", encoding="utf-8") as file:
                data = file.read()
                data = data.replace(currver, ver)

            with open(ini, "wt", encoding="utf-8") as file:
                file.write(data)

#заменяем разрядность по-умолчанию на соответствующую в уже перенесенном vitro.ini файле
def change_vitroini_files_arch(arch_list, directory, currarch):
    ini = os.path.join(directory, 'vitro.ini')
    for arch in arch_list:
        if search(arch, directory):

            with open(ini, "rt", encoding="utf-8") as file:
                data = file.read()
                data = data.replace(currarch, arch)

            with open(ini, "wt", encoding="utf-8") as file:
                file.write(data)

def search_lines(filename, word):
    lines = []
    with open(filename, "rb") as file:
        for line in file:
            lines.append(line.decode('utf-8', 'backslashreplace'))

    for line in lines:
        if word in line.lower():
            return True
    
    return False

def change_ncadini_files(directory):
    ini = os.path.join(directory, 'nCad.ini')
    word = '#include "vitro.ini"'
    
    if os.path.exists(ini):
        if search_lines(ini, word) is False:
            file = open(ini, "a+")
            file.write('\n#include "vitro.ini"')
            file.close()

#считываем настройки
with open(resolve_path("config.json"), "r") as config_file:
    config = json.load(config_file)
    #Определяем директории и версии
    vitro_path = config['vitro_path']
    nano_path = config['nano_path']
    nano_version_list = config['version_list']
    nano_arch_list = config['arch_list']

#Определяем рабочие директории и список файлов для переноса
dir_list = os.listdir(nano_path)
vitro_files = os.listdir(vitro_path)

currver = get_vitroini_ver(nano_version_list, vitro_path)

currarch = get_vitroini_arch(nano_arch_list, vitro_path)

#MAIN
def main(dir_list, nano_path, vitro_files, vitro_path, nano_version_list, nano_arch_list, currver, currarch):
    for dir in dir_list:
        full_dir_name = os.path.join(nano_path, dir)
        if os.path.isdir(full_dir_name):
            try:
                copy_vitro_files(vitro_files, vitro_path, full_dir_name)
                change_vitroini_files_ver(nano_version_list, full_dir_name, currver)
                change_vitroini_files_arch(nano_arch_list, full_dir_name, currarch)
                change_ncadini_files(full_dir_name)
            except OSError as error:
                print(error)

if __name__ == "__main__":
    main(dir_list, nano_path, vitro_files, vitro_path, nano_version_list, nano_arch_list, currver, currarch)