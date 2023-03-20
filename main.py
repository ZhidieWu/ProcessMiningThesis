import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
# decision tree
from decisiontree import *
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
#select feature
#selectKBest
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

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

## LabelEncoder
# text column
text_columns = df_2.select_dtypes(include=['object']).columns.tolist()
le = LabelEncoder()
df_encoded = df_2
for col in text_columns:
    df_encoded[col] = le.fit_transform(df_encoded[col])
df_encoded.to_csv('Data/encoded_data.csv', index=False)
print(df_encoded)

# ## Decision Tree

#all_features
all_features = df_encoded.columns.tolist()
all_features.remove('activity')
all_features.remove('time')
all_features.remove('timestamp')

# initial value
# Define the features and target variable
X = df_encoded[all_features]
y = df_encoded['activity']
pre_accuracy_score = decision_tree(X, y)
current_accuracy_score = pre_accuracy_score
num_feature = len(all_features)
data_objects = []
new_features = all_features
while (pre_accuracy_score <= current_accuracy_score) and (current_accuracy_score >= 0.8):
    data_objects = new_features
    num_feature = num_feature - 1
    # select feature
    selector = SelectKBest(score_func=f_classif, k=num_feature)  # 选择 F 统计量作为评分函数
    selector.fit(X, y)
    # print selected feature
    mask = selector.get_support()  # 获取掩码
    new_features = X.columns[mask]  # 获取选择的特征名称
    print(new_features)

    X = df_encoded[new_features]
    # decision tree
    current_accuracy_score = decision_tree(X, y)

print('data_objects:',data_objects)


