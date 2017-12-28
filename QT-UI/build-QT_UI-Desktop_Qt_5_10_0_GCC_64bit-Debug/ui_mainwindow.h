/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.10.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDial>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QOpenGLWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionExit;
    QAction *actionObject;
    QAction *actionModel;
    QAction *actionObject_2;
    QAction *actionModel_2;
    QAction *actionPredefined_Forms;
    QAction *actionPredefined_Scenes;
    QAction *actionObject_3;
    QAction *actionModel_3;
    QAction *actionScene_POV;
    QAction *actionAbout;
    QWidget *centralWidget;
    QWidget *layoutWidget;
    QGridLayout *gridLayout;
    QSpacerItem *verticalSpacer;
    QGridLayout *gridLayout_2;
    QOpenGLWidget *openGLWidget;
    QSpacerItem *horizontalSpacer;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *verticalSpacer_6;
    QWidget *widget;
    QGridLayout *gridLayout_3;
    QSpacerItem *horizontalSpacer_3;
    QGridLayout *gridLayout_4;
    QSpacerItem *verticalSpacer_2;
    QComboBox *comboBox;
    QLabel *label_4;
    QSpacerItem *verticalSpacer_3;
    QFrame *line_3;
    QGridLayout *gridLayout_5;
    QDial *dial;
    QLabel *label;
    QGridLayout *gridLayout_6;
    QDial *dial_2;
    QLabel *label_2;
    QGridLayout *gridLayout_7;
    QDial *dial_3;
    QLabel *label_3;
    QFrame *line;
    QGridLayout *gridLayout_8;
    QSpacerItem *verticalSpacer_7;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QSpacerItem *verticalSpacer_8;
    QFrame *line_2;
    QHBoxLayout *horizontalLayout;
    QGridLayout *gridLayout_9;
    QSpacerItem *verticalSpacer_4;
    QLCDNumber *lcdNumber;
    QLabel *label_5;
    QSpacerItem *verticalSpacer_5;
    QSlider *verticalSlider;
    QSpacerItem *horizontalSpacer_4;
    QMenuBar *menuBar;
    QMenu *menuFile;
    QMenu *menuLoad;
    QMenu *menuSave;
    QMenu *menuEdit;
    QMenu *menuTools;
    QMenu *menuHelp;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->setWindowModality(Qt::WindowModal);
        MainWindow->resize(1000, 600);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        actionExit = new QAction(MainWindow);
        actionExit->setObjectName(QStringLiteral("actionExit"));
        actionObject = new QAction(MainWindow);
        actionObject->setObjectName(QStringLiteral("actionObject"));
        actionModel = new QAction(MainWindow);
        actionModel->setObjectName(QStringLiteral("actionModel"));
        actionObject_2 = new QAction(MainWindow);
        actionObject_2->setObjectName(QStringLiteral("actionObject_2"));
        actionModel_2 = new QAction(MainWindow);
        actionModel_2->setObjectName(QStringLiteral("actionModel_2"));
        actionPredefined_Forms = new QAction(MainWindow);
        actionPredefined_Forms->setObjectName(QStringLiteral("actionPredefined_Forms"));
        actionPredefined_Scenes = new QAction(MainWindow);
        actionPredefined_Scenes->setObjectName(QStringLiteral("actionPredefined_Scenes"));
        actionObject_3 = new QAction(MainWindow);
        actionObject_3->setObjectName(QStringLiteral("actionObject_3"));
        actionModel_3 = new QAction(MainWindow);
        actionModel_3->setObjectName(QStringLiteral("actionModel_3"));
        actionScene_POV = new QAction(MainWindow);
        actionScene_POV->setObjectName(QStringLiteral("actionScene_POV"));
        actionAbout = new QAction(MainWindow);
        actionAbout->setObjectName(QStringLiteral("actionAbout"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        layoutWidget = new QWidget(centralWidget);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(0, 0, 1001, 411));
        gridLayout = new QGridLayout(layoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        verticalSpacer = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer, 0, 0, 1, 1);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        openGLWidget = new QOpenGLWidget(layoutWidget);
        openGLWidget->setObjectName(QStringLiteral("openGLWidget"));
        openGLWidget->setEnabled(true);

        gridLayout_2->addWidget(openGLWidget, 0, 1, 1, 1);

        horizontalSpacer = new QSpacerItem(20, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer, 0, 0, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(20, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_2, 0, 2, 1, 1);

        verticalSpacer_6 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_2->addItem(verticalSpacer_6, 1, 1, 1, 1);


        gridLayout->addLayout(gridLayout_2, 1, 0, 1, 1);

        widget = new QWidget(centralWidget);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(0, 410, 1001, 141));
        gridLayout_3 = new QGridLayout(widget);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        gridLayout_3->setContentsMargins(0, 0, 0, 0);
        horizontalSpacer_3 = new QSpacerItem(20, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_3->addItem(horizontalSpacer_3, 0, 0, 1, 1);

        gridLayout_4 = new QGridLayout();
        gridLayout_4->setSpacing(6);
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        verticalSpacer_2 = new QSpacerItem(20, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_4->addItem(verticalSpacer_2, 0, 0, 1, 1);

        comboBox = new QComboBox(widget);
        comboBox->setObjectName(QStringLiteral("comboBox"));

        gridLayout_4->addWidget(comboBox, 1, 0, 1, 1);

        label_4 = new QLabel(widget);
        label_4->setObjectName(QStringLiteral("label_4"));

        gridLayout_4->addWidget(label_4, 2, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_4->addItem(verticalSpacer_3, 3, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_4, 0, 1, 1, 1);

        line_3 = new QFrame(widget);
        line_3->setObjectName(QStringLiteral("line_3"));
        line_3->setFrameShape(QFrame::VLine);
        line_3->setFrameShadow(QFrame::Sunken);

        gridLayout_3->addWidget(line_3, 0, 2, 1, 1);

        gridLayout_5 = new QGridLayout();
        gridLayout_5->setSpacing(6);
        gridLayout_5->setObjectName(QStringLiteral("gridLayout_5"));
        dial = new QDial(widget);
        dial->setObjectName(QStringLiteral("dial"));

        gridLayout_5->addWidget(dial, 0, 0, 1, 1);

        label = new QLabel(widget);
        label->setObjectName(QStringLiteral("label"));

        gridLayout_5->addWidget(label, 1, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_5, 0, 3, 1, 1);

        gridLayout_6 = new QGridLayout();
        gridLayout_6->setSpacing(6);
        gridLayout_6->setObjectName(QStringLiteral("gridLayout_6"));
        dial_2 = new QDial(widget);
        dial_2->setObjectName(QStringLiteral("dial_2"));

        gridLayout_6->addWidget(dial_2, 0, 0, 1, 1);

        label_2 = new QLabel(widget);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout_6->addWidget(label_2, 1, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_6, 0, 4, 1, 1);

        gridLayout_7 = new QGridLayout();
        gridLayout_7->setSpacing(6);
        gridLayout_7->setObjectName(QStringLiteral("gridLayout_7"));
        dial_3 = new QDial(widget);
        dial_3->setObjectName(QStringLiteral("dial_3"));

        gridLayout_7->addWidget(dial_3, 0, 0, 1, 1);

        label_3 = new QLabel(widget);
        label_3->setObjectName(QStringLiteral("label_3"));

        gridLayout_7->addWidget(label_3, 1, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_7, 0, 5, 1, 1);

        line = new QFrame(widget);
        line->setObjectName(QStringLiteral("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout_3->addWidget(line, 0, 6, 1, 1);

        gridLayout_8 = new QGridLayout();
        gridLayout_8->setSpacing(6);
        gridLayout_8->setObjectName(QStringLiteral("gridLayout_8"));
        verticalSpacer_7 = new QSpacerItem(20, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_8->addItem(verticalSpacer_7, 0, 0, 1, 1);

        pushButton = new QPushButton(widget);
        pushButton->setObjectName(QStringLiteral("pushButton"));

        gridLayout_8->addWidget(pushButton, 1, 0, 1, 1);

        pushButton_2 = new QPushButton(widget);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));

        gridLayout_8->addWidget(pushButton_2, 2, 0, 1, 1);

        verticalSpacer_8 = new QSpacerItem(20, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_8->addItem(verticalSpacer_8, 3, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_8, 0, 7, 1, 1);

        line_2 = new QFrame(widget);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);

        gridLayout_3->addWidget(line_2, 0, 8, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        gridLayout_9 = new QGridLayout();
        gridLayout_9->setSpacing(6);
        gridLayout_9->setObjectName(QStringLiteral("gridLayout_9"));
        verticalSpacer_4 = new QSpacerItem(20, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_9->addItem(verticalSpacer_4, 0, 0, 1, 1);

        lcdNumber = new QLCDNumber(widget);
        lcdNumber->setObjectName(QStringLiteral("lcdNumber"));

        gridLayout_9->addWidget(lcdNumber, 1, 0, 1, 1);

        label_5 = new QLabel(widget);
        label_5->setObjectName(QStringLiteral("label_5"));

        gridLayout_9->addWidget(label_5, 2, 0, 1, 1);

        verticalSpacer_5 = new QSpacerItem(20, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_9->addItem(verticalSpacer_5, 3, 0, 1, 1);


        horizontalLayout->addLayout(gridLayout_9);

        verticalSlider = new QSlider(widget);
        verticalSlider->setObjectName(QStringLiteral("verticalSlider"));
        verticalSlider->setOrientation(Qt::Vertical);

        horizontalLayout->addWidget(verticalSlider);


        gridLayout_3->addLayout(horizontalLayout, 0, 9, 1, 1);

        horizontalSpacer_4 = new QSpacerItem(20, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_3->addItem(horizontalSpacer_4, 0, 10, 1, 1);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1000, 25));
        menuFile = new QMenu(menuBar);
        menuFile->setObjectName(QStringLiteral("menuFile"));
        menuLoad = new QMenu(menuFile);
        menuLoad->setObjectName(QStringLiteral("menuLoad"));
        menuSave = new QMenu(menuFile);
        menuSave->setObjectName(QStringLiteral("menuSave"));
        menuEdit = new QMenu(menuBar);
        menuEdit->setObjectName(QStringLiteral("menuEdit"));
        menuTools = new QMenu(menuBar);
        menuTools->setObjectName(QStringLiteral("menuTools"));
        menuHelp = new QMenu(menuBar);
        menuHelp->setObjectName(QStringLiteral("menuHelp"));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuFile->menuAction());
        menuBar->addAction(menuEdit->menuAction());
        menuBar->addAction(menuTools->menuAction());
        menuBar->addAction(menuHelp->menuAction());
        menuFile->addAction(menuLoad->menuAction());
        menuFile->addAction(menuSave->menuAction());
        menuFile->addAction(actionExit);
        menuLoad->addAction(actionObject);
        menuLoad->addAction(actionModel);
        menuSave->addAction(actionObject_2);
        menuSave->addAction(actionModel_2);
        menuEdit->addAction(actionObject_3);
        menuEdit->addAction(actionModel_3);
        menuEdit->addAction(actionScene_POV);
        menuTools->addAction(actionPredefined_Forms);
        menuTools->addAction(actionPredefined_Scenes);
        menuHelp->addAction(actionAbout);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "G2-F", nullptr));
        actionExit->setText(QApplication::translate("MainWindow", "Exit", nullptr));
        actionObject->setText(QApplication::translate("MainWindow", "Object", nullptr));
        actionModel->setText(QApplication::translate("MainWindow", "Model", nullptr));
        actionObject_2->setText(QApplication::translate("MainWindow", "Object", nullptr));
        actionModel_2->setText(QApplication::translate("MainWindow", "Model", nullptr));
        actionPredefined_Forms->setText(QApplication::translate("MainWindow", "Predefined Objects", nullptr));
        actionPredefined_Scenes->setText(QApplication::translate("MainWindow", "Predefined Scenes", nullptr));
        actionObject_3->setText(QApplication::translate("MainWindow", "Object", nullptr));
        actionModel_3->setText(QApplication::translate("MainWindow", "Model", nullptr));
        actionScene_POV->setText(QApplication::translate("MainWindow", "Scene POV", nullptr));
        actionAbout->setText(QApplication::translate("MainWindow", "About", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "Object on Scene", nullptr));
        label->setText(QApplication::translate("MainWindow", "Rotate   X", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "Rotate   Y", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "Rotate   Z", nullptr));
        pushButton->setText(QApplication::translate("MainWindow", "Hide", nullptr));
        pushButton_2->setText(QApplication::translate("MainWindow", "Modify", nullptr));
        label_5->setText(QApplication::translate("MainWindow", "Zoom Ratio", nullptr));
        menuFile->setTitle(QApplication::translate("MainWindow", "File", nullptr));
        menuLoad->setTitle(QApplication::translate("MainWindow", "Load", nullptr));
        menuSave->setTitle(QApplication::translate("MainWindow", "Save", nullptr));
        menuEdit->setTitle(QApplication::translate("MainWindow", "Edit", nullptr));
        menuTools->setTitle(QApplication::translate("MainWindow", "Tools", nullptr));
        menuHelp->setTitle(QApplication::translate("MainWindow", "Help", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
