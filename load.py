import argparse
import pandas as pd
from dpre import dpre
from model import model
from vis import vis
from eda import eda

def load_dataset(file_path):
    try:
        dataset = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return dataset
    except Exception as e:
        print(f"Error loading the dataset: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Load and process dataset.")
    parser.add_argument("file_path", help="Path to the dataset file")
    args = parser.parse_args()

    dataset = load_dataset(args.file_path)
    if dataset is not None:
        dataset = dpre(dataset)
        model(dataset)
        vis(dataset)
        eda(dataset)

if __name__ == "__main__":
    main()
