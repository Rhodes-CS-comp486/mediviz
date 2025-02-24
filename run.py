import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit
from PySide6.QtCore import Qt
import file_loader
from svm_runner import SVMRunner

class CSVUploader(QMainWindow):
    def __init__(self):  
        super().__init__()
        self.setWindowTitle("Patient Data Loader")
        self.setGeometry(500, 500, 600, 400)

        # Layout and widgets
        layout = QVBoxLayout()

        self.label = QLabel("No folder selected", self)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold; color: black; margin: 10px")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.status_label = QLabel("", self)
        self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: green; margin: 10px")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        upload_button = QPushButton("Upload Patient Data", self)
        upload_button.setStyleSheet("background-color:  #B7BFC7; font-size: 16px; font-weight: bold; color: black; padding: 10px;")
        upload_button.clicked.connect(self.upload_folder)
        layout.addWidget(upload_button)

        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        self.text_display.setStyleSheet("background-color: #F6FBFC; color: black; font-size: 12px; font-weight: normal; padding: 10px; margin: 10px")
        layout.addWidget(self.text_display)

        # Container 
        container = QWidget()
        container.setLayout(layout)
        container.setStyleSheet("background-color: #E2E5E8;")
        self.setCentralWidget(container)

    def upload_folder(self):
        """Handles patient data loading and runs SVM."""
        lesion_matrices, labels, error = file_loader.load_patient_data()
        
        if error:
            self.text_display.setText(error)
            self.status_label.setText("Error")
            self.status_label.setStyleSheet("color: red;")
            return
        
        self.label.setText("Patient data loaded successfully.")
        self.status_label.setText("Processing...")
        self.status_label.setStyleSheet("color: blue;")

        # Run SVM
        svm_runner = SVMRunner(lesion_matrices, labels)
        results = svm_runner.train_and_evaluate()

        self.text_display.setText(results)
        self.status_label.setText("SVM Training Completed!")
        self.status_label.setStyleSheet("color: green;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CSVUploader()
    window.show()
    sys.exit(app.exec())
