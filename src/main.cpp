// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include "qt-main-thread.h"

using namespace streamorph::gui;

int main(int argc, char* argv[]) {
    auto qt_main_thread = QtMainThreadWrapper::getInstance(argc, argv);

    return qt_main_thread->run();
}
