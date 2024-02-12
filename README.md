# streamorph-cpp

Current list of dependency packages:
(This list is not going to be maintained after using conan. This list will be removed after all the packages handled using conan) 
PKGS="make
      cmake
      meson
      ninja
      gcc
      gcc-c++
      qt6-qtbase-devel
      qt6-qttools
      qt6-qttools-devel
      qt6-designer
      gtest
      gtest-devel
      gcovr
      libasan
      libubsan
      gstreamer1
      gstreamer1-devel
      gstreamer1-plugins-base-devel
      gtk3-devel
      clang
      clang-tools-extra"


conan needs to be installed
- Create a virtual environment dedicated to conan installation
--> python -m venv ~/conan
- Activate the conan virtual environment (Linux) (TODO: what is the acivation command in Windows?)
--> source ~/conan/bin/activate
- Install conan
--> pip install conan

How conan executable will be found by meson?
I do not think if the following scrips are required:
- setenv.sh will activate conan virtual environment
(You only need to run setenv.sh if you are going to add a new dependency to the project or if you want to build the project on a new host.)
- unsetenv.sh will deactivate conan virtual environment