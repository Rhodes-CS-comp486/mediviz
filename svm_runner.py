import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import csv
import os
import pickle

class SVMRunner:
    def __init__(self, patient_matrices, diagnoses):
        self.patient_matrices = np.array(patient_matrices) #THIS SHOULD BE CHANGED..... each row could be moved into a dataframe later?   idk what structure it will enter as
        self.diagnoses = np.array(diagnoses)
        self.model = SVC(kernel='linear')
        self.report = None
        with open(patient_matrices, 'r') as file:
            csv_reader = csv.reader(file)
            patients = list(csv_reader)
            patients = np.array(patients)
            self.patient_matrices = patients[1:, 1:]

        with open(diagnoses, 'r') as file:
            csv_reader = csv.reader(file)
            diagnoses = list(csv_reader)
            diagnoses = np.array(diagnoses)
            self.diagnoses  = diagnoses[1:].ravel() #just turns it into the correct structure for the model to run


    def train_and_evaluate(self):
        """Trains an SVM model and prints the classification report."""
        if len(set(self.diagnoses)) < 2:
            return "Error: At least one sample from each class (0 and 1) is required."
        self.model.fit(self.patient_matrices, self.diagnoses)
        predictions = self.model.predict(self.patient_matrices)
        self.report = classification_report(self.diagnoses, predictions)
        return self.report
    
    def test(self, test_data):
        """Tests the SVM model on new data and returns the predictions."""
        return self.model.predict(self.patient_matrices)
    
    def load_trained_model(filename='svm_model.pkl'):
        """Loads the SVM model from a file."""
        if not os.path.exists(filename):
            return "no pickle file"
        with open(filename, 'rb') as file:
            model = pickle.load(file)
            return model
    def filename_creation(self):    
        
        """Creates a filename for the SVM model based on the current date and time."""
        from datetime import datetime
        now = datetime.now()
        return f"svm_model_{now.strftime('%Y%m%d_%H%M%S')}.pkl"
    def save_model(self):
        filename = self.filename_creation()
        """Saves the SVM model to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self.model, file)
        
    def load_model(self, filename):
        """Loads the SVM model from a file."""
        if not os.path.exists(filename):
            return False
        with open(filename, 'rb') as file:
            self.model = pickle.load(file)
        return self.model
    


# #EVERYTHING BELOW THIS IS JUST TESTING YOU CAN DELETE IT LATER <3
# def load(filename):
#     """Loads the SVM model from a file."""
#     if not os.path.exists(filename):
#         return False
#        # return "Error: No saved model found. Train the model first."
#     with open(filename, 'rb') as file:
#         model = pickle.load(file)


# def train_and_evaluate(patient_matrices, diagnoses):
        
#         model = SVC(kernel='linear')
#         """Trains an SVM model and prints the classification report."""
#         # if len(set(diagnoses)) < 2:
#         #     return "Error: At least one sample from each class (0 and 1) is required."
#         model.fit(patient_matrices, diagnoses)
#         predictions = model.predict(patient_matrices)

#         with open('svm_model.pkl', 'wb') as file:
#             pickle.dump(model, file)
#         return classification_report(diagnoses, predictions)

# def test(self, test_data):
#     """Tests the SVM model on new data and returns the predictions."""
#     return self.model.predict(self.patient_matrices)


with open('patient_data/patients_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    patients = list(csv_reader)
    patients = np.array(patients)
    patients = patients[1:, 1:]

with open('diagnoses.csv', 'r') as file:
    csv_reader = csv.reader(file)
    diagnoses = list(csv_reader)
    diagnoses = np.array(diagnoses)
    diagnoses  = diagnoses[1:].ravel() #just turns it into the correct structure for the model to run


# # print(f"Shape of patients: {patients.shape}")
# # print(f"Shape of diagnoses: {diagnoses.shape}")
# # print(patients)
# print(train_and_evaluate(patients, diagnoses))
