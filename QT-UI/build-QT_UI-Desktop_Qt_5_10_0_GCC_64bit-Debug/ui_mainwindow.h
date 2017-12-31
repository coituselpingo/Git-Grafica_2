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
    QOpenGLWidget *sceneOpenGLWidget;
    QSpacerItem *horizontalSpacer;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *verticalSpacer_6;
    QWidget *layoutWidget1;
    QGridLayout *gridLayout_3;
    QSpacerItem *horizontalSpacer_3;
    QGridLayout *gridLayout_4;
    QSpacerItem *verticalSpacer_2;
    QComboBox *graphObjectComboBox;
    QLabel *graphObjectLabel;
    QSpacerItem *verticalSpacer_3;
    QFrame *line_3;
    QGridLayout *gridLayout_5;
    QDial *objectXDial;
    QLabel *objectXLabel;
    QGridLayout *gridLayout_6;
    QDial *objectYDial;
    QLabel *objectYLabel;
    QGridLayout *gridLayout_7;
    QDial *objectZDial;
    QLabel *objectZLabel;
    QFrame *line;
    QGridLayout *gridLayout_8;
    QSpacerItem *verticalSpacer_7;
    QPushButton *hidePushButton;
    QPushButton *modifyPushButton;
    QSpacerItem *verticalSpacer_8;
    QFrame *line_2;
    QGridLayout *gridLayout_11;
    QGridLayout *gridLayout_12;
    QSpacerItem *verticalSpacer_5;
    QSlider *zoomVerticalSlider;
    QSpacerItem *verticalSpacer_11;
    QSpacerItem *horizontalSpacer_6;
    QGridLayout *gridLayout_9;
    QLabel *povFieldLabel;
    QSpacerItem *verticalSpacer_4;
    QLCDNumber *zoomLcdNumber;
    QLabel *zoomLabel;
    QSpacerItem *verticalSpacer_9;
    QLCDNumber *povFieldLcdNumber;
    QSlider *povFieldHorizontalSlider;
    QSpacerItem *verticalSpacer_10;
    QGridLayout *gridLayout_10;
    QMenuBar *menuBar;
    QMenu *menuFile;
    QMenu *menuLoad;
    QMenu *menuSave;
    QMenu *menuEdit;
    QMenu *menuTools;
    QMenu *menuHelp;

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
        sceneOpenGLWidget = new QOpenGLWidget(layoutWidget);
        sceneOpenGLWidget->setObjectName(QStringLiteral("sceneOpenGLWidget"));
        sceneOpenGLWidget->setEnabled(true);

        gridLayout_2->addWidget(sceneOpenGLWidget, 0, 1, 1, 1);

        horizontalSpacer = new QSpacerItem(20, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer, 0, 0, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(20, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_2, 0, 2, 1, 1);


        gridLayout->addLayout(gridLayout_2, 1, 0, 1, 1);

        verticalSpacer_6 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer_6, 2, 0, 1, 1);

        layoutWidget1 = new QWidget(centralWidget);
        layoutWidget1->setObjectName(QStringLiteral("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(0, 410, 1001, 161));
        gridLayout_3 = new QGridLayout(layoutWidget1);
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

        graphObjectComboBox = new QComboBox(layoutWidget1);
        graphObjectComboBox->setObjectName(QStringLiteral("graphObjectComboBox"));

        gridLayout_4->addWidget(graphObjectComboBox, 1, 0, 1, 1);

        graphObjectLabel = new QLabel(layoutWidget1);
        graphObjectLabel->setObjectName(QStringLiteral("graphObjectLabel"));

        gridLayout_4->addWidget(graphObjectLabel, 2, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_4->addItem(verticalSpacer_3, 3, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_4, 0, 1, 1, 1);

        line_3 = new QFrame(layoutWidget1);
        line_3->setObjectName(QStringLiteral("line_3"));
        line_3->setFrameShape(QFrame::VLine);
        line_3->setFrameShadow(QFrame::Sunken);

        gridLayout_3->addWidget(line_3, 0, 2, 1, 1);

        gridLayout_5 = new QGridLayout();
        gridLayout_5->setSpacing(6);
        gridLayout_5->setObjectName(QStringLiteral("gridLayout_5"));
        objectXDial = new QDial(layoutWidget1);
        objectXDial->setObjectName(QStringLiteral("objectXDial"));

        gridLayout_5->addWidget(objectXDial, 0, 0, 1, 1);

        objectXLabel = new QLabel(layoutWidget1);
        objectXLabel->setObjectName(QStringLiteral("objectXLabel"));

        gridLayout_5->addWidget(objectXLabel, 1, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_5, 0, 3, 1, 1);

        gridLayout_6 = new QGridLayout();
        gridLayout_6->setSpacing(6);
        gridLayout_6->setObjectName(QStringLiteral("gridLayout_6"));
        objectYDial = new QDial(layoutWidget1);
        objectYDial->setObjectName(QStringLiteral("objectYDial"));

        gridLayout_6->addWidget(objectYDial, 0, 0, 1, 1);

        objectYLabel = new QLabel(layoutWidget1);
        objectYLabel->setObjectName(QStringLiteral("objectYLabel"));

        gridLayout_6->addWidget(objectYLabel, 1, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_6, 0, 4, 1, 1);

        gridLayout_7 = new QGridLayout();
        gridLayout_7->setSpacing(6);
        gridLayout_7->setObjectName(QStringLiteral("gridLayout_7"));
        objectZDial = new QDial(layoutWidget1);
        objectZDial->setObjectName(QStringLiteral("objectZDial"));

        gridLayout_7->addWidget(objectZDial, 0, 0, 1, 1);

        objectZLabel = new QLabel(layoutWidget1);
        objectZLabel->setObjectName(QStringLiteral("objectZLabel"));

        gridLayout_7->addWidget(objectZLabel, 1, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_7, 0, 5, 1, 1);

        line = new QFrame(layoutWidget1);
        line->setObjectName(QStringLiteral("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout_3->addWidget(line, 0, 6, 1, 1);

        gridLayout_8 = new QGridLayout();
        gridLayout_8->setSpacing(6);
        gridLayout_8->setObjectName(QStringLiteral("gridLayout_8"));
        verticalSpacer_7 = new QSpacerItem(20, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_8->addItem(verticalSpacer_7, 0, 0, 1, 1);

        hidePushButton = new QPushButton(layoutWidget1);
        hidePushButton->setObjectName(QStringLiteral("hidePushButton"));

        gridLayout_8->addWidget(hidePushButton, 1, 0, 1, 1);

        modifyPushButton = new QPushButton(layoutWidget1);
        modifyPushButton->setObjectName(QStringLiteral("modifyPushButton"));

        gridLayout_8->addWidget(modifyPushButton, 2, 0, 1, 1);

        verticalSpacer_8 = new QSpacerItem(20, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_8->addItem(verticalSpacer_8, 3, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_8, 0, 7, 1, 1);

        line_2 = new QFrame(layoutWidget1);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);

        gridLayout_3->addWidget(line_2, 0, 9, 1, 1);

        gridLayout_11 = new QGridLayout();
        gridLayout_11->setSpacing(6);
        gridLayout_11->setObjectName(QStringLiteral("gridLayout_11"));
        gridLayout_12 = new QGridLayout();
        gridLayout_12->setSpacing(6);
        gridLayout_12->setObjectName(QStringLiteral("gridLayout_12"));
        gridLayout_12->setSizeConstraint(QLayout::SetFixedSize);
        verticalSpacer_5 = new QSpacerItem(15, 35, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_12->addItem(verticalSpacer_5, 2, 0, 1, 1);

        zoomVerticalSlider = new QSlider(layoutWidget1);
        zoomVerticalSlider->setObjectName(QStringLiteral("zoomVerticalSlider"));
        sizePolicy.setHeightForWidth(zoomVerticalSlider->sizePolicy().hasHeightForWidth());
        zoomVerticalSlider->setSizePolicy(sizePolicy);
        zoomVerticalSlider->setOrientation(Qt::Vertical);

        gridLayout_12->addWidget(zoomVerticalSlider, 1, 0, 1, 1);

        verticalSpacer_11 = new QSpacerItem(15, 5, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_12->addItem(verticalSpacer_11, 0, 0, 1, 1);

        horizontalSpacer_6 = new QSpacerItem(20, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_12->addItem(horizontalSpacer_6, 1, 1, 1, 1);


        gridLayout_11->addLayout(gridLayout_12, 0, 1, 1, 1);

        gridLayout_9 = new QGridLayout();
        gridLayout_9->setSpacing(6);
        gridLayout_9->setObjectName(QStringLiteral("gridLayout_9"));
        povFieldLabel = new QLabel(layoutWidget1);
        povFieldLabel->setObjectName(QStringLiteral("povFieldLabel"));

        gridLayout_9->addWidget(povFieldLabel, 6, 0, 1, 1);

        verticalSpacer_4 = new QSpacerItem(20, 5, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_9->addItem(verticalSpacer_4, 0, 0, 1, 1);

        zoomLcdNumber = new QLCDNumber(layoutWidget1);
        zoomLcdNumber->setObjectName(QStringLiteral("zoomLcdNumber"));

        gridLayout_9->addWidget(zoomLcdNumber, 1, 0, 1, 1);

        zoomLabel = new QLabel(layoutWidget1);
        zoomLabel->setObjectName(QStringLiteral("zoomLabel"));

        gridLayout_9->addWidget(zoomLabel, 3, 0, 1, 1);

        verticalSpacer_9 = new QSpacerItem(20, 5, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_9->addItem(verticalSpacer_9, 8, 0, 1, 1);

        povFieldLcdNumber = new QLCDNumber(layoutWidget1);
        povFieldLcdNumber->setObjectName(QStringLiteral("povFieldLcdNumber"));

        gridLayout_9->addWidget(povFieldLcdNumber, 5, 0, 1, 1);

        povFieldHorizontalSlider = new QSlider(layoutWidget1);
        povFieldHorizontalSlider->setObjectName(QStringLiteral("povFieldHorizontalSlider"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(povFieldHorizontalSlider->sizePolicy().hasHeightForWidth());
        povFieldHorizontalSlider->setSizePolicy(sizePolicy1);
        povFieldHorizontalSlider->setOrientation(Qt::Horizontal);

        gridLayout_9->addWidget(povFieldHorizontalSlider, 7, 0, 1, 1);

        verticalSpacer_10 = new QSpacerItem(20, 5, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_9->addItem(verticalSpacer_10, 4, 0, 1, 1);

        gridLayout_10 = new QGridLayout();
        gridLayout_10->setSpacing(6);
        gridLayout_10->setObjectName(QStringLiteral("gridLayout_10"));

        gridLayout_9->addLayout(gridLayout_10, 9, 0, 1, 1);


        gridLayout_11->addLayout(gridLayout_9, 0, 0, 1, 1);


        gridLayout_3->addLayout(gridLayout_11, 0, 10, 1, 1);

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
#ifndef QT_NO_WHATSTHIS
        actionExit->setWhatsThis(QString());
#endif // QT_NO_WHATSTHIS
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
        graphObjectLabel->setText(QApplication::translate("MainWindow", "Object on Scene", nullptr));
        objectXLabel->setText(QApplication::translate("MainWindow", "Rotate   X", nullptr));
        objectYLabel->setText(QApplication::translate("MainWindow", "Rotate   Y", nullptr));
        objectZLabel->setText(QApplication::translate("MainWindow", "Rotate   Z", nullptr));
        hidePushButton->setText(QApplication::translate("MainWindow", "Hide", nullptr));
        modifyPushButton->setText(QApplication::translate("MainWindow", "Modify", nullptr));
        povFieldLabel->setText(QApplication::translate("MainWindow", "POV Field", nullptr));
        zoomLabel->setText(QApplication::translate("MainWindow", "Zoom Ratio", nullptr));
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
