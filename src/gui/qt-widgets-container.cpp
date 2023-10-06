// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include "qt-widgets-container.h"

using namespace streamorph::gui;

void QtWidgetsContainer::init() {
    _btnHWorld = std::make_unique<QPushButton>("Hello World!");
}

void QtWidgetsContainer::show() {
    _btnHWorld->show();
}
