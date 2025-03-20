import pandas as pd
import numpy as np

df = pd.read_csv('patient_data/patients_data.csv', header=None)

for i in range(1, df.shape[0]):
    row_data = df.iloc[2].values[1:]

    test = pd.DataFrame(row_data.reshape(25,25))
    print(test)
    