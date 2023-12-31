import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QFileDialog, QTextEdit, QErrorMessage, QComboBox
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
        self.env_input.setPlaceholderText("Enter environment name")

        self.pkg_label = QLabel('Additional Packages')
        self.pkg_label.setStyleSheet("font-weight: bold")
        self.pkg_input = QLineEdit()
        self.pkg_input.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")
        self.pkg_input.setPlaceholderText(
            "Enter additional packages (comma-separated)")

        self.port_label = QLabel('Port Number')
        self.port_label.setStyleSheet("font-weight: bold")
        self.port_input = QLineEdit()
        self.port_input.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")
        self.port_input.setPlaceholderText("Enter port number")

        self.shell_label = QLabel('Shell')
        self.shell_label.setStyleSheet("font-weight: bold")
        self.shell_dropdown = QComboBox()
        self.shell_dropdown.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")
        self.shell_dropdown.addItem("bash")
        self.shell_dropdown.addItem("cmd.exe")
        self.shell_dropdown.addItem("powershell")
        self.shell_dropdown.addItem("zsh")
        self.shell_dropdown.addItem("fish")

        self.conda_label = QLabel('Conda Path')
        self.conda_label.setStyleSheet("font-weight: bold")
        self.conda_input = QLineEdit()
        self.conda_input.setStyleSheet(
            "background-color: #9D73FA; font-weight: bold;")
        self.conda_input.setPlaceholderText("Enter path to conda executable")

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
        # Add shell label and dropdown box to layout
        form_layout.addWidget(self.shell_label)
        form_layout.addWidget(self.shell_dropdown)

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
        env_name = self.env_input.text()
        additional_packages = self.pkg_input.text()
        port_number = self.port_input.text()
        conda_path = self.conda_input.text()
        # Retrieve the selected shell from the dropdown box
        selected_shell = self.shell_dropdown.currentText()

        # Initialize Conda
        init_conda_cmd = f'source {conda_path} && conda init {selected_shell} && conda activate {env_name}'

    def kill_jupyter_server(self):
        pass

    def browse_for_conda(self):
        # Open file dialog to select conda executable
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(
            self, "Select Conda Executable", "", "Executable Files (*.exe *.sh *.bat)", options=options)

        if file == "":
            return
        if not os.path.isfile(file):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('Invalid file selected')
            return

        # Set the selected file path in the conda_input QLineEdit
        self.conda_input.setText(file)


if __name__ == '__main__':
    init()
    app = QApplication(sys.argv)
    jupyter = JupyterManager()
    jupyter.show()
    sys.exit(app.exec_())
