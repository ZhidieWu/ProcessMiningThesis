import pandas as pd
def encodeStringColumn(newdf):
    # remain the artifact-related column and selected column(for split data)
    newdf = newdf.loc[:, ['mainShipmentRouteNumber','speed', 'city', 'country', 'activity']]
    # change activity to unique int
    newdf['activity'], _ = pd.factorize(newdf['activity'])
    # one-hot encoding
    # text column
    text_columns = newdf.select_dtypes(include=['object']).columns.tolist()
    # Perform one-hot encoding on the categorical columns
    df_encoded = pd.get_dummies(newdf, columns=text_columns)
    print(df_encoded)
    return df_encoded