from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, QSlider, QFrame, QMessageBox, QApplication, QTextEdit, QFileDialog
from PySide6.QtCore import Qt
import pandas as pd 
import numpy as np
import sys
import os
from svm_runner import SVMRunner

class Algorithm(QMainWindow):
    def __init__(self, mode):
        super().__init__()
        self.setWindowTitle(f"{mode} Algorithm")
        self.setGeometry(400, 400, 400, 200)

        #Layout
        layout = QVBoxLayout()

        self.label = QLabel(f"Running Algorithm Mode: {mode}", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        #Run Button
        self.run_button - QPushButton(f"Run {mode}")
        self.run_button.clicked.connect(self.run_algorithm)
        layout.addWidget(self.run_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

class ChooseUploader(QMainWindow):
    #def run_svm(self):
    #    QMessageBox.information(self, "Success", "ML Algorithm run successfully! ")
    def run_algorithm(self, mode):
            #Should Open RunAlgWindow in either Test or Train mode
            self.algorithm_window = Algorithm(mode)
            self.algorithm_window.show()

    def update_status(self):
            #Enables train and test buttons if CSVs are uploaded
            if self.patient_data_path and self.diagnosis_data_path:
                self.train_button.setEnabled(True)
                self.test_button.setEnabled(True)
                self.text_display.setText(
                    f"✅ Both files uploaded! n\nPatient Data: {self.patient_data_path}\nDiagnosis Data: {self.diagnosis_data_path}"
                )

    def upload_file(self, file_type):
            file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV File", " ", "CSV Files (*.csv)")

            if file_path:
                file_name = os.path.basename(file_path)

                if file_type == "patient":
                    self.patient_data_path = file_path
                    self.patient_label.setText(f"✅ Patient Data: {file_name}")
                elif file_type == "diagnosis":
                    self.diagnosis_data_path = file_path
                    self.diagnosis_label.setText(f"✅ Diagnosis Data: {file_name}")

                self.update_status()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Patient Data Loader")
        self.setGeometry(400, 400, 400, 400)

        #uploaded files
        self.patient_data_path = None
        self.diagnosis_data_path = None

        # Layout
        layout = QVBoxLayout()


        #Patient data Upload Point
        self.patient_label = QLabel("No Patient Data Selected", self)
        self.patient_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.patient_label)

        self.patient_button = QPushButton("Upload Patient Data CSV")
        self.patient_button.clicked.connect(lambda: self.upload_file("patient"))
        layout.addWidget(self.patient_button)

        #Diagnosis Data Upload Point
        self.diagnosis_label = QLabel("No Diagnosis Data Selected", self)
        self.diagnosis_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.diagnosis_label)

        self.diagnosis_button = QPushButton("Upload Diagnosis CSV")
        self.diagnosis_button.clicked.connect(lambda: self.upload_file("diagnosis"))
        layout.addWidget(self.diagnosis_button)

        # Test & Train (should be diasabled until diagnosis and patient_data CSVs are uploaded)
        self.train_button = QPushButton("Train Algorithm")
        self.train_button.setEnabled(False)
        self.train_button.clicked.connect(self.train_algorithm)
        layout.addWidget(self.train_button)

        self.test_button = QPushButton("Test Algorithm")
        self.test_button.setEnabled(False)
        self.test_button.clicked.connect(self.test_algorithm)
        layout.addWidget(self.test_button)

        # Text Display for File Info
        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        #Creating a central widget NEWCODE
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)



        # Create buttons
        #self.train_button = QPushButton("Train")
        #self.test_button = QPushButton("Test")

        # Add buttons to layout
        #layout.addWidget(self.train_button)
        #layout.addWidget(self.test_button)

        # Set layout to the window
        #container.setLayout(layout)

        # Connect buttons to functions
        #self.train_button.clicked.connect(self.train_action)
        #self.test_button.clicked.connect(self.test_action)

    def train_algorithm(self):
       QMessageBox.information(self, "Success", "Algorithm trained successfully!")
       print("Train button clicked")
       svm = SVMRunner(self.patient_data_path, self.diagnosis_data_path)
       train_results = SVMRunner.train_and_evaluate(svm) 
       print(train_results)
       self.save_button = QPushButton("Save Trained Model")
       self.centralWidget().layout().addWidget(self.save_button)
       self.save_button.clicked.connect(lambda: self.save_model(svm))
    

    def test_algorithm(self):
       QMessageBox.information(self, "Success", "Algorithm tested successfully!")
       print("Test button clicked")
       svm = SVMRunner(self.patient_data_path, self.diagnosis_data_path)
       test_results = SVMRunner.test(svm)
    
    def save_model(self, svm):
        name = svm.save_model()
        
        QMessageBox.information(
        self,
        "Saved",
        f"Model saved successfully!\nSaved as: {name}"
    )



    #def train_algorithm(self):
    #    QMessageBox.information(self, "Success", "Algorithm trained successfully! ")    
    #def test_algorithm(self):
    #    QMessageBox.information(self, "Success", "Algorithm tested successfully! ") 


