from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QTextEdit, QHBoxLayout, QStackedWidget, QScrollArea
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
        self.setStyleSheet("background-color: white;")
        self.stacked_widget = stacked_widget

        # Layout and widgets
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        
        # MediViz Logo
        pixmap = QPixmap("MV_Final_Logo2.png")
        logo_label = QLabel()
        logo_label.setPixmap(pixmap)
        logo_label.setFixedSize(500,300)
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
                                        QPushButton:hover{background-color: #ececec
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
                                    QPushButton:hover{background-color: #ececec
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
                                        QPushButton:hover{background-color: #ececec
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
        self.setStyleSheet("background-color: #D3D3D3;")
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background-color: white; border: none;")

        inner_widget = QWidget()
        inner_widget.setStyleSheet("background-color: white;")
        inner_layout = QVBoxLayout(inner_widget)

        top_row_layout = QHBoxLayout()
        top_row_layout.setAlignment(Qt.AlignTop)

        back_button = QPushButton("Back to Home")
        back_button.setFixedWidth(125)
        back_button.setStyleSheet("border: 1px solid #cccccc; border-radius: 6px;")
        back_button.clicked.connect(self.go_to_home)
        top_row_layout.addWidget(back_button, alignment=Qt.AlignLeft)

        inner_layout.addLayout(top_row_layout)

        # MediViz Logo
        pixmap = QPixmap("MV_Final_Logo2.png")
        logo_label = QLabel()
        logo_label.setPixmap(pixmap)
        logo_label.setFixedSize(500,300)
        logo_label.setScaledContents(True)
        inner_layout.addWidget(logo_label, alignment=Qt.AlignCenter)

        header_label2 = QLabel("MediViz Instructions and Frequently Asked Questions")
        header_label2.setAlignment(Qt.AlignHCenter)
        header_label2.setStyleSheet("font-size:15px; font-weight:bold; color: rgb(43, 85, 122);")
        inner_layout.addWidget(header_label2)

        #second_row_layout.setAlignment(Qt.AlignHCenter)
        #second_row_layout.addLayout(header_layout)
        #layout.addLayout(second_row_layout)

        faq_text = """
        <br></br>
        <h4>USER GUIDE: Running the Algorithm</h4>
        <ul>
            <li>Select patient data and diagnoses CSV files.
            (If you do not have patient data, select the "Generate Data" button. See below for instructions.)</li>
            <li>Once files have been selected, a green check mark should appear at each upload point, and a confirmation message should appear.</li>
            <li>Next, click the "Train Algorithm" button.</li>
            <li>Once the algorithm has been trained, the algorithm is ready to be tested! Select "Test Algorithm".</li>
            <li>Visualize the results in the form of the output chart, confusion matrix, and/or heat map.</li>
        </ul>
        <br></br>
        <h4>USER GUIDE: Generating Data</h4>
        <ul>
            <li>Adjust the preferences for the patient data generation.</li>
            <li>Select "Generate Data".</li>
            <li>The data will automatically save to the user's file system.
            NOTE: If you are generating more than one set of patient data, rename each generated file to ensure that it is not overwritten.</li>
        </ul>
        <br></br>
        <h4>FAQs:</h4>
        <ul>
            <li>What are the different parameters for data generation?</li>
            <ul>
                <li><b>Scaling Factor:</b> how spread out or close together the generated data points are around a given center which, in this case, is the ground truth. </li>
                <li><b>Ground Truth Size:</b> the size of ground truth. The ground truth is benchmark for data predictions. It is the area that classifies a patient for a positive diagnosis if breached by a certain amount. In otherwords, if more than 50% of a lesion falls within ground truth, it is considered a positive diagnosis. </li>
                <li><b>Lesion Position Variance:</b> how random the generated lesions are around a central mean. </li>
                <li><b>X and Y Position:</b> the X and Y coordinates of the ground truth. </li>
            </ul>
            <br></br>
            <li>How do I interpret the SVM output chart?</li>
        </ul>
        """
        add_text = QLabel(faq_text)
        add_text.setWordWrap(True)
        add_text.setStyleSheet("color: black;")
        add_text.setAlignment(Qt.AlignTop)
        inner_layout.addWidget(add_text)
        
        scroll_area.setWidget(inner_widget)
        
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        
        self.setLayout(main_layout)
    
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


