import os
import numpy as np
import pandas as pd
import random
import visualize_lesion

def generate_patient_data(folder='patient_data', num_patients=100, size=25, lesion_size=4):
    if not os.path.exists(folder):
        os.makedirs(folder)

    patient_data = []  # Store patient data for a single CSV

    for i in range(num_patients):
        matrix = np.zeros((size, size))

        # Generate random contiguous lesions
        lesion_size_x, lesion_size_y = lesion_size, lesion_size # this is where, 4 x 4, 5 x 5, 6 x 6
        start_x, start_y = random.randint(0, size - lesion_size_x), random.randint(0, size - lesion_size_y)
        matrix[start_x:start_x + lesion_size_x, start_y:start_y + lesion_size_y] = 1

        # Flatten matrix and store with Patient ID
        flattened_matrix = matrix.flatten().tolist()
        patient_data.append([f"Patient_{i+1}"] + flattened_matrix)

    # Create DataFrame with Patient IDs
    columns = ["Patient_ID"] + [f"Region_{i}" for i in range(size * size)]
    df = pd.DataFrame(patient_data, columns=columns)
    
    # Save to a single CSV file
    df.to_csv(os.path.join(folder, "patients_data.csv"), index=False)
    print(f"Generated {num_patients} patients in 'patients_data.csv'")
    print(df)
    
    #delete after testing (there should be a gap at line 29)
    test_df = pd.read_csv("patient_data/patients_data.csv")
    visualize = input("Do you want to visualize? y/n")
    while(visualize == "y"):
        patient_to_visualize = int(input("What patient? (Enter a numer 1-1000)"))
        visualize_lesion.visualize_patient(test_df, patient_to_visualize)
        visualize = input("Do you want to visualize another patient? y/n")
    #delete after testing"


# Example usage:
generate_patient_data()