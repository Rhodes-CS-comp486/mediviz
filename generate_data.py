import os
import numpy as np
import pandas as pd
import random

def generate_patient_data(folder='patient_data', num_patients=1000, size=25, scale_factor=1):
    if not os.path.exists(folder):
        os.makedirs(folder)

    patient_data = []  # Store patient data for a single CSV

    for i in range(num_patients):
        matrix = np.zeros((size, size))

        # Scale lesion size dynamically
        base_lesion_size = 4
        growth_factor = random.randint(1, 3)
        lesion_size = min(base_lesion_size + int(scale_factor * growth_factor), size)

        # Place lesion at center
        center_x = size // 2
        center_y = size // 2
        start_x = max(0, center_x - lesion_size // 2)
        start_y = max(0, center_y - lesion_size // 2)

        matrix[start_x:start_x + lesion_size, start_y:start_y + lesion_size] = 1

        # Flatten matrix and store with Patient ID
        flattened_matrix = matrix.flatten().tolist()
        patient_data.append([f"Patient_{i+1}"] + flattened_matrix)

    # Create DataFrame with Patient IDs
    columns = ["Patient_ID"] + [f"Region_{i}" for i in range(size * size)]
    df = pd.DataFrame(patient_data, columns=columns)

    # Save to a single CSV file
    df.to_csv(os.path.join(folder, "patients_data.csv"), index=False)
    print(f"Generated {num_patients} patients in 'patients_data.csv'")
