import pandas as pd
import numpy as np
 
def fill_store_name(input_df):
 
    df = input_df.copy()
 
    df['Store_Name'] = df['Store_Name'].replace(
        ['Nan', 'nan', 'NULL', 'null', ''],
        np.nan
    )
 
    store_mapping = (
        df.dropna(subset=['Store_Name'])
          .groupby('Store_ID')['Store_Name']
          .first()
    )
 
    df['Store_Name'] = df['Store_Name'].fillna(
        df['Store_ID'].map(store_mapping)
    )
 
    if df['Store_Name'].isnull().sum() > 0:
 
        mode_value = df['Store_Name'].mode()[0]
 
        df['Store_Name'] = df['Store_Name'].fillna(
            mode_value
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
       # 'Sale_Status': prep_string()
 
    })