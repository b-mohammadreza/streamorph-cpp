# Author: Mohammadreza Bahmanpour
# Copyright 2023 streamorph.live project.
# All rights reserved. Please refer to LICENSE file for more details.

src_files = ['main.cpp']

subdir('gui')

deps = [dependency('Qt6Core'), dependency('Qt6Gui'), dependency('Qt6Widgets')]

streamorph_bin = executable('streamorph'
                            , sources: src_files
                            , include_directories: inc_dirs
                            , dependencies: deps)
