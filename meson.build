project('streamorph', 'c', 'cpp'
, default_options:['c_std=c20','cpp_std=c++20']
, version:'0.1.0')

# TODO: test in Windows (is '/' working in Windows?)
executable('streamorph', 'src/main.cpp')

# TODO: test in Windows (is '.exe' required?)
python_bin = find_program('python', 'python3', 'python2', required: true)

# TODO: test in Windows (is '/' working in Windows?)
run_target('run_linter', command: [python_bin
                                    , '@SOURCE_ROOT@/linter/linter.py'
                                    , '--name'
                                    , 'clang-tidy'
                                    , '--src'
                                    , '@SOURCE_ROOT@'
                                    , '--build'
                                    , '@BUILD_ROOT@'])
