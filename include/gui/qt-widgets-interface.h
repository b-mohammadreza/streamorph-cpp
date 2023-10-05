// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#pragma once

namespace streamorph::gui {
    class IQtWidgetsContainer {
    public:
        virtual void init(int argc, char* argv[]) = 0;
        virtual void show() = 0;
        virtual int exec() = 0;
    };
}
