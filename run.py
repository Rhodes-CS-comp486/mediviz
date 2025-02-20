from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#app = QApplication(sys.argv)

#window = QWidget()
#window.show()

#app.exec()

def load_lesion_data(matrix_path, label_path):
    """Loads and validates CSV lesion data"""
    print("Loading lesion data")
    df=pd.read_csv(matrix_path)
    lesion_matrix = df[['Region A', 'Region B', 'Region C', 'Region D']].values
    tf=pd.read_csv(label_path)
    labels = tf['Diagnosis'].values
    print("matrix and label data loaded")
    return lesion_matrix, labels 


def train_svm(lesion_matrix, labels):
    """Train an SVM model on lesion data."""
    print("training model")
    model = SVC(kernel='linear', random_state=42)
    model.fit(lesion_matrix, labels)
    predictions = model.predict(lesion_matrix)
    accuracy = accuracy_score(labels, predictions)
    return model, predictions

lesion_matrix, labels = load_lesion_data('data/sample_data.csv','data/sample_data_diag.csv')
model, predictions = train_svm(lesion_matrix, labels)

# Print evaluation metrics
print("\n🔍 Model Performance:")
print(classification_report(labels, predictions))

# Plot confusion matrix
conf_matrix = confusion_matrix(labels, predictions)
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()