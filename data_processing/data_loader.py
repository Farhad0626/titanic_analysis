import pandas as pd


def load_data(path: str = "data/titanic.csv") -> pd.DataFrame:

    try:
        titanic = pd.read_csv(path)
        print(f"Data loaded from \"{path}\".")
        return titanic
    except FileNotFoundError as e:
        print(f"Error: File not found at '{path}'.")
        raise e
    except pd.errors.EmptyDataError as e:
        print(f"Error: The CSV file at '{path}' is empty.")
        raise e
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse the CSV file at '{path}'. Check delimiter or format.")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred while loading {path}: {e}")
        raise e

