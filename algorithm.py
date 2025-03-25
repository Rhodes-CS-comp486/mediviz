from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, QSlider, QFrame, QMessageBox, QApplication
from PySide6.QtCore import Qt
import pandas as pd 
import numpy as np
import sys


class RunAlgorithmWindow(QMainWindow):
    def run_svm(self):
        QMessageBox.information(self, "Success", "ML Algorithm run successfully! ")
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Run Algorithm")
        self.setGeometry(400, 400, 400, 400)

        # Layout
        layout = QVBoxLayout()

        self.label = QLabel("Do you want to train or test the algorithm?", self)
        self.label.setAlignment(Qt.AlignCenter)

        # Dropdown Box
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(["Train", "Test"])
        layout.addWidget(self.dropdown)
        self.dropdown.setEnabled(True)
        self.dropdown.currentIndexChanged.connect(self.option_selected)

        # Create buttons
        self.train_button = QPushButton("Train")
        self.test_button = QPushButton("Test")

        # Add buttons to layout
        layout.addWidget(self.train_button)
        layout.addWidget(self.test_button)

        # Set layout to the window
        self.setLayout(layout)

        # Connect buttons to functions
        self.train_button.clicked.connect(self.train_action)
        self.test_button.clicked.connect(self.test_action)

    def train_action(self):
        print("Train button clicked")

    def test_action(self):
        print("Test button clicked")

        # Container
        container = QWidget()
        self.setCentralWidget(container)

    def option_selected(self):  
        selected_option = self.dropdown.currentText()
        if selected_option == "Train":
            self.train_algorithm()
        else:
            self.test_algorithm()



    def train_algorithm(self):
        QMessageBox.information(self, "Success", "Algorithm trained successfully! ")    
    def test_algorithm(self):
        QMessageBox.information(self, "Success", "Algorithm tested successfully! ") 

