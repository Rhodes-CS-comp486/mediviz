from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
import pandas as pd
import sys

class CSVUploader(QMainWindow):
    def __init__(self):  
        super().__init__()
        self.setWindowTitle("CSV File Uploader")
        self.setGeometry(300,300,400,200)

        # Layout and widgets
        layout = QVBoxLayout()
        self.label = QLabel("No file selected", self)
        layout.addWidget(self.label) 

        upload_button = QPushButton("Upload CSV", self)
        upload_button.clicked.connect(self.upload_csv)
        layout.addWidget(upload_button)

        # Container 
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def upload_csv(self): 
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.label.setText(f"Selected file: {file_path}")
            try:
                df = pd.read_csv(file_path)
                print(df.head())
            except Exception as e:
                self.label.setText(f"Failed to read file: {e}")

app = QApplication(sys.argv)
window = CSVUploader()
window.show()
sys.exit(app.exec())
