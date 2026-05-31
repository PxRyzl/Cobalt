#! /usr/bin/env python3
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout, QGroupBox, QMessageBox, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from manual import ManualWindow
from automatic import AutoWindow
from inf import InfWindow
#from inf import InfWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cobalt')
        self.setWindowState(Qt.WindowMaximized)

        app.setWindowIcon(QIcon("assets/logo.svg"))

        container = QWidget()
        container.setMaximumWidth(940)
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)

        outer_layout = QHBoxLayout()
        outer_layout.addStretch()
        outer_layout.addWidget(container)
        outer_layout.addStretch()

        central = QWidget()
        central.setLayout(outer_layout)
        self.setCentralWidget(central)

        # MANUAL
        group_man = QGroupBox('Manual Conversion')
        layout_group_man = QVBoxLayout(group_man)
        group_man.setLayout=(layout_group_man)

        label_man = QLabel('Recommended: \n This conversion would need the user to manually select each type of cursor.')
        label_man.setAlignment(Qt.AlignCenter)

        button_man = QPushButton('MANUAL')
        button_man.clicked.connect(self.open_manual_window)

        layout_group_man.addWidget(label_man)
        layout_group_man.addWidget(button_man)

        # AUTOMATIC
        group_auto = QGroupBox('Automatic Conversion')
        layout_group_auto = QVBoxLayout(group_auto)
        group_auto.setLayout=(layout_group_auto)

        label_auto = QLabel('WARNING: \n THIS WILL AUTOMATICALLY CONVERT ALL THE CURSOR AVAILABLE IN A DIRECTORY WITHOUT \n NEEDING TO MANUALLY SELECT EACH ONE. BUT THE NAME OF THE CURSOR MUST BE CORRECT, \n CHECK README for more information')
        label_auto.setAlignment(Qt.AlignCenter)

        button_auto = QPushButton('AUTOMATIC')
        button_auto.clicked.connect(self.open_auto_window)

        layout_group_auto.addWidget(label_auto)
        layout_group_auto.addWidget(button_auto)

        # INF File
        group_inf = QGroupBox('INF Conversion')
        layout_group_inf = QVBoxLayout(group_inf)
        group_inf.setLayout=(layout_group_inf)

        label_inf = QLabel('This conversion would need the cursor to be included with an inf file and will automatically convert the cursor.')
        label_inf.setAlignment(Qt.AlignCenter)

        button_inf = QPushButton('INF')
        button_inf.clicked.connect(self.open_inf_window)

        layout_group_inf.addWidget(label_inf)
        layout_group_inf.addWidget(button_inf)

        # Layout order
        layout.addWidget(group_man)
        layout.addWidget(group_auto)
        layout.addWidget(group_inf)

    def open_manual_window(self):
        self.manual_window = ManualWindow(self)
        self.manual_window.show()
        self.hide()

    def open_auto_window(self):
        self.auto_window = AutoWindow(self)
        self.auto_window.show()
        self.hide()

    def open_inf_window(self):
        self.inf_window = InfWindow(self)
        self.inf_window.show()
        self.hide()



app = QApplication()

window = MainWindow()
window.show()

app.exec()
