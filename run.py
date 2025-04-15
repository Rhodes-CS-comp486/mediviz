from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QTextEdit
from PySide6.QtCore import Qt
import pandas as pd
import sys
import os
from generate import GenerateWindow
from algorithm import ChooseUploader


class CSVUploader(QMainWindow):
    def __init__(self):  
        super().__init__()
        self.setWindowTitle("Patient Data Loader")
        self.setGeometry(500, 500, 600, 400)

        # Layout and widgets
        layout = QVBoxLayout()

        welcome_label = QLabel("MediViz")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size:30px; font-weight:bold; color: #333333; margin-top: 10px;")
        layout.addWidget(welcome_label)

        self.label = QLabel("No folder selected", self)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold; color: black; margin: 10px")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.status_label = QLabel("", self)
        self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: green; margin: 10px")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        upload_button = QPushButton("Upload Data and Run Algorithm", self)
        upload_button.setStyleSheet("""QPushButton{background-color:rgb(175, 193, 210); 
                                    font-family: "font-size: 16px; 
                                    font-weight: bold; 
                                    color: black; 
                                    padding: 10px 20px; 
                                    border: 1px solid #e0e0e0
                                    } 
                                    QPushButton:hover{background-color: #F5F8F9
                                    }""")
        upload_button.clicked.connect(self.run_algorithm) # used to be self.upload_folder
        layout.addWidget(upload_button)
        
        generate_button = QPushButton("Generate Data", self)
        generate_button.setStyleSheet("background-color:  #B7BFC7; font-size: 16px; font-weight: bold; color: black; padding: 10px; hover {background-color: #A4ABB3;}")
        generate_button.clicked.connect(self.generate_data)
        layout.addWidget(generate_button)

        #self.text_display = QTextEdit(self)
        #self.text_display.setReadOnly(True)
        #self.text_display.setStyleSheet("background-color: #F6FBFC; color: black; font-size: 12px; font-weight: normal; padding: 10px; margin: 10px")
        #layout.addWidget(self.text_display)

        # Container 
        container = QWidget()
        container.setLayout(layout)
        container.setStyleSheet("background-color: #E2E5E8;")
        self.setCentralWidget(container)


    def upload_folder(self): 
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        
        if folder_path:
            self.label.setText(f"Selected folder: {folder_path}")
            files = [f for f in os.listdir(folder_path) if f.endswith(('.csv'))]

            if not files:
                self.text_display.setText("No CSV file found in selected folder.")
                return

            all_text = " "
            success = False
            for file in files:
                file_path = os.path.join(folder_path, file)
                try:
                    if file.endswith('.csv'):
                        df = pd.read_csv(file_path)
                    else:
                        df = pd.read_excel(file_path)

                    file_text = f"\nFile: {file}\n{df.to_string(index=True)}\n{'_'*50}\n"
                    all_text += file_text
                    success = True
                except Exception as e:
                    all_text += f"\nFailed to read {file}: {e}\n"

            #self.text_display.setText(all_text)
            file_names = "\n".join(files)
            self.text_display.setText(f"Files in folder:\n{file_names}")

            if success:
                self.status_label.setText("Upload successful!")
                self.status_label.setStyleSheet("color: green;")
            else:
                self.status_label.setText("Upload failed: Errors encountered.")
                self.status_label.setStyleSheet("color: red;")
                
    def generate_data(self):
        """Opens the data generation window."""
        self.generate_window = GenerateWindow()  # Create instance of the GenerateWindow class
        self.generate_window.show()
        

    def run_algorithm(self):
        """Opens the algorithm window."""
        self.algorithm_window = ChooseUploader()
        self.algorithm_window.show()
app = QApplication(sys.argv)
window = CSVUploader()
window.show()
sys.exit(app.exec())
