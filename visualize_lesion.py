import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd 
import numpy as np
from PySide6.QtWidgets import QMessageBox, QInputDialog

def visualize_patient(df, gt, patient_index, parent_window=None):
    """
    Visualizes an entire patient's lesion grid as a 25x25 image.
    Parameters:
        df (pd.DataFrame): DataFrame where each row is a patient.
        patient_index (int): Index of the patient in the DataFrame.
    """
    while True:
        try:
            patient_index = int(patient_index)

            if patient_index >= len(df) or patient_index < 1:
                print(patient_index>=len(df))
                print(patient_index<1)
                raise ValueError()
            
        
            patient_data = df.iloc[patient_index, 1:].values  # Select patient, exclude first column
            patient_data = np.array(patient_data, dtype=np.float64)
            gt_data = np.array(gt, dtype=np.float64)

            # Reshape into a 25x25 grid (order = 'C' for row-wise shaping)
            lesion_matrix_c = patient_data.reshape((50, 50), order='C')

            
                
            plt.figure(figsize=(5, 5))  # Create a single plot
            plt.imshow(lesion_matrix_c, cmap='gray')
            plt.contour(gt_data, levels=[0.5],colors='red',linewidths=1.5)
            plt.title(f"Lesion Graph for Patient {patient_index}")
            plt.show()
            
        except ValueError:
            QMessageBox.critical(parent_window, "Error", "Invalid patient number. Please enter a valid number.")
            return
        
        reply = QMessageBox.question(
            parent_window, "Visualize Another?", "Would you like to visualize another patient?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.No:
            break
        
        patient_index, ok = QInputDialog.getText(
            parent_window, "Patient Number", "Enter a number for which patient to visualize:"
        )
        
        if not ok or patient_index.strip() == "":
            break


    






