TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
        main.cpp \
        unimodalAlgorithms.cpp


win32:CONFIG(release, debug|release): LIBS += -L$$PWD/parser/ -lparser
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/parser/ -lparserd

INCLUDEPATH += $$PWD/parser/include
DEPENDPATH += $$PWD/parser/include

win32-g++:CONFIG(release, debug|release): PRE_TARGETDEPS += $$PWD/parser/libparser.a
else:win32-g++:CONFIG(debug, debug|release): PRE_TARGETDEPS += $$PWD/parser/libparserd.a
else:win32:!win32-g++:CONFIG(release, debug|release): PRE_TARGETDEPS += $$PWD/parser/parser.lib
else:win32:!win32-g++:CONFIG(debug, debug|release): PRE_TARGETDEPS += $$PWD/parser/parserd.lib

HEADERS += \
    IIterationObserver.h \
    unimodalAlgorithms.h
