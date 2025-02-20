import os
import numpy as np
import pandas as pd
import random
from sklearn.svm import SVC
from sklearn.metrics import classification_report

def generate_patient_data(folder='patient_data', num_patients=100, size=25):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i in range(num_patients):
        matrix = np.zeros((size, size))
        num_lesions = random.randint(1, 5)
        for _ in range(num_lesions):
            lesion_size_x, lesion_size_y = random.randint(1, 5), random.randint(1, 5)
            start_x, start_y = random.randint(0, size-lesion_size_x), random.randint(0, size-lesion_size_y)
            matrix[start_x:start_x+lesion_size_x, start_y:start_y+lesion_size_y] = 1
        df = pd.DataFrame(matrix)
        df.to_excel(os.path.join(folder, f"patient_{i+1}.xlsx"), index=False)

def assign_diagnoses(folder='patient_data', size=25, diagnosis_file='diagnoses.csv'):
    labels = []
    lesion_matrices = []
    patient_files = []
    
    for file in os.listdir(folder):
        if file.endswith('.xlsx'):
            df = pd.read_excel(os.path.join(folder, file), header=None)
            matrix = df.to_numpy()
            lesion_matrices.append(matrix.flatten())
            diagnosis = 1 if np.sum(matrix[10:15, 10:15]) > 6 else 0
            labels.append(diagnosis)
            patient_files.append(file)

    # Ensure at least one patient has each diagnosis
    if 0 not in labels:
        labels[random.randint(0, len(labels)-1)] = 0
    if 1 not in labels:
        labels[random.randint(0, len(labels)-1)] = 1

    # Save diagnoses to a CSV file
    diagnosis_df = pd.DataFrame({'Patient File': patient_files, 'Diagnosis': labels})
    diagnosis_df.to_csv(os.path.join(folder, diagnosis_file), index=False)

    return np.array(lesion_matrices), np.array(labels)

def train_svm_model(lesion_matrix, labels):
    model = SVC(kernel='linear')
    model.fit(lesion_matrix, labels)
    predictions = model.predict(lesion_matrix)
    print(classification_report(labels, predictions))

def main():
    generate_patient_data()
    lesion_matrix, labels = assign_diagnoses()
    #train_svm_model(lesion_matrix, labels)

if __name__ == "__main__":
    main()
