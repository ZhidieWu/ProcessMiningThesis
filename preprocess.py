import pandas as pd

def createCSVFortDataObject(df,activity_cycle_column):
    activityPairDf = pd.DataFrame(columns=df.columns)
    activityPairDf.to_csv('Data/activityPairDf.csv', index=False)

    newdf = pd.read_csv('Data/activityPairDf.csv')

    last_activity = 'start'
    print(df.iloc[0][activity_cycle_column])
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




