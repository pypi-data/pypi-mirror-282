import pandas as pd
import pyspark_utils
def get_dataset_ids(dataset, table, aliases, QA):
    """
    Fetch dataset IDs for given aliases from a mapping table.
    
    Parameters:
    - dataset (str): The dataset name.
    - table (str): The table name.
    - aliases (str or list): A single alias or a list of aliases.
    - QA (bool): Flag to determine whether to fetch QA or production dataset IDs.
    
    Returns:
    - list: A list of dataset IDs corresponding to the provided aliases.
    """
    
    # Load the mapping DataFrame
    df = pyspark_utils.get_pandas_from_aic_table(dataset, table)
    
    # Determine the target column based on the QA flag
    target_col = 'qa_dataset' if QA else 'prod_dataset'

    # Handle both single alias (string) and multiple aliases (list)
    if isinstance(aliases, str):
        aliases = [aliases]

    # List to store the results
    results = []

    for alias in aliases:
        row = df[df['alias'] == alias]
        if not row.empty:
            results.append(row.iloc[0][target_col])
        else:
            results.append(None)  # or raise ValueError(f"Alias '{alias}' not found in mapping table")

    return results
