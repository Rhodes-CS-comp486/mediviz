import pandas as pd 
import numpy as np

def load_lesion_data(file_path):
    """Loads and validates CSV lesion data"""
    try:
        df=pd.read_csv(file_path)
        lesion_matrix = df.to_numpy()
        return lesion_matrix
    except Exception as e:
        print(f"Error loading data: {e}")
        return None 



