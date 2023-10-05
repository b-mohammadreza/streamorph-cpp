// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include <memory>
#include "qt-widgets-interface.h"

namespace streamorph::gui {
    
    class IQtWidgetsContainer;
    class QtMainThreadWrapper {
    public:
        static std::shared_ptr<QtMainThreadWrapper> getInstance(int argc, char* argv[]);
        int run();

    private:
        QtMainThreadWrapper() = default;
        static void initWidgetsContainer(int argc, char* argv[]);

    private:
        static std::shared_ptr<QtMainThreadWrapper> _instance;
        std::unique_ptr<IQtWidgetsContainer> _qtWidgetsContainer = nullptr;
    };
}