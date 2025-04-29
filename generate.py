from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, QSlider, QFrame, QMessageBox, QScrollArea
from PySide6.QtCore import Qt, QSettings
import pandas as pd 
import numpy as np
import generate_data
from visualize import VisualizeWindow

class GenerateWindow(QWidget):
    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)
    
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        #self.setWindowTitle("Generate Data")
        #self.setGeometry(400, 400, 400, 400)
        self.settings = QSettings("MediViz", "Lesion")
        self.past_x_position = self.settings.value("slider_x_position", 0, type=int)
        self.past_y_position = self.settings.value("slider_y_position", 0, type=int)
        self.past_box_size = self.settings.value("box_size", 0, type=int)
        self.past_scaling_factor = self.settings.value("scaling_factor", 0, type=int)
        self.past_lesion_distribution = self.settings.value("lesion_distribution", 0, type=int)
        # Layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        back_button = QPushButton("Back to Home")
        back_button.setFixedWidth(125)
        back_button.setStyleSheet("border: 1px solid #cccccc; border-radius: 6px;")
        back_button.clicked.connect(self.go_to_home)
        main_layout.addWidget(back_button)

        label = QLabel("Select options for data generation:", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 14px; font-weight: bold; color: black; margin: 10px")
        main_layout.addWidget(label)

        # Scaling Factor Dropdown
        scaling_layout = QVBoxLayout()
        scaling_label = QLabel("Select Scaling Factor")
        self.dropdown1 = QComboBox()
        self.dropdown1.addItems(["1", "2", "3", "4", "5"])  # Scale factor options
        self.dropdown1.setCurrentText(str(self.past_scaling_factor)) 
        scaling_layout.addWidget(scaling_label)
        scaling_layout.addWidget(self.dropdown1)
        main_layout.addLayout(scaling_layout)

        # Ground Truth Size Dropdown
        gt_layout = QVBoxLayout()
        gt_label = QLabel("Select Ground Truth Size:")
        self.dropdown2 = QComboBox()
        self.dropdown2.addItems(["3", "4", "5", "6", "7", "8", "9", "10", "15"])  # Ground truth size options
        self.dropdown2.setCurrentText(str(self.past_box_size))

        self.dropdown2.currentIndexChanged.connect(self.update_box_size)  # Update box size and sliders
        gt_layout.addWidget(gt_label)
        gt_layout.addWidget(self.dropdown2)
        main_layout.addLayout(gt_layout)
        
        #Lesion Distribution Dropdown 
        lesion_layout = QVBoxLayout()
        lesion_label = QLabel("Select Lesion Position Variance:")
        self.dropdown3 = QComboBox()
        self.dropdown3.setMaxVisibleItems(20)  
        self.dropdown3.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"])  #1-20
        self.dropdown3.setCurrentText(str(self.past_lesion_distribution)) 
        lesion_layout.addWidget(lesion_label)
        lesion_layout.addWidget(self.dropdown3)
        main_layout.addLayout(lesion_layout)

        # Grid for visualization
        self.grid = QFrame()
        self.grid.setFixedSize(500, 500)
        self.grid.setStyleSheet("background-color: black; margin: 10px")
        main_layout.addWidget(self.grid, alignment=Qt.AlignCenter)

        # **Red Box (Ground Truth Indicator)**
        self.box = QLabel(self.grid)
        self.box.setFixedSize(30, 30)  # Default 3x3
        self.box.setStyleSheet("background-color: red; border: 1px solid black; opacity: 0.7;")
        self.box.move(0, 0)

        # **Sliders**
        self.label_x = QLabel(f"X Position: {self.past_x_position}")
        main_layout.addWidget(self.label_x)

        self.slider_x = QSlider(Qt.Horizontal, self)
        self.slider_x.setTickInterval(1)
        self.slider_x.setTickPosition(QSlider.TicksBelow)
        main_layout.addWidget(self.slider_x)


        self.label_y = QLabel(f"Y Position: {self.past_y_position}")
        main_layout.addWidget(self.label_y)

        self.slider_y = QSlider(Qt.Horizontal, self)
        self.slider_y.setTickInterval(1)
        self.slider_y.setTickPosition(QSlider.TicksBelow)
        self.slider_y.setValue(self.past_y_position)
        main_layout.addWidget(self.slider_y)



        # **Slider event connections**
        self.slider_x.valueChanged.connect(self.update_box_position)
        self.slider_y.valueChanged.connect(self.update_box_position)

        # Save Button
        self.save_button = QPushButton("Generate Data", self)
        self.save_button.clicked.connect(self.save_selection)
        main_layout.addWidget(self.save_button)
        
        # Visualize Button 
        self.visualize_lesion_button = QPushButton("Visualize Data", self)
        self.visualize_lesion_button.setVisible(False) #Hide button until after lesions are generated
        self.visualize_lesion_button.clicked.connect(self.visualize_data)
        main_layout.addWidget(self.visualize_lesion_button)
        
        # Text Box for Diagnoses Percentage
        self.diag_text_box = QLabel("Diagnoses Percentage", self)
        self.diag_text_box.setWordWrap(True)  # Enable word wrapping
        self.diag_text_box.setStyleSheet("border: 1px solid black; padding: 10px; background-color: #F0F0F0; color:black")
        self.diag_text_box.setVisible(False)
        main_layout.addWidget(self.diag_text_box)

        
        scroll_content = QWidget()
        scroll_content.setLayout(main_layout)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background-color: #EDEDED; border: none;")
        scroll_area.setWidget(scroll_content)
        outer_layout = QVBoxLayout()
        outer_layout.addWidget(scroll_area)
        self.setLayout(outer_layout)

        # Container
        #container = QWidget()
        #container.setLayout(layout)
        #self.setCentralWidget(container)

        # Initialize slider ranges
        self.setLayout(main_layout)
        self.update_box_size()
        self.slider_x.setValue(int(self.past_x_position))
        self.slider_y.setValue(int(self.past_y_position))
        self.update_box_position()

        #connect signals
        self.slider_x.valueChanged.connect(self.update_box_position)
        self.slider_y.valueChanged.connect(self.update_box_position)
        self.dropdown2.currentIndexChanged.connect(self.update_box_size)  # Update box size and sliders

    def closeEvent(self, event):
        """Saves the current slider positions when the window is closed."""
        self.settings.setValue("slider_x_position", self.slider_x.value())
        self.settings.setValue("slider_y_position", self.slider_y.value())
        self.settings.setValue("box_size", self.dropdown2.currentText())
        self.settings.setValue("scaling_factor", self.dropdown1.currentText())
        self.settings.setValue("lesion_distribution", self.dropdown3.currentText())
        super().closeEvent(event)

    def update_box_size(self):
        """Updates the red box size and slider range based on ground truth selection."""
        size = (int(self.dropdown2.currentText()) * 10)  # Convert to pixels
        self.box.setFixedSize(size, size)

        # Adjust slider range to keep ground truth inside the grid
        max_slider_value = (500 - size) // 10  # Ensure box stays within 250x250 grid
        self.slider_x.setRange(0, max_slider_value)
        self.slider_y.setRange(0, max_slider_value)
        
        self.update_box_position()

    def update_box_position(self):
        """Updates the red box position based on slider values."""
        x_pos = self.slider_x.value() * 10
        y_pos = self.slider_y.value() * 10
        self.label_x.setText(f"X Position: {self.slider_x.value()}")
        self.label_y.setText(f"Y Position: {self.slider_y.value()}")
        self.box.move(x_pos, y_pos)
        # Save current positions
        self.past_x_position = self.slider_x.value()
        self.past_y_position = self.slider_y.value()

    def save_selection(self):
        """Saves the ground truth selection and generates patient data."""
        x_grid = self.slider_x.value()
        y_grid = self.slider_y.value()
        ground_truth_size = int(self.dropdown2.currentText())  # User-selected size
        scale_factor = float(self.dropdown1.currentText())  # User-selected scale factor

        # Generate 50x50 matrix
        grid_data = [[0 for _ in range(50)] for _ in range(50)]

        # Apply selected ground truth size at chosen location
        for i in range(ground_truth_size):
            for j in range(ground_truth_size):
                if 0 <= y_grid + i < 50 and 0 <= x_grid + j < 50:
                    grid_data[y_grid + i][x_grid + j] = 1

        # Save ground truth as CSV
        pd.DataFrame(grid_data).to_csv("ground_truth.csv", index=False, header=False)
        print(f"Saved ground truth of size {ground_truth_size} at ({x_grid}, {y_grid})")
      

        # Generate patient data using the scale factor
        generate_data.generate_patient_data(scale_factor=scale_factor)
        self.make_diagnoses()
        
        QMessageBox.information(self, "Success", "Data generation complete!  You can find them in the 'patient_data' folder, in the same path as this application.")

        self.save_button.setText("Generate more data? (This will overwrite previously generated data)")
        
        #Show percentage to user
        self.visualize_lesion_button.setVisible(True)
      
        """Get Percentage of Patients with a positive diagnosis"""
        # Load the CSV
        df = pd.read_csv("diagnoses.csv") 
        
        # Count occurrences of 1
        num_ones = (df["Diagnosis"] == 1).sum()  # Count rows where Diagnosis == 1
        total_rows = len(df)
        positive_percentage = np.round((num_ones / total_rows) * 100,2)
        self.diag_text_box.setText(f"Percentage of Patients with a positive diagnosis: {positive_percentage}")
        #Show percentage to user
        self.visualize_lesion_button.setVisible(True)
        #Show Visualize Lesion Button now that data is generated
        self.diag_text_box.setVisible(True)
        
        
    def check_overlap(patient_data, ground_truth, overlap_threshold=0.5):
        patient_data = np.array(patient_data).astype(float)
        ground_truth = np.array(ground_truth).astype(float)
        #Define the ground truth mask (the 4x4 square of 1s)
        ground_truth_mask = ground_truth == 1

        #Find the overlapping region (patient's 1s that intersect with the the ground truth 1s)
        overlap = np.sum((patient_data == 1) & ground_truth_mask)
        print("overlap:  ", overlap)
        #Total number of 1s in the ground truth region (this is 4x4 = 16)
        #total_ground_truth_ones = np.sum(ground_truth_mask)
        patient_mask = patient_data == 1
        patient_ones = np.sum (patient_mask)
        #print("total_ground_truth_ones:  ", total_ground_truth_ones)
        #Check if the overlap is greater than or equal to the threshold (50%)
        overlap_percentage = overlap / patient_ones
        print(f"Overlap percentage: {overlap_percentage}")
        print(f"Overlap threshold: {overlap_threshold}")

        if overlap_percentage >= overlap_threshold:
            return 1
        else:
            return  0
            
            
    
    def make_diagnoses(self):
        df = pd.read_csv('patient_data/patients_data.csv', header=None)
        df_ground_truth = pd.read_csv('ground_truth.csv', header=None)
        #print(df_ground_truth)
        diagnosis = []
        for i in range(1, df.shape[0]):
            #row_data = df.iloc[i].values[1:] test diff order for debugging note: are we accidentally excluding some patients by doing [1:] should it be [0:]
            row_data = df.iloc[i, 1:].values
            test = pd.DataFrame(row_data.reshape(50,50))
            print(f"Patient data shape: {test.shape}")
            print(test)
            #print(f"Ground truth shape: {df_ground_truth.shape}")
            temp_diagnosis = GenerateWindow.check_overlap(test, df_ground_truth, overlap_threshold=0.5)
            if temp_diagnosis == 1:
                diagnosis.append(1)
                print("patient number")
                print(i)
                print(test)
            else:
                diagnosis.append(0)
            #print(test)
            #print(temp_diagnosis)
           # Create a DataFrame for the diagnoses
        diagnoses_df = pd.DataFrame({'Diagnosis': diagnosis})

        # Save the diagnoses to a CSV file
        output_filename = 'diagnoses.csv'
        diagnoses_df.to_csv(output_filename, index=False)

        print(f"Diagnoses saved to {output_filename}")
    
    def visualize_data(self): 
        """Opens the data generation window."""
        self.visualize_window = VisualizeWindow()  # Create instance of the GenerateWindow class
        self.visualize_window.show()
        


        
        
                

        

        
