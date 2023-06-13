import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QFileDialog, QTextEdit
from PyQt5.QtCore import pyqtSignal, Qt
from colorama import init


class JupyterManager(QWidget):
    def __init__(self):
        super().__init__()

        # Input Fields
        self.env_label = QLabel('Environment Name')
        self.env_label.setStyleSheet("font-weight: bold")
        self.env_input = QLineEdit()
        self.env_input.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")

        self.pkg_label = QLabel('Additional Packages')
        self.pkg_label.setStyleSheet("font-weight: bold")
        self.pkg_input = QLineEdit()
        self.pkg_input.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")

        self.port_label = QLabel('Port Number')
        self.port_label.setStyleSheet("font-weight: bold")
        self.port_input = QLineEdit()
        self.port_input.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")

        self.conda_label = QLabel('Conda Path')
        self.conda_label.setStyleSheet("font-weight: bold")
        self.conda_input = QLineEdit()
        self.conda_input.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")

        self.init_ui()

    def init_ui(self):
        # Browse button for conda executable
        self.browse_button = QPushButton('Browse')
        self.browse_button.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")
        self.browse_button.clicked.connect(self.browse_for_conda)

        # Create and launch button
        self.create_button = QPushButton('Create and Launch')
        self.create_button.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")
        self.create_button.clicked.connect(
            self.create_env_and_launch_jupyter)

        # Kill button
        self.kill_button = QPushButton('Kill Jupyter Server')
        self.kill_button.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")
        self.kill_button.clicked.connect(self.kill_jupyter_server)

        # Text output field
        self.text_output = QTextEdit()
        self.text_output.setStyleSheet(
            "background-color: #F060C3; font-weight: bold;")

        # Add labels and input fields to layout
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.env_label)
        form_layout.addWidget(self.env_input)
        form_layout.addWidget(self.pkg_label)
        form_layout.addWidget(self.pkg_input)
        form_layout.addWidget(self.port_label)
        form_layout.addWidget(self.port_input)
        form_layout.addWidget(self.conda_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.conda_input)
        hbox.addWidget(self.browse_button)
        form_layout.addLayout(hbox)

        # Add buttons to layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.kill_button)

        # Add form and buttons to main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.text_output)

        # Set main layout and window properties
        self.setLayout(main_layout)
        self.setWindowTitle('Jupyter Manager')
        self.setGeometry(300, 300, 500, 500)
        # Set main layout and window properties
        self.setLayout(main_layout)
        # set background color
        self.setStyleSheet("background-color: #332EF0;")
        self.setWindowTitle('Jupyter Manager')
        self.setGeometry(300, 300, 500, 500)
        self.show()

    def create_env_and_launch_jupyter(self):
        pass

    def kill_jupyter_server(self):
        pass

    def browse_for_conda(self):
        pass


if __name__ == '__main__':
    init()
    app = QApplication(sys.argv)
    jupyter = JupyterManager()
    jupyter.show()
    sys.exit(app.exec_())
