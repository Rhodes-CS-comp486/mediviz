import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import csv
import pandas as pd

def visualize_patient(df, patient_index):
    """
    Visualizes an entire patient's lesion grid as a 25x25 image.
    Parameters:
        df (pd.DataFrame): DataFrame where each row is a patient.
        patient_index (int): Index of the patient in the DataFrame.
    """
    if patient_index >= len(df):
        raise ValueError("Invalid patient index")
    # Remove Patient_ID column and convert to float
    patient_data = df[df["Patient_ID"] == "Patient_1"].iloc[:, 1:].to_numpy().reshape(25, 25)
    patient_data = df.iloc[patient_index, 1:].astype(float).values
    
    # Ensure the shape is correct
    if len(patient_data) != 625:
        raise ValueError(f"Incorrect number of columns; expected 625, got {len(patient_data)}")
    
    # Reshape into a 25x25 grid
    patient_grid = np.array(patient_data, dtype=float).flatten().reshape((25, 25))
    
    # Invert colors so lesions (1) appear black and background (0) appears white
    patient_grid = 1 - patient_grid
    
    # Display the grid
    plt.imshow(patient_grid, cmap="gray", vmin=0, vmax=1)
    plt.axis("off")
    plt.show()







