# aic_utils.py

import pandas as pd

def get_dataset_id(alias, QA):
    # MAP WRITES TO QA OR PROD TABLES
    df = pyspark_utils.get_pandas_from_aic_table('Silver', 
'LKP_QA_TABLE_MAPPING')
    row = df[df['alias'] == alias]
    
    # Choose the appropriate column based on QA flag
    if QA:
        target_col = 'qa_dataset'
    else:
        target_col = 'prod_dataset'
    
    # Return the dataset ID
    if not row.empty:
        return row.iloc[0][target_col]
    else:
        raise ValueError("Alias not found in mapping table")

