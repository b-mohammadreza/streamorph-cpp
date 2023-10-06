// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include "qt-app-wrapper.h"
#include "qt-widgets-container.h"

using namespace streamorph::gui;

std::shared_ptr<QApplicationWrapper> QApplicationWrapper::_instance = nullptr;

std::shared_ptr<QApplicationWrapper> QApplicationWrapper::getInstance(int argc, char* argv[]) {
    if (_instance == nullptr) {
        _instance = std::shared_ptr<QApplicationWrapper>(new QApplicationWrapper());
        _instance->_qtApp = std::make_unique<QApplication>(argc, argv);
        _instance->_qtWidgetsContainer = std::make_unique<QtWidgetsContainer>();

        initWidgetsContainer();
    }

    return _instance;
}

void QApplicationWrapper::initWidgetsContainer() {
    _instance->_qtWidgetsContainer->init();
    _instance->_qtWidgetsContainer->show();
}

int QApplicationWrapper::exec() {
    return _instance->_qtApp->exec();
}