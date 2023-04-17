import pandas as pd
def addActivity(df,df_2):
    new_df = pd.read_csv('Data/LHR_AMS.csv')
    new_df.to_csv('Data/preprocessresult.csv', index=False)
    preprocessResult = pd.read_csv('Data/LHR_AMS.csv', sep=";", parse_dates=True)
    preprocessResult.columns = ["mainShipmentRouteNumber", "speed", "time", "truckNumber", "timestamp",
                                "shipmentEndCity", "shipmentStartCity", "city", "country"]
    preprocessResult['activity'] = ''
    ###
    start_time = 0
    end_time = 0
    process = 2
    case_id = 0
    from_activity = 'start'
    current_row = 0
    insert_row_num = 0
    Isinsert = False
    for index, row in df.iterrows():
        process = process - 1
        # start_time
        if process == 1:
            start_time = df['EGSMtimestamp'][index]
        # end_time
        if process == 0:
            end_time = df['EGSMtimestamp'][index]
            if case_id != df['mainShipmentRouteNumber'][index]:
                case_id = df['mainShipmentRouteNumber'][index]
            for index2, row2 in df_2.iterrows():
                if case_id == row2['mainShipmentRouteNumber']:
                    if (int(row2['timestamp']) >= int(start_time) and int(row2['timestamp']) <= int(end_time)):
                        if (preprocessResult['activity'][index2 + insert_row_num] == ''):
                            preprocessResult['activity'][index2 + insert_row_num] = str(row['activity'])
                        else:
                            new_row = preprocessResult.iloc[index2 + insert_row_num].copy()
                            preprocessResult = preprocessResult.iloc[:index2 + insert_row_num].append(new_row).append(
                                preprocessResult.iloc[index2 + insert_row_num:]).reset_index(drop=True)
                            insert_row_num = insert_row_num + 1
                            preprocessResult['activity'][index2 + insert_row_num] = str(row['activity'])

            process = 2

    # ## Delete the row which activity is null
    rowIndexs = preprocessResult[preprocessResult['activity'] == ''].index
    preprocessResult.drop(rowIndexs, inplace=True)
    preprocessResult.to_csv('Data/preprocessresult.csv', index=False)
