// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include "qt-main-thread.h"
#include "qt-widgets-container.h"

using namespace streamorph::gui;

std::shared_ptr<QtMainThreadWrapper> QtMainThreadWrapper::_instance = nullptr;

std::shared_ptr<QtMainThreadWrapper> QtMainThreadWrapper::getInstance(int argc, char* argv[]) {
    if (_instance == nullptr) {
        _instance = std::shared_ptr<QtMainThreadWrapper>(new QtMainThreadWrapper());
        _instance->_qtWidgetsContainer = std::make_unique<QtWidgetsContainer>();

        initWidgetsContainer(argc, argv);
    }

    return _instance;
}

void QtMainThreadWrapper::initWidgetsContainer(int argc, char* argv[]) {
    _instance->_qtWidgetsContainer->init(argc, argv);
    _instance->_qtWidgetsContainer->show();
}

int QtMainThreadWrapper::run() {
    return _instance->_qtWidgetsContainer->exec();
}