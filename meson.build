# Author: Mohammadreza Bahmanpour
# Copyright 2023 streamorph.live project.
# All rights reserved. Please refer to LICENSE file for more details.

project('streamorph'
, 'c'
, 'cpp'
, default_options:['c_std=c2x'
                    , 'cpp_std=c++20'
                    , 'b_sanitize=address,undefined'
                    , 'b_coverage=true']
, version:'0.1.0'
, license: 'GPL-3.0')

HOST_LINUX = false
HOST_WINDOWS = false

_build_machine = build_machine.system()
if _build_machine == 'linux'
    HOST_LINUX = true
endif

if _build_machine == 'windows'
    HOST_WINDOWS = true
endif

if HOST_LINUX
    inc_dirs = include_directories('include'
                                   , 'include/gui')
elif HOST_WINDOWS
    # TODO: test in Windows (need to change '/')
endif

subdir('src')
subdir('test')

if HOST_LINUX
    python_bin = find_program('python', 'python3', 'python2', required: true)
    pip_bin = find_program('pip', 'pip3', required: true)

elif HOST_WINDOWS
    python_bin = find_program('py', required: true)
endif

if HOST_LINUX
    src_root = meson.project_source_root()
    run_result = run_command(pip_bin
                            , 'install'
                            , '-r'
                            ,  src_root + '/linter/.requirements.txt'
                            , check: false)
    if run_result.returncode() != 0
        error(run_result.stderr())
    endif

    run_target('run_linter', command: [python_bin
                                        , '@SOURCE_ROOT@/linter/linter.py'
                                        , '--src'
                                        , '@SOURCE_ROOT@'
                                        , '--build'
                                        , '@BUILD_ROOT@'])

elif HOST_WINDOWS
    # TODO: test in Windows (need to change '/')
endif
