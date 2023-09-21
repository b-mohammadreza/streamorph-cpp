# Author: Mohammadreza Bahmanpour
# Copyright 2023 streamorph.live project.
# All rights reserved. Please refer to LICENSE file for more details.

project('streamorph', 'c', 'cpp'
, default_options:['c_std=c20','cpp_std=c++20']
, version:'0.1.0')

__build_machine = build_machine.system()

if __build_machine == 'linux'
    executable('streamorph', 'src/main.cpp')
elif __build_machine == 'windows'
    # TODO: test in Windows (need to change '/')
endif

if __build_machine == 'linux'
    python_bin = find_program('python', 'python3', 'python2', required: true)
elif __build_machine == 'windows'
    # TODO: test in Windows (is '.exe' required?)
endif

if __build_machine == 'linux'
    run_target('run_linter', command: [python_bin
                                        , '@SOURCE_ROOT@/linter/linter.py'
                                        , '--src'
                                        , '@SOURCE_ROOT@'
                                        , '--build'
                                        , '@BUILD_ROOT@'])
elif __build_machine == 'windows'
    # TODO: test in Windows (need to change '/')
endif
