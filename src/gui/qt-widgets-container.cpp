// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include "qt-widgets-container.h"

using namespace streamorph::gui;

void QtWidgetsContainer::init() {
    _mainWindow = std::make_unique<QtMainWindowForm>(nullptr);
}

void QtWidgetsContainer::show() {
    _mainWindow->show();
}
