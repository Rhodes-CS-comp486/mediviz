from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QTextEdit, QHBoxLayout, QStackedWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import pandas as pd
import sys
import os
from generate import GenerateWindow
from algorithm import ChooseUploader

###########################
### DISPLAY MAIN WINDOW ###
###########################
class CSVUploader(QMainWindow):
    def __init__(self, stacked_widget):  
        super().__init__()
        self.setWindowTitle("Patient Data Loader")
        self.setGeometry(500, 500, 600, 400)
        self.stacked_widget = stacked_widget

        # Layout and widgets
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        
        # MediViz Logo
        pixmap = QPixmap("MediViz_Logo.png")
        logo_label = QLabel()
        logo_label.setPixmap(pixmap)
        logo_label.setFixedSize(372,161)
        logo_label.setScaledContents(True)
        layout.addWidget(logo_label, alignment=Qt.AlignCenter)

        # "Instructions and FAQs" button -- links to new page in the same window
        faq_button = QPushButton("Instructions and FAQs", self)
        faq_button.setStyleSheet("""QPushButton{background-color: rgb(162, 191, 215); 
                                        font-family: 'Trebuchet MS';
                                        font-size: 16px; 
                                        font-weight: bold; 
                                        color: white; 
                                        padding: 10px; 
                                        border: 1px solid #e0e0e0}
                                        QPushButton:hover{background-color: #F5F8F9
                                        }""")
        faq_button.clicked.connect(self.faq_page)
        layout.addWidget(faq_button)
        
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        button_layout.setAlignment(Qt.AlignCenter)

        # "Upload Data and Run Algorithm" button -- opens new window
        upload_button = QPushButton("Upload Data and Run Algorithm", self)
        upload_button.setFixedWidth(350)
        upload_button.setStyleSheet("""QPushButton{background-color:rgb(118, 149, 177); 
                                    font-family: 'Trebuchet MS';
                                    font-size: 16px; 
                                    font-weight: bold; 
                                    color: white; 
                                    padding: 10px; 
                                    border: 1px solid #e0e0e0
                                    } 
                                    QPushButton:hover{background-color: #F5F8F9
                                    }""")
        upload_button.clicked.connect(self.run_algorithm) # (used to be self.upload_folder)
        button_layout.addWidget(upload_button)
        
        # "Generate Data" button -- opens new window
        generate_button = QPushButton("Generate Data", self)
        generate_button.setFixedWidth(350)
        generate_button.setStyleSheet("""QPushButton{background-color: rgb(118, 149, 177); 
                                        font-family: 'Trebuchet MS';
                                        font-size: 16px; 
                                        font-weight: bold; 
                                        color: white; 
                                        padding: 10px; 
                                        border: 1px solid #e0e0e0}
                                        QPushButton:hover{background-color: #F5F8F9
                                        }""")
        generate_button.clicked.connect(self.generate_data)
        button_layout.addWidget(generate_button)

        layout.addLayout(button_layout)

        # Container 
        container = QWidget()
        container.setLayout(layout)
        container.setStyleSheet("background-color: rgb(255,255,255);")
        self.setCentralWidget(container)
    
    def faq_page(self):
        self.stacked_widget.setCurrentIndex(1)

    # Upload Data and Run Algorithm
    def run_algorithm(self):
        """Opens the algorithm window."""
        #self.algorithm_window = ChooseUploader()
        #self.algorithm_window.show()
        self.stacked_widget.setCurrentIndex(2)
    
    # Generate Data: opens new window allowing user to select desired parameters for data generation            
    def generate_data(self):
        """Opens the data generation window."""
        #self.generate_window = GenerateWindow()  # Create instance of the GenerateWindow class
        #self.generate_window.show()
        self.stacked_widget.setCurrentIndex(3)
        
    
        

###########################
###      FAQ PAGE       ###
###########################
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

class UploadData_Page(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)

class GenerateData_Page(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)

app = QApplication(sys.argv)
# Create multiple pages in the same window
stacked_widget = QStackedWidget()

# Main Page
main_window = CSVUploader(stacked_widget)
stacked_widget.addWidget(main_window) # index 0

# FAQ Page
faq_page = FAQ_Page(stacked_widget)
stacked_widget.addWidget(faq_page)  # index 1

# Upload Data Page
upload_page = ChooseUploader(stacked_widget)
stacked_widget.addWidget(upload_page)  # index 2

# Generate Data Page
generate_page = GenerateWindow(stacked_widget)
stacked_widget.addWidget(generate_page)  # index 3

# Show window
stacked_widget.show()
sys.exit(app.exec())


