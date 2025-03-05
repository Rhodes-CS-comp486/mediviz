import os
import numpy as np
import pandas as pd
import random

def generate_patient_data(folder='patient_data', num_patients=100, size=25, lesion_size=4):
    if not os.path.exists(folder):
        os.makedirs(folder)

    patient_data = []  # Store patient data for a single CSV

    for i in range(num_patients):
        matrix = np.zeros((size, size))
        num_lesions = random.randint(1, 5)

        # Generate random contiguous lesions
        for _ in range(num_lesions):
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

# Example usage:
generate_patient_data()