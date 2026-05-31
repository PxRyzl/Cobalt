from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout, QGroupBox, QMessageBox, QHBoxLayout, QGridLayout, QFileDialog, QLineEdit
from PySide6.QtCore import Qt
from core.inf_conversion import InfConversion

class loadingWindow(QMainWindow):
    def __init__(self, n):
        super().__init__()
        self.setWindowTitle('Process Completed')

        in_container = QWidget()
        self.setCentralWidget(in_container)
        layout_in = QVBoxLayout(in_container)

        label_in = QLabel('Your cursor have been converted\nIt has been put into ~/icons')
        label_in.setAlignment(Qt.AlignCenter)

        layout_in.addWidget(label_in)

class InfWindow(QMainWindow):

    def __init__(self, main):
        super().__init__()
        self.main = main

        self.setWindowTitle('Cobalt')

        container = QWidget()
        container.setMinimumWidth(940)
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)

        outer_layout = QHBoxLayout()
        outer_layout.addStretch()
        outer_layout.addWidget(container)
        outer_layout.addStretch()

        central = QWidget()
        central.setLayout(outer_layout)
        self.setCentralWidget(central)

        # Name and Description
        group_desc = QGroupBox('Create Your Cursor Theme')
        layout_group_desc = QGridLayout(group_desc)
        group_desc.setLayout=(layout_group_desc)

        label_name = QLabel("Name")
        label_desc = QLabel("Comment")

        self.line_name = QLineEdit()
        self.line_com = QLineEdit()

        self.window = []

        layout_group_desc.addWidget(label_name, 0, 0)
        layout_group_desc.addWidget(label_desc, 1, 0)
        layout_group_desc.addWidget(self.line_name,  0, 1)
        layout_group_desc.addWidget(self.line_com,  1, 1)

        # Cursor Selection
        group_cursor = QGroupBox('INF Conversion')
        layout_group_cursor = QGridLayout(group_cursor)
        group_cursor.setLayout=(layout_group_cursor)

        label = QLabel('Select the inf file')
        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)
        browse = QPushButton('Browse')
        browse.clicked.connect(self.file_dialog)

        layout_group_cursor.addWidget(label, 0, 0)
        layout_group_cursor.addWidget(self.file_path, 1,0)
        layout_group_cursor.addWidget(browse, 2, 0)

        # Back and Continue Button
        button_container = QWidget()
        button_container_layout = QHBoxLayout(button_container)

        back_button = QPushButton('Back')
        back_button.clicked.connect(self.back_to_main)

        continue_button = QPushButton('Continue')
        continue_button.clicked.connect(self.continue_button_pressed)

        back_button.setFixedWidth(80)
        continue_button.setFixedWidth(80)

        button_container_layout.addWidget(back_button)
        button_container_layout.addStretch()
        button_container_layout.addWidget(continue_button)

        # Layout order
        layout.addWidget(group_desc)
        layout.addWidget(group_cursor)
        layout.addStretch()
        layout.addWidget(button_container)

    def file_dialog(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select INF File", "", "INF File (*.inf);;All Files (*)")

        if file:
            self.file_path.setText(file)

    def continue_button_pressed(self):
        theme_name = self.line_name.text()
        theme_com = self.line_com.text()
        file_path = self.file_path.text()
        InfConversion(file_path, theme_name, theme_com)

        window = loadingWindow(self)
        self.window.append(window)
        window.show()

    def back_to_main(self):
        self.main.show()
        self.close()














