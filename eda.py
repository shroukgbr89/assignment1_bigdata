import numpy as np
import pandas as pd

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def eda(df):
    numeric_df = df.select_dtypes(include=[np.number])
    columns = numeric_df.columns
    results = np.zeros((len(columns), len(columns)))

    # Calculate cosine similarity between numeric features
    with open('eda-in-1.txt', 'w') as f:
        for i, col1 in enumerate(columns):
            for j, col2 in enumerate(columns):
                results[i, j] = cosine_similarity(numeric_df[col1], numeric_df[col2])
                f.write(f'Cosine similarity between {col1} and {col2}: {results[i, j]:.4f}\n')

            # Mean, median, and correlation analysis
            mean_val, median_val = numeric_df[col1].mean(), numeric_df[col1].median()
            f.write(f'{col1} Mean: {mean_val:.2f}, Median: {median_val:.2f}\n')

        f.write('\nCorrelation Matrix:\n' + numeric_df.corr().to_string())
        f.write(f'\nHighest Fare: {df["Fare"].max()}\nBiggest Family Size: {df["FamilySize"].max()}\n')
