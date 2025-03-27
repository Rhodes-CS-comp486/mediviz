import os
import numpy as np
import pandas as pd
import random
import visualize_lesion
import matplotlib.pyplot as plt

def generate_patient_data(folder='patient_data', num_patients=100, size=25, lesion_size=4):
    if not os.path.exists(folder):
        os.makedirs(folder)

    patient_data = []  # Store patient data for a single CSV

    for i in range(num_patients):
        matrix = np.zeros((size, size))
        num_lesions = random.randint(1, 5)

        # Generate random contiguous lesions
        #for _ in range(num_lesions):
        lesion_size_x, lesion_size_y = lesion_size, lesion_size # this is where, 4 x 4, 5 x 5, 6 x 6
        start_x, start_y = random.randint(0, size - lesion_size_x), random.randint(0, size - lesion_size_y)
        matrix[start_x:start_x + lesion_size_x, start_y:start_y + lesion_size_y] = 1

        # Flatten matrix and store with Patient ID
        flattened_matrix = matrix.flatten().tolist()
        patient_data.append([f"Patient_{i+1}"] + flattened_matrix)

    # Create DataFrame with Patient IDs
    columns = ["Patient_ID"] + [f"Region_{i}" for i in range(size * size)]
    df = pd.DataFrame(patient_data, columns=columns)
    
    #delete after testing (there should be a gap at line 29)
    test_df = pd.read_csv("patient_data/patients_data-1.csv")
    visualize = input("Do you want to visualize? y/n")
    while(visualize == "y"):
        patient_to_visualize = int(input("What patient? (Enter a numer 1-1000)"))
        visualize_lesion.visualize_patient(test_df, patient_to_visualize)
        visualize = input("Do you want to visualize another patient? y/n")
    #delete after testing"
    """
    # TESTING
    # Extract patient data (excluding 'Patient_ID')
    patient_data = df.iloc[0, 1:].values  # Select first row, exclude first column
    patient_data = np.array(patient_data, dtype=np.float64)
    # Reshape into a 25x25 grid (try both 'C' and 'F' orders)
    lesion_matrix_c = patient_data.reshape((25, 25), order='C')
    lesion_matrix_f = patient_data.reshape((25, 25), order='F')
    # Plot to visualize if lesions appear contiguous
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(lesion_matrix_c, cmap='gray')
    axes[0].set_title('C-Order Reshape')
    axes[1].imshow(lesion_matrix_f, cmap='gray')
    axes[1].set_title('F-Order Reshape')
    plt.show()
    # END TESTING
"""
    # Save to a single CSV file
    df.to_csv(os.path.join(folder, "patients_data.csv"), index=False)
    print(f"Generated {num_patients} patients in 'patients_data.csv'")
    print(df)
 

# Example usage:
generate_patient_data()