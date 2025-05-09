from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, QSlider, QFrame, QMessageBox, QApplication, QTextEdit, QFileDialog
from PySide6.QtCore import Qt
import pandas as pd 
import numpy as np
import sys
import os
from svm_runner import SVMRunner
from results_dashboard import ResultsWindow

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
        self.run_button = QPushButton(f"Run {mode}")
        self.run_button.clicked.connect(self.run_algorithm)
        layout.addWidget(self.run_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

######class ChooseUploader(QMainWindow)#######
class ChooseUploader(QWidget):
    #def run_svm(self):
    #    QMessageBox.information(self, "Success", "ML Algorithm run successfully! ")
    
    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)
    
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        #self.setWindowTitle("Patient Data Loader")
        #self.setGeometry(400, 400, 400, 400)

        #uploaded files
        self.patient_data_path = None
        self.diagnosis_data_path = None

        # Layout
        self.layout = QVBoxLayout()
        layout = self.layout

        back_button = QPushButton("Back to Home")
        back_button.setFixedWidth(80)
        back_button.setStyleSheet("""
    QPushButton {
        background-color: rgb(118, 149, 177);
        font-family: 'Trebuchet MS';
        font-size: 8px;
        font-weight: bold;
        color: white;
        padding: 10px;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
    }
    QPushButton:hover {
        background-color: #ececec;
        color: black;
    }
""")
        back_button.clicked.connect(self.go_to_home)
        layout.addWidget(back_button)

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
        self.train_button = QPushButton("Train and Test Algorithm")
        self.train_button.setEnabled(False)
       
        self.train_button.clicked.connect(self.train_and_test_algorithm)
        layout.addWidget(self.train_button)

        self.test_button = QPushButton("Re-Test Algorithm")
        self.test_button.setEnabled(False)
      
        self.test_button.clicked.connect(self.test_algorithm)
        layout.addWidget(self.test_button)

        # Text Display for File Info
        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        #Creating a central widget NEWCODE
        #container = QWidget()
        #container.setLayout(layout)
        #self.setCentralWidget(container)
        
        self.show_results_button = QPushButton("Visualize Results")
        self.show_results_button.setVisible(False)
        self.show_results_button.clicked.connect(self.show_results)
        layout.addWidget(self.show_results_button)

        self.setLayout(layout)
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

    

    def train_and_test_algorithm(self):
       QMessageBox.information(self, "Success", "Algorithm trained successfully!")
       print("Train button clicked")
       svm = SVMRunner(self.patient_data_path, self.diagnosis_data_path)
       train_results, y_true, y_pred = SVMRunner.train_and_test(svm) 
       self.show_results_button.setVisible(True)
       self.last_report = train_results
       self.last_y_true = y_true
       self.last_y_pred = y_pred
       print(train_results)
       
         # Create the save button if it doesn't exist yet
       if not hasattr(self, 'save_button'):
        self.save_button = QPushButton("Save Model")
        self.save_button.clicked.connect(lambda: self.save_model(svm))
 
         # Add to layout if not already present
        if self.save_button not in [self.layout.itemAt(i).widget() for i in range(self.layout.count())]:
           self.layout.addWidget(self.save_button)
 
       self.show_results_button.setText("Visualize Training Results")
       self.save_button.clicked.connect(lambda: self.save_model(svm))
       self.svm_model = svm.model 
       
    

    def test_algorithm(self):
       print("Test button clicked")
       svm = SVMRunner(self.patient_data_path, self.diagnosis_data_path)
       test_results, y_true, y_pred = SVMRunner.test(svm)
       QMessageBox.information(self, "Success", "Algorithm tested successfully!")
       print(test_results)
       self.show_results_button.setVisible(True)
       self.last_report = test_results
       self.last_y_true = y_true
       self.last_y_pred = y_pred
       self.show_results_button.setText("Visualize Testing Results")
       self.svm_model = svm.model
       
    
    def show_results(self):
        self.results_window = ResultsWindow(self.last_report, self.last_y_true, self.last_y_pred, model=self.svm_model )
        self.results_window.show()
    
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


