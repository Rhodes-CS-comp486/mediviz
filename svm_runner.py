import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import csv

class SVMRunner:
    def __init__(self, patient_matrices, diagnoses):
        self.patient_matrices = np.array(patient_matrices) #THIS SHOULD BE CHANGED..... each row could be moved into a dataframe later?   idk what structure it will enter as
        self.diagnoses = np.array(diagnoses)
        self.model = SVC(kernel='linear')

    def train_and_evaluate(self):
        """Trains an SVM model and prints the classification report."""
        if len(set(self.diagnoses)) < 2:
            return "Error: At least one sample from each class (0 and 1) is required."
        self.model.fit(self.patient_matrices, self.diagnoses)
        predictions = self.model.predict(self.patient_matrices)
        return classification_report(self.diagnoses, predictions)
    def test(self, test_data):
        """Tests the SVM model on new data and returns the predictions."""
        return self.model.predict(self.patient_matrices)
    


#EVERYTHING BELOW THIS IS JUST TESTING YOU CAN DELETE IT LATER <3333

def train_and_evaluate(patient_matrices, diagnoses):
        model = SVC(kernel='linear')
        """Trains an SVM model and prints the classification report."""
        # if len(set(diagnoses)) < 2:
        #     return "Error: At least one sample from each class (0 and 1) is required."
        model.fit(patient_matrices, diagnoses)
        predictions = model.predict(patient_matrices)
        return classification_report(diagnoses, predictions)
def test(self, test_data):
    """Tests the SVM model on new data and returns the predictions."""
    return self.model.predict(self.patient_matrices)


with open('patient_data/patients_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    patients = list(csv_reader)
    patients = np.array(patients)
    patients = patients[1:, 1:]

with open('diagnoses.csv', 'r') as file:
    csv_reader = csv.reader(file)
    diagnoses = list(csv_reader)
    diagnoses = np.array(diagnoses)
    diagnoses  = diagnoses[1:].ravel()


# print(f"Shape of patients: {patients.shape}")
# print(f"Shape of diagnoses: {diagnoses.shape}")
# print(patients)
print(train_and_evaluate(patients, diagnoses))
