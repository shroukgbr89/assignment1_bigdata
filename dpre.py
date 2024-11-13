import pandas as pd
import numpy as np

def dpre(df):
    # Feature Engineering
    df['FamilySize'] = df['SibSp'] + df['Parch']
    df["Title"] = df["Name"].str.extract(r', (Mr|Miss|Mrs)\.')

    # Handle missing values for 'Age' using random sampling based on mean and std deviation
    mean_age = df['Age'].mean()
    std_age = df['Age'].std()
    missing_ages = np.random.normal(mean_age, std_age, df['Age'].isnull().sum())
    df.loc[df['Age'].isnull(), 'Age'] = np.clip(missing_ages, 0, df['Age'].max())

    # Impute 'Title' and 'Survived' columns based on distribution
    for col in ['Title', 'Survived']:
        distribution = df[col].value_counts(normalize=True)
        df[col].fillna(np.random.choice(distribution.index, p=distribution.values), inplace=True)

    # Data reduction and discretization
    df.drop(columns=['PassengerId', 'Name', 'Cabin', 'Ticket'], inplace=True)
    df['AgeGroup'] = pd.cut(df['Age'], bins=[-1, 10, 20, 30, 40, 50, 60, df['Age'].max()+1],
                            labels=['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61+'])
    df['FareGroup'] = pd.cut(df['Fare'].fillna(df['Fare'].mean()), bins=[-1, 20, 40, 60, 80, 100, df['Fare'].max()],
                             labels=['0-20', '21-40', '41-60', '61-80', '81-100', '100+'])

    # Encode categorical data
    for col in ['Sex', 'Embarked', 'Title', 'AgeGroup', 'FareGroup']:
        df[f'Int{col}'] = pd.factorize(df[col])[0]

    # Final dataset after dropping original categorical columns
    df.drop(columns=['AgeGroup', 'FareGroup', 'Title', 'Sex', 'Embarked'], inplace=True)
    df.to_csv("res_dpre.csv", index=False)
    return df
