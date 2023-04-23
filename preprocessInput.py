import pandas as pd
def createInputCSV(df,df_2):
    activityStartDf = pd.DataFrame(columns=df_2.columns)
    activityStartDf.to_csv('Data/activityStartDf.csv', index=False)

    newdf = pd.read_csv('Data/activityStartDf.csv')
    newdf['activity'] = ''
    for index, row in df.iterrows():
        for index2, row2 in df_2.iterrows():
            if df['lifecycle'][index] == 'Started' and int(df['EGSMtimestamp'][index]) == int(row2['timestamp']):
                startActivity = df['activity'][index]
                new_row = df_2.iloc[index2]
                new_row['activity'] = startActivity
                newdf = newdf.append(new_row, ignore_index=True)
                #newdf = pd.concat(objs=[newdf, new_row])
    newdf = newdf.sort_values('activity', ascending=True)
    newdf.to_csv('Data/activityStartDf.csv', index=False)


