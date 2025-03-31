from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, QSlider, QFrame, QMessageBox, QLineEdit
from PySide6.QtCore import Qt
from visualize_lesion import visualize_patient
import pandas as pd

class VisualizeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualize Data")
        self.setGeometry(400, 400, 400, 400)
        
        # Layout
        layout = QVBoxLayout()
        
        self.label = QLabel("Select which Patient you would like to visualize:", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 14px; font-weight: bold; color: black; margin: 10px")
        layout.addWidget(self.label)  
        
        # **Input Box**
        self.input_label = QLabel("Enter a value:", self)
        layout.addWidget(self.input_label)

        self.input_box = QLineEdit(self)  # Create the input box
        self.input_box.setPlaceholderText("Type here...")  
        layout.addWidget(self.input_box)
        
        # **Connect Enter key to save function**
        self.input_box.returnPressed.connect(self.save_input)  
        
         # **Save Button**
        self.save_input_button = QPushButton("Visualize Patient Lesion", self)
        self.save_input_button.clicked.connect(self.save_input)  # Connect button to save input
        layout.addWidget(self.save_input_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        

    def save_input(self):
        """Save input text to a variable when Enter is pressed or button is clicked."""
        self.user_input_value = self.input_box.text()  # Store input in a variable
        
        if not self.user_input_value.isdigit():
            QMessageBox.critical(self, "Invalid Input", "Please enter a valid number to select a patient.")
            return
        
        QMessageBox.information(self, "Input Saved!", f"Visualizing lesion for patient: {self.user_input_value}...")
        df = pd.read_csv("patient_data/patients_data.csv")
        visualize_patient(df, self.user_input_value, parent_window=self)

