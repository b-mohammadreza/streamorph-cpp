// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#pragma once

namespace streamorph::gui {
    class IQtWidgetsContainer {
    public:
        virtual ~IQtWidgetsContainer() = default;

    public:
        virtual void init() = 0;
        virtual void show() = 0;
    };
}
