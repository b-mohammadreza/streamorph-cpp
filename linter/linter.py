# Author: Mohammadreza Bahmanpour
# Copyright 2023 streamorph.live project.
# All rights reserved. Please refer to LICENSE file for more details.

# Removed the shebang for now

import sys
import shutil
import json5
import os

from colorama import Fore

def print_usage():
    print(Fore.CYAN+'Usage: linter.py --name <linter_cmd_name> --src <path_to_src_dir> --build <path_to_build_dir>')
    sys.exit(1)

def create_settings_path(src_path) -> str:
    path = os.path.join('linter', '.settings.json')
    return os.path.join(src_path, path)

def get_settings(settings_path) -> (str, list, list):
    # TODO: Make sure the settings path is compatible for all 
    # platforms (Windows)

    with open(settings_path, 'r', encoding='utf-8') as setting_file: 
        struct = json5.load(setting_file)
    
    return get_linter_params(struct)

def get_source_files(build_path: str):
    compile_commands_path = os.path.join(build_path, 'compile_commands.json')

    src_files: list[str] = []
    with open(compile_commands_path, 'r', encoding='utf-8') as compile_cmds_file: 
        src_files += json5.load(compile_cmds_file, object_hook=get_file)
    
    return src_files

def get_src_files_paths(src_files: list[str], build_path: str):
    src_file_paths: list[str] = []

    for src_file in src_files:
        src_file_paths.append(os.path.join(build_path, src_file))

    return src_file_paths

def get_file(obj):
    try:
        src_file = obj["file"]
    except ValueError as e:
        print(Fore.RED+f'ERROR: "file" attribute missed! \
                In "compile_commands.json" each object must define "file" attribute. Description: {e}')
        
    return src_file

def get_linter_params(struct:dict) -> (str, list, list):
    """ Returns the linter parameters, only for the active one ('enabled=true') """

    name: str = ''
    place_holders: list = []
    options: list = []

    for key in struct.keys():
        value:dict = struct[key]
        name = key

        is_enabled = False
        try:
            is_enabled = value['enabled']
        except ValueError as e:
            print(Fore.RED+f'ERROR: "enabled" setting missed! \
                  In ".settings.json" each linter must define "enabled" setting. Description: {e}')
        
        if is_enabled == False:
            continue

        try:
            place_holders = value['place_holders']
        except ValueError as e:
            print(Fore.RED+f'ERROR: "place_holders" setting missed! \
                  In ".settings.json" each linter must define "place_holders" setting. Description: {e}')
            
        try:
            options = value['options']
        except ValueError as e:
            print(Fore.RED+f'ERROR: "options" setting missed! \
                  In ".settings.json" each linter must define "options" setting. Description: {e}')
    
    return (name, place_holders, options)

def main():
    if len(sys.argv) < 5:
        print_usage()

    linter_name: str = ''
    src_path: str = ''
    build_path: str = ''

    if sys.argv[1] == '--name':
        linter_name = sys.argv[2]
    else:
        print_usage()

    if shutil.which(linter_name) is None:
        print(Fore.RED+f'ERROR: Invalid linter_name: {linter_name}')
        sys.exit(1)

    if sys.argv[3] == '--src':
        src_path = sys.argv[4]
    else:
        print_usage()

    if len(src_path) < 1:
        print(Fore.RED+f'ERROR: Invalid src_path: {src_path}')
        sys.exit(1)

    if sys.argv[5] == '--build':
        build_path = sys.argv[6]
    else:
        print_usage()

    if len(build_path) < 1:
        print(Fore.RED+f'ERROR: Invalid build_path: {build_path}')
        sys.exit(1)

    settings_path = create_settings_path(src_path)
    (name, place_holders, options) = get_settings(settings_path)

    # At this point need to replace placeholders. This task should be done in 'main()'
    # function, because all corresponding varibales to 'place_holders' are defined in
    # the 'main()' function
    # for option in options:
    #     for place_holder in place_holders:
    #         if place_holder in option:
    #             option = option.format(place_holder='1111')
    #             print(option)

    src_files = get_source_files(build_path)
    src_files = get_src_files_paths(src_files, build_path)

    # cmd: str = create_linter_cmd(name, place_holders, options, src_files)

    print(Fore.GREEN+f'DEBUG >>> variables: {vars()}')
    print(Fore.RESET, end='')

if __name__ == '__main__':
    main()
