from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, QGridLayout
from PySide6.QtCore import Qt
from generate_data import generate_patient_data

class GenerateWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generate Data")
        self.setGeometry(550, 550, 400, 300)

        # Layout
        layout = QVBoxLayout()
        self.label = QLabel("Select options for data generation:", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 14px; font-weight: bold; color:black; margin: 10px")
        layout.addWidget(self.label)

        # Dropdowns
        self.label1 = QLabel("Select Scaling Factor:", self)
        self.label1.setAlignment(Qt.AlignLeft)
        self.label1.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin-top: 5px; margin-left: 5px;")
        layout.addWidget(self.label1)

        self.dropdown1 = QComboBox(self)
        self.dropdown1.addItems(["4", "5", "6"])
        self.dropdown1.setStyleSheet("color: black;")  # Modify with actual options
        self.label1.setStyleSheet("font-size: 12px; font-weight: bold; color: black; margin:5px")
        layout.addWidget(self.label1)
        layout.addWidget(self.dropdown1)

        self.label2 = QLabel("Select Ground Truth Size:", self)
        self.label2.setAlignment(Qt.AlignLeft)
        self.label2.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin-top: 5px; margin-left: 5px;")
        layout.addWidget(self.label2)

        self.dropdown2 = QComboBox(self)
        self.dropdown2.addItems(["Option 2A", "Option 2B", "Option 2C"])
        self.dropdown2.setStyleSheet("color: black;")  # Modify with actual options
        self.label2.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin: 1px")
        layout.addWidget(self.label2)
        layout.addWidget(self.dropdown2)

        self.label3 = QLabel("Select Ground Truth Distance:", self)
        self.label3.setAlignment(Qt.AlignLeft)
        self.label3.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin-top: 5px; margin-left: 5px;")
        layout.addWidget(self.label3)

        self.dropdown3 = QComboBox(self)
        self.dropdown3.addItems(["Option 3A", "Option 3B", "Option 3C"])
        self.dropdown3.setStyleSheet("color: black;")  # Modify with actual options
        self.label3.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin: 1px")
        layout.addWidget(self.label3)
        layout.addWidget(self.dropdown3)


        # Save Button
        self.save_button = QPushButton("Save Selections", self)
        self.save_button.setStyleSheet("background-color: #B7BFC7; font-size: 14px; font-weight: bold; padding: 10px")
        self.save_button.clicked.connect(self.save_selections)
        layout.addWidget(self.save_button)

        # Container
        container = QWidget()
        container.setLayout(layout)
        container.setStyleSheet("background-color: #E2E5E8;")
        self.setCentralWidget(container)

    def save_selections(self):
        self.selection1 = self.dropdown1.currentText()
        self.selection2 = self.dropdown2.currentText()
        self.selection3 = self.dropdown3.currentText()
        print(f"Selections saved: {self.selection1}, {self.selection2}, {self.selection3}") 