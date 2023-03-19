import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
# decision tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ## results_LHR_AMS
df = pd.read_csv('Data/results_LHR_AMS.csv', sep=";", parse_dates=True)

# ## LHR_AMS
df_2 = pd.read_csv('Data/LHR_AMS.csv', sep=";", parse_dates=True)

# ## add column name
df_2.columns = ["mainShipmentRouteNumber", "speed", "time", "truckNumber", "timestamp", "shipmentEndCity",
                "shipmentStartCity", "city", "country"]

# ## add column "activity"
df_2['activity'] = ''

###
start_time = 0
end_time = 0
process = 2
case_id = 0
from_activity = 'start'
current_row = 0
for index, row in df.iterrows():
    process = process - 1
    # start_time
    if process == 1:
        start_time = df['EGSMtimestamp'][index]
    # end_time
    if process == 0:
        end_time = df['EGSMtimestamp'][index]
        if case_id != df['mainShipmentRouteNumber'][index]:
            # 判断是否为表格中的第一行数据
            if case_id != 0:
                from_activity = 'start'
            case_id = df['mainShipmentRouteNumber'][index]
        for index2, row2 in df_2.iterrows():
            if case_id == row2['mainShipmentRouteNumber']:
                if (int(row2['timestamp']) == int(start_time) and from_activity == 'start') or (
                        int(row2['timestamp']) > int(start_time) and int(row2['timestamp']) <= int(end_time)):
                    df_2['activity'][index2] = str([from_activity, row['activity']])
        from_activity = row['activity']
        process = 2

# ## Delete the row which activity is null
row_indexs = df_2[df_2['activity'] == ''].index
df_2.drop(row_indexs, inplace=True)

print(df_2)
# ## Decision Tree

# Define the features and target variable
X = df_2[['truckNumber', 'speed']]
y = df_2['activity']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier on the training data
clf.fit(X_train, y_train)

# Use the trained classifier to make predictions on the testing data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)



