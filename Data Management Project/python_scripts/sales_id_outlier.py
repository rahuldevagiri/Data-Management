import pandas as pd
import numpy as np

def clean_salesid(input_df):

    df = input_df.copy()

    # Convert Sale_ID to numeric
    df['Sale_ID'] = pd.to_numeric(
        df['Sale_ID'],
        errors='coerce'
    )

    # Calculate median using positive values only
    median_value = df.loc[
        df['Sale_ID'] > 0,
        'Sale_ID'
    ].median()

    # Replace null and negative values
    df['Sale_ID'] = np.where(
        (df['Sale_ID'].isnull()) |
        (df['Sale_ID'] < 0),
        median_value,
        df['Sale_ID']
    )

    # Create status column
    df['Sale_Status'] = np.where(
        df['Sale_ID'] == median_value,
        'Corrected',
        'Valid'
    )

    return df


def get_output_schema():

    return pd.DataFrame({

        'Sale_ID': prep_decimal(),
        'Date': prep_date(),
        'Store_ID': prep_int(),
        'Store_Name': prep_string(),
        'Store_City': prep_string(),
        'Store_Location': prep_string(),
        'Store_Open_Date': prep_date(),
        'Product_ID': prep_int(),
        'Product_Name': prep_string(),
        'Product_Category': prep_string(),
        'Units': prep_int(),
        'Revenue': prep_decimal(),
        'Manufacture_Cost': prep_decimal(),
        'Sales_Price_Clean': prep_decimal(),
        'Year': prep_int(),
        'Profit Category': prep_string(),
        'Profit Margin': prep_decimal(),
        'Quarter_No': prep_int(),
        'Table Names': prep_string(),
        'Product_ID-1': prep_int(),
        'Store_ID-1': prep_int(),
        #'Sale_Status': prep_string()

    }, index=[0])