// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include <memory>
#include <QtWidgets/QApplication>
#include <QtWidgets/QPushButton>

#include "qt-widgets-interface.h"

namespace streamorph::gui {
    class QtWidgetsContainer : public IQtWidgetsContainer {
    public:
        void init(int argc, char* argv[]) override;
        void show() override;
        int exec() override;
    
    private:
        std::unique_ptr<QApplication> _qtApp = nullptr;
        std::unique_ptr<QPushButton> _btnHWorld = nullptr;
    };
}