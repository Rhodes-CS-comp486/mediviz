from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QTextEdit
from PySide6.QtCore import Qt
import pandas as pd
import sys

class CSVUploader(QMainWindow):
    def __init__(self):  
        super().__init__()
        self.setWindowTitle("CSV File Uploader")
        self.setGeometry(500,500,600,400)

        # Layout and widgets
        layout = QVBoxLayout()

        self.label = QLabel("No file selected", self)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold; color: black; margin: 10px")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label) 

        upload_button = QPushButton("Upload CSV", self)
        upload_button.setStyleSheet("background-color:  #B7BFC7; font-size: 16px; font-weight: bold; color: black; padding: 10px; hover {background-color: #A4ABB3;}")
        upload_button.clicked.connect(self.upload_csv)
        layout.addWidget(upload_button)

        # Container 
        container = QWidget()
        container.setLayout(layout)
        container.setStyleSheet("background-color: #E2E5E8;")
        self.setCentralWidget(container)

        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        self.text_display.setStyleSheet("background-color: #F6FBFC; color: black; font-size: 12px; font-weight: normal; padding: 10px; margin: 10px")
        layout.addWidget(self.text_display)

    def upload_csv(self): 
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.label.setText(f"Selected file: {file_path}")
            try:
                df = pd.read_csv(file_path)
                # We can add checks for the file here (if df is null, check if values are not 0 or 1)
                csv_text = df.to_string(index=True)
                self.text_display.setText(csv_text)
            except Exception as e:
                self.label.setText(f"Failed to read file: {e}")

app = QApplication(sys.argv)
window = CSVUploader()
window.show()
sys.exit(app.exec())
