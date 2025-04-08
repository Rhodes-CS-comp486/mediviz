def load_patient_data():
    """Opens a file dialog for folder selection and loads patient lesion data from Excel files."""
    import os
    import pandas as pd
    from PySide6.QtWidgets import QFileDialog

    folder_path = QFileDialog.getExistingDirectory(None, "Select Patient Data Folder")
    
    if not folder_path:
        return None, None, "No folder selected."

    # Find all Excel files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith(('.xlsx', '.xls'))]
    
    if len(files) < 2:
        return None, None, "Error: At least two patient files are required."

    lesion_matrices = []
    patient_files = []

    for file in files:
        file_path = os.path.join(folder_path, file)
        try:
            df = pd.read_excel(file_path, header=None)
            matrix = df.to_numpy()
            lesion_matrices.append(matrix.flatten())
            patient_files.append(file)
        except Exception as e:
            return None, None, f"Failed to read {file}: {e}"

    # Check for diagnosis file
    diagnosis_file = os.path.join(folder_path, "diagnoses.csv")
    if not os.path.exists(diagnosis_file):
        return None, None, "Error: diagnoses.csv file is missing."

    diagnoses_df = pd.read_csv(diagnosis_file)
    if "Diagnosis" not in diagnoses_df.columns:
        return None, None, "Error: diagnoses.csv does not contain a 'Diagnosis' column."

    labels = diagnoses_df["Diagnosis"].to_numpy()

    return lesion_matrices, labels, None

