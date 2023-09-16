# Author: Mohammadreza Bahmanpour
# Copyright 2023 streamorph.live project
# All rights reserved. Please refer to LICENSE file for details

# Removed the shebang for now

import sys
import shutil
import json
import os

from colorama import Fore

def print_usage():
    print(Fore.CYAN+'Usage: linter.py --name <linter_cmd_name> --src <path_to_src_dir> --build <path_to_build_dir>')
    sys.exit(1)

def build_settings_path(src_path) -> str:
    path = os.path.join('linter', '.settings.json')
    return os.path.join(src_path, path)

def load_settings(settings_path) -> (str, list, list):
    # TODO: Make sure the settings path is compatible for all 
    # platforms (Windows)

    with open(settings_path, 'r') as setting_file: 
        (name, place_holders, options) = json.load(setting_file, object_hook=get_linter_params)
    
    return (name, place_holders, options)

def get_linter_params(struct:dict) -> (str, list, list):
    """ Returns the only active linter parameters """

    name: str = ''
    place_holders: list = []
    options: list = []

    print(Fore.GREEN+f'DEBUG >>> get_linter_params(): struct->{struct}')
    print(Fore.RESET, end='')

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

    settings_path = build_settings_path(src_path)
    (name, place_holders, options) = load_settings(settings_path)

    print(Fore.GREEN+f'DEBUG >>> variables: {vars()}')
    print(Fore.RESET, end='')

if __name__ == '__main__':
    main()
