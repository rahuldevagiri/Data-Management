import pandas as pd
 
def remove_outliers(
    
    input_df
):
    df = input_df.copy()
    
 
    # Convert to numeric
    df['Sales_Price_Clean'] = pd.to_numeric(
        df['Sales_Price_Clean'],
        errors='coerce'
    )
 
    # Calculate Q1 and Q3
    Q1 = df['Sales_Price_Clean'].quantile(0.25)
    Q3 = df['Sales_Price_Clean'].quantile(0.75)
 
    # Calculate IQR
    IQR = Q3 - Q1
 
    # Define lower and upper bounds
    lower_bound = Q1 - 3.5 * IQR
    upper_bound = Q3 + 3.5 * IQR
 
    # Mark outliers as NULL
    df.loc[
        
        (df['Sales_Price_Clean'] > upper_bound),
        'Sales_Price_Clean'
    ] = None
 
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
        'Store_ID-1': prep_int()
        
 
    }, index=[0])