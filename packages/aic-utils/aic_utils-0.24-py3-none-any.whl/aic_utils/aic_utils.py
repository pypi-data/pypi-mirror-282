import pandas as pd
from google.cloud import bigquery

def get_dataset_ids(project, dataset, table, aliases, QA):
    # Initialize BigQuery client
    client = bigquery.Client(project=project)

    # Query to read the table
    query = f"SELECT * FROM `{project}.{dataset}.{table}`"
    
    # Load the table into a DataFrame
    df = client.query(query).to_dataframe()

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
