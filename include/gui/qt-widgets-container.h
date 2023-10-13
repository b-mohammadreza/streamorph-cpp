// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include <memory>
#include <QtWidgets/QPushButton>

#include "qt-widgets-interface.h"
#include "qt-main-window-widget.h"

namespace streamorph::gui {
    class QtWidgetsContainer : public IQtWidgetsContainer {
    public:
        void init() override;
        void show() override;
    
    private:
        std::unique_ptr<QtMainWindowForm> _mainWindow = nullptr;
    };
}