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
def createOutputCSV(df,df_2):
    activityEndDf = pd.DataFrame(columns=df_2.columns)
    activityEndDf.to_csv('Data/activityEndDf.csv', index=False)

    newdf = pd.read_csv('Data/activityEndDf.csv')
    newdf['activity'] = ''
    for index, row in df.iterrows():
        for index2, row2 in df_2.iterrows():
            if df['lifecycle'][index] == 'End' and int(df['EGSMtimestamp'][index]) == int(row2['timestamp']):
                startActivity = df['activity'][index]
                new_row = df_2.iloc[index2]
                new_row['activity'] = startActivity
                newdf = newdf.append(new_row, ignore_index=True)
                #newdf = pd.concat(objs=[newdf, new_row])
    newdf = newdf.sort_values('activity', ascending=True)
    newdf.to_csv('Data/activityEndDf.csv', index=False)

def createInputObjectCSV(df):
    activityStartDf = pd.DataFrame(columns=df.columns)
    activityStartDf.to_csv('Data/activityStartDf.csv', index=False)

    newdf = pd.read_csv('Data/activityStartDf.csv')
    print(df['activity'].unique())
    last_activity = ''
    for activty_name in df['activity'].unique():
        for index, row in df.iterrows():
            if activty_name == row['activity'] and row['activity']!=last_activity:
                new_row = df.iloc[index]
                newdf = newdf.append(new_row, ignore_index=True)
            last_activity = row['activity']
    newdf = newdf.sort_values('activity', ascending=True)
    newdf.to_csv('Data/activityStartDf.csv', index=False)

def createOutputObjectCSV(df):
    activityEndDf = pd.DataFrame(columns=df.columns)
    activityEndDf.to_csv('Data/activityEndDf.csv', index=False)

    newdf = pd.read_csv('Data/activityEndDf.csv')
    last_activity = df['activity'][0]
    flag = 1
    for activty_name in df['activity'].unique():
        for index, row in df.iterrows():
            if activty_name == row['activity'] and row['activity'] != last_activity and flag !=len(df['activity'].unique()):
                new_row = df.iloc[index]
                new_row['activity'] = activty_name
                newdf = newdf.append(new_row, ignore_index=True)
            elif activty_name == row['activity'] and row['activity'] != last_activity and flag ==len(df['activity'].unique()):
                new_row = df.iloc[index - 1]
                new_row['activity'] = activty_name
                newdf = newdf.append(new_row, ignore_index=True)
            last_activity = row['activity']
        flag = flag + 1
    newdf = newdf.sort_values('activity', ascending=True)
    newdf.to_csv('Data/activityEndDf.csv', index=False)

def createCSVFortDataObject(df,activity_cycle_column):
    activityPairDf = pd.DataFrame(columns=df.columns)
    activityPairDf.to_csv('Data/activityPairDf.csv', index=False)

    newdf = pd.read_csv('Data/activityPairDf.csv')

    last_activity = 'start'
    current_cycle_column = df[activity_cycle_column][0]

    new_csv_index = 0
    for index, row in df.iterrows():
        if current_cycle_column == row[activity_cycle_column]:
            if last_activity != row['activity']:
                new_row = df.iloc[index]
                new_row['activity'] = str(last_activity + ',' + row['activity'])
                newdf = newdf.append(new_row, ignore_index=True)
                #newdf['activity'][index] = str(last_activity)+","+str(row['activity'])
                new_csv_index = new_csv_index + 1
        else:
            #final activity
            new_row = df.iloc[index-1]
            new_row['activity'] = str(last_activity + ',' + 'end')
            newdf = newdf.append(new_row, ignore_index=True)
            # newdf['activity'][index] = str(last_activity)+","+str(row['activity'])
            new_csv_index = new_csv_index + 1
            #new start
            last_activity = 'start'
            new_row = df.iloc[index]
            new_row['activity'] =  str(last_activity + ',' + row['activity'])
            newdf = newdf.append(new_row, ignore_index=True)
            #newdf['activity'][index] = str(last_activity) + "," + str(row['activity'])
            new_csv_index = new_csv_index + 1
        last_activity = row['activity']
        current_cycle_column = row[activity_cycle_column]
    newdf = newdf.sort_values('activity', ascending=True)
    newdf.to_csv('Data/activityPairDf.csv', index=False)




