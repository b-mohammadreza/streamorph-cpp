// Author: Mohammadreza Bahmanpour
// Copyright 2023 streamorph.live project.
// All rights reserved. Please refer to LICENSE file for more details.

#include "ui_main-window.h"

class QtMainWindowForm : public QMainWindow {
    Q_OBJECT;

public:
    explicit QtMainWindowForm(QWidget* parent = nullptr);

private slots:

private:
    Ui::MainWindow _mainWindowUi;
};
