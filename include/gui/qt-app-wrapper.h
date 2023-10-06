// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include <memory>
#include <QtWidgets/QApplication>

namespace streamorph::gui {
    class IQtWidgetsContainer;

    class QApplicationWrapper {
    public:
        static std::shared_ptr<QApplicationWrapper> getInstance(int argc, char* argv[]);
        int exec();

    private:
        QApplicationWrapper() = default;
        static void initWidgetsContainer();

    private:
        static std::shared_ptr<QApplicationWrapper> _instance;
        std::unique_ptr<QApplication> _qtApp = nullptr;
        std::unique_ptr<IQtWidgetsContainer> _qtWidgetsContainer;
    };
}