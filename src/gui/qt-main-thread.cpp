// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include "qt-main-thread.h"

std::shared_ptr<QtMainThreadWrapper> QtMainThreadWrapper::getInstance() {
    if (_instance == nullptr)
        _instance = std::make_shared<QtMainThreadWrapper>();

        return _instance;
}
