import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import classification_report

class SVMRunner:
    def __init__(self, lesion_matrices, labels):
        self.lesion_matrices = np.array(lesion_matrices)
        self.labels = np.array(labels)
        self.model = SVC(kernel='linear')

    def train_and_evaluate(self):
        """Trains an SVM model and prints the classification report."""
        if len(set(self.labels)) < 2:
            return "Error: At least one sample from each class (0 and 1) is required."

        self.model.fit(self.lesion_matrices, self.labels)
        predictions = self.model.predict(self.lesion_matrices)
        return classification_report(self.labels, predictions)

