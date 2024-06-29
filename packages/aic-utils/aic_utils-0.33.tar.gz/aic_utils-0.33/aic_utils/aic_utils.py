import pandas as pd
from google.cloud import bigquery

def get_dataset_ids(aliases, QA, dataset=None, table=None):
    # Initialize BigQuery client
    client = bigquery.Client(project='aic-production-core')
    dataset = '3349c7ea_09a2_461d_87f5_312a5401c51a'
    table = 'LKP_QA_TABLE_MAPPING'
    
    # Query to read the table
    query = f"SELECT * FROM `{dataset}.{table}`"
    
    # Load the table into a DataFrame
    df = client.query(query).to_dataframe()

    # Determine the target column based on the QA flag
    target_col = 'qa_dataset' if QA else 'prod_dataset'

    single_alias = False
    if isinstance(aliases, str):
        aliases = [aliases]
        single_alias = True

    # List to store the results
    results = []

    for alias in aliases:
        row = df[df['alias'] == alias]
        if not row.empty:
            results.append(row.iloc[0][target_col])
        else:
            results.append(None)  # or raise ValueError(f"Alias '{alias}' not found in mapping table")

    # Return a single result or a list based on the input
    return results[0] if single_alias else results

