# Removed the shebang for now

import sys
import shutil
from colorama import Fore

def print_usage():
    print(Fore.CYAN+'Usage: linter.py --name <linter_cmd_name> --src <path_to_src_dir> --build <path_to_build_dir>')
    sys.exit(1)


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

    print(Fore.GREEN+f'DEBUG >>> linter_name->{linter_name}, src_path->{src_path}, build_path->{build_path}')
    print(Fore.RESET, end='')

if __name__ == '__main__':
    main()
