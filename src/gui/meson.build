# Author: Mohammadreza Bahmanpour
# Copyright 2023 streamorph.live project.
# All rights reserved. Please refer to LICENSE file for more details.

qt6 = import('qt6')

qt6_dep = dependency('qt6', modules: ['Core', 'Gui', 'Widgets'])
deps += [qt6_dep]

moc_files = qt6.compile_moc(sources : []
                            , headers: qt_moc_headers
                            , extra_args: []
                            , include_directories: inc_dirs
                            , dependencies: deps)

subdir('qt-resources')

qrc_files = qt6.compile_resources(sources : qt_resources
                                                   , extra_args: [])

subdir('qt-ui')

ui_files = qt6.compile_ui(sources : qt_uis
                                           , extra_args: [])

gui_src_files = files('qt-app-wrapper.cpp'
                                 , 'qt-widgets-container.cpp'
                                 , 'qt-main-window-widget.cpp')

src_files += [gui_src_files]
src_files += [moc_files] + [qrc_files] + [ui_files]
