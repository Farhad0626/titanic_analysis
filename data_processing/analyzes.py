import pandas as pd



def survival_rate(dataframe: pd.DataFrame) -> float:
    return dataframe["Survived"].mean()


def missing_count(dataframe: pd.DataFrame, column: str) -> int:
    result = dataframe[column].isnull().sum()
    return result


def missing_percentage(dataframe: pd.DataFrame, column: str) -> float:
    result = dataframe[column].isnull().sum() / len(dataframe) * 100
    return result


def calculate_q1(dataframe: pd.DataFrame, column: str) -> float:
    return dataframe[column].describe()["25%"]


def calculate_q3(dataframe: pd.DataFrame, column: str) -> float:
    return dataframe[column].describe()["75%"]


def calculate_iqr(dataframe: pd.DataFrame, column: str) -> float:
    result = calculate_q3(dataframe, column) - calculate_q1(dataframe, column)
    return result

def lower_bound(dataframe: pd.DataFrame, column: str) -> float:
    q1 = calculate_q1(dataframe, column)
    iqr = calculate_iqr(dataframe, column)

    return q1 - 1.5 * iqr


def upper_bound(dataframe: pd.DataFrame, column: str) -> float:
    q3 = calculate_q3(dataframe, column)
    iqr = calculate_iqr(dataframe, column)

    return q3 + 1.5 * iqr


def outlier_count(dataframe: pd.DataFrame, column: str) -> int:
    lower = lower_bound(dataframe, column)
    upper = upper_bound(dataframe, column)

    outlier_count = 0

    for value in dataframe[column]:
        if value < lower or value > upper:
            outlier_count += 1

    return outlier_count


def value_percentage(dataframe: pd.DataFrame, column: str):
    result = dataframe[column].value_counts(normalize=True) * 100
    return result