from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QTextEdit, QHBoxLayout, QStackedWidget
from PySide6.QtCore import Qt
import pandas as pd
import sys
import os
from generate import GenerateWindow
from algorithm import ChooseUploader


class CSVUploader(QMainWindow):
    def __init__(self, stacked_widget):  
        super().__init__()
        self.setWindowTitle("Patient Data Loader")
        self.setGeometry(500, 500, 600, 400)
        self.stacked_widget = stacked_widget

        # Layout and widgets
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        welcome_layout = QVBoxLayout()
        welcome_layout.setSpacing(0)

        welcome_label1 = QLabel("welcome to")
        welcome_label1.setAlignment(Qt.AlignCenter)
        welcome_label1.setStyleSheet("font-size:15px; font-weight:bold; color: rgb(43, 85, 122);")
        welcome_layout.addWidget(welcome_label1)

        welcome_label2 = QLabel("MediViz")
        welcome_label2.setAlignment(Qt.AlignCenter)
        welcome_label2.setStyleSheet("font-size:45px; font-weight:bold; color:rgb(28, 57, 82);")
        welcome_layout.setContentsMargins(0,0,0,40)
        welcome_layout.addWidget(welcome_label2)

        layout.addLayout(welcome_layout)


        #descrip = QTextEdit()
        #descrip.setReadOnly(True)
        #descrip.setStyleSheet("font-size: 12px; color:rgb(43, 85, 122);")
        #descrip.setText(
        #    "How to use...\n\n"
        #    "1. If you have your own data, select 'Upload Data and Run Algorithm'."
        #    "2. If you would like to generate synthetic data, select 'Generate Data'."
        #    "3. Once the data has been generated, you can then upload it and run the algorithm."
        #)
        #layout.addWidget(descrip)

        faq_button = QPushButton("Instructions and FAQs", self)
        faq_button.setStyleSheet("""QPushButton{background-color: rgb(162, 191, 215); 
                                        font-size: 16px; 
                                        font-weight: bold; 
                                        color: black; 
                                        padding: 10px; 
                                        border: 1px solid #e0e0e0}
                                        QPushButton:hover{background-color: #F5F8F9
                                        }""")
        faq_button.clicked.connect(self.faq_page)
        layout.addWidget(faq_button)
        
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        button_layout.setAlignment(Qt.AlignCenter)


        upload_button = QPushButton("Upload Data and Run Algorithm", self)
        upload_button.setFixedWidth(350)
        upload_button.setStyleSheet("""QPushButton{background-color:rgb(118, 149, 177); 
                                    font-size: 16px; 
                                    font-weight: bold; 
                                    color: black; 
                                    padding: 10px; 
                                    border: 1px solid #e0e0e0
                                    } 
                                    QPushButton:hover{background-color: #F5F8F9
                                    }""")
        upload_button.clicked.connect(self.run_algorithm) # used to be self.upload_folder
        button_layout.addWidget(upload_button)
        
        generate_button = QPushButton("Generate Data", self)
        generate_button.setFixedWidth(350)
        generate_button.setStyleSheet("""QPushButton{background-color: rgb(118, 149, 177); 
                                        font-size: 16px; 
                                        font-weight: bold; 
                                        color: black; 
                                        padding: 10px; 
                                        border: 1px solid #e0e0e0}
                                        QPushButton:hover{background-color: #F5F8F9
                                        }""")
        generate_button.clicked.connect(self.generate_data)
        button_layout.addWidget(generate_button)

        layout.addLayout(button_layout)

        

        #self.label = QLabel("(No Folder Selected)", self)
        #self.label.setStyleSheet("font-size: 16px; font-weight: bold; color: black; margin: 10px")
        #self.label.setAlignment(Qt.AlignCenter)
        #layout.addWidget(self.label)

        #self.status_label = QLabel("", self)
        #self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: green; margin: 10px")
        #self.status_label.setAlignment(Qt.AlignCenter)
        #layout.addWidget(self.status_label)

        #self.text_display = QTextEdit(self)
        #self.text_display.setReadOnly(True)
        #self.text_display.setStyleSheet("background-color: #F6FBFC; color: black; font-size: 12px; font-weight: normal; padding: 10px; margin: 10px")
        #layout.addWidget(self.text_display)

        # Container 
        container = QWidget()
        container.setLayout(layout)
        container.setStyleSheet("background-color: rgb(255,255,255);")
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

    def faq_page(self):
        self.stacked_widget.setCurrentIndex(1)

class FAQ_Page(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

        top_row_layout = QHBoxLayout()
        top_row_layout.setAlignment(Qt.AlignTop)

        back_button = QPushButton("Back to Home")
        back_button.setFixedWidth(125)
        back_button.clicked.connect(self.go_to_home)
        top_row_layout.addWidget(back_button, alignment=Qt.AlignLeft)

        layout.addLayout(top_row_layout)

        second_row_layout = QHBoxLayout()
        

        header_layout = QVBoxLayout()
        header_layout.setSpacing(0)
        header_layout.setContentsMargins(0,0,0,0)

        header_label1 = QLabel("MediViz")
        header_label1.setAlignment(Qt.AlignHCenter)
        header_label1.setStyleSheet("font-size:45px; font-weight:bold; color:rgb(28, 57, 82);")
        header_layout.addWidget(header_label1)

        header_label2 = QLabel("MediViz Instructions and Frequently Asked Questions")
        header_label2.setAlignment(Qt.AlignHCenter)
        header_label2.setStyleSheet("font-size:15px; font-weight:bold; color: rgb(43, 85, 122);")
        header_layout.addWidget(header_label2)

        second_row_layout.setAlignment(Qt.AlignHCenter)
        second_row_layout.addLayout(header_layout)
        layout.addLayout(second_row_layout)

        instruc = QLabel("1) Do you have patient data?\n  --> If yes, then select 'Upload Data and Run Algorithm'.\n  --> If no, then select 'Generate Data' to create synthetic patient data. \n\n2) Once you have generated data, go back and select 'Upload Data and Run Algorithm'."
        )
        instruc.setAlignment(Qt.AlignLeft)
        instruc.setContentsMargins(20,0,0,0)
        instruc.setStyleSheet("font-size:12px; color:rgb(0, 0, 0)")
        layout.addWidget(instruc)

        self.setLayout(layout)
    
    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)

app = QApplication(sys.argv)
# Create multiple pages in the same window
stacked_widget = QStackedWidget()
main_window = CSVUploader(stacked_widget)
faq_page = FAQ_Page(stacked_widget)
stacked_widget.addWidget(main_window)
stacked_widget.addWidget(faq_page)
stacked_widget.setCurrentIndex(0)
# Show window
stacked_widget.show()
sys.exit(app.exec())


