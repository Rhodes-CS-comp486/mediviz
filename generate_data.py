import os
import numpy as np
import pandas as pd
import random


def generate_patient_data(folder='patient_data', num_patients=1000, size=50, scale_factor=1, spread_range=5):
    if not os.path.exists(folder):
        os.makedirs(folder)

    patient_data = []  # Store patient data for a single CSV


    for i in range(num_patients):
        matrix = np.zeros((size, size))

        # Scale lesion size dynamically
        #base_lesion_size = 4
        base_lesion_size = 2 
        growth_factor = random.randint(1, 3)
        normalized_scale_factor = int(np.clip(np.random.normal(scale_factor, 0.5, size=(1,1)), 1, 5))
        #lesion_size = min(base_lesion_size + int(scale_factor * growth_factor), size)
        lesion_size = min(base_lesion_size + int(normalized_scale_factor * growth_factor), size)

        # Place lesion at center
        center_x = int(np.clip(np.random.normal(size//2, spread_range, size=(1,1)), 0, size -1)) 
        center_y = int(np.clip(np.random.normal(size//2, spread_range, size=(1,1)), 0, size-1))
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
    print(df)

