from PySide2.QtCore import Qt, Slot, QDir, QSettings
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QPushButton, QFileDialog, QInputDialog, \
    QLineEdit, QHBoxLayout, QVBoxLayout, QLabel

import sys


class Application(QWidget):
    pathToWTF = "_retail_/WTF/Account"

    def __init__(self):
        QWidget.__init__(self)
        self.config = QSettings("Nierhain", "WTFUtils")

        self.layout = QHBoxLayout()


        self.quit = QPushButton("Quit")

        # Options
        self.accountname = QLineEdit(self.config.value("accountname"))
        self.realm = QLineEdit(self.config.value("realm"))
        self.character = QLineEdit(self.config.value("character"))
        self.wowPath = QLineEdit(self.config.value("wowPath"))
        self.wowPath.picker = QPushButton('Select')
        self.copyPath = QLineEdit(self.config.value("copyPath"))
        self.copyPath.picker = QPushButton('Select')
        self.backupPath = QLineEdit(self.config.value("backupPath"))
        self.backupPath.picker = QPushButton('Select')

        self.options = QVBoxLayout()

        self.options.setMargin(10)
        self.options.addWidget(QLabel("WoW path"))
        self.options.addWidget(self.wowPath)
        self.options.addWidget(self.wowPath.picker)
        self.options.addWidget(QLabel("Character settings path"))
        self.options.addWidget(self.copyPath)
        self.options.addWidget(self.copyPath.picker)
        self.options.addWidget(QLabel("Account name"))
        self.options.addWidget(self.accountname)
        self.options.addWidget(QLabel("Realm"))
        self.options.addWidget(self.realm)
        self.options.addWidget(QLabel("Character name"))
        self.options.addWidget(self.character)
        self.options.addWidget(QLabel("Backup folder path"))
        self.options.addWidget(self.backupPath)
        self.options.addWidget(self.backupPath.picker)
        self.options.addStretch()
        self.options.addWidget(self.quit)


        self.layout.addLayout(self.options)
        self.setLayout(self.layout)

        self.realm.editingFinished.connect(self.setRealm)
        self.quit.clicked.connect(self.quit_application)
        self.copyPath.picker.clicked.connect(self.setCopyPath)
        self.wowPath.picker.clicked.connect(self.setWowPath)
        self.backupPath.picker.clicked.connect(self.setBackupPath)

    @Slot()
    def setRealm(self):
        self.config.setValue("realm", self.realm.text())

    @Slot()
    def setCharacter(self):
        self.config.setValue("character", self.realm.text())

    @Slot()
    def setAccountname(self):
        self.config.setValue("accountname", self.realm.text())

    @Slot()
    def setCopyPath(self):
        self.config.setValue("copyPath", QFileDialog.getExistingDirectory(self, "select character settings directory"))
        self.copyPath.setText(self.config.value("copyPath"))
    @Slot()
    def setWowPath(self):
        self.config.setValue("wowPath", QFileDialog.getExistingDirectory(self, "select wow directory"))
        self.wowPath.setText(self.config.value("wowPath"))
    @Slot()
    def setBackupPath(self):
        self.config.setValue("backupPath", QFileDialog.getExistingDirectory(self, "select backup directory"))
        self.backupPath.setText(self.config.value("backupPath"))


    @Slot()
    def quit_application(self):
        QApplication.quit()


class MainWindow(QMainWindow):

    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("WTFUtils - by Nierhain")

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Application()
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
