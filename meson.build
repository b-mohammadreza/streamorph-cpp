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
, version: '0.1.0'
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

subdir('include')
subdir('src')
subdir('test')
subdir('linter')
