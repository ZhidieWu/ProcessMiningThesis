import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
#decision tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# ## results_LHR_AMS
from decisiontree import get_rules
from addactivitycolumn import addActivity
from preprocessInput import createInputCSV
from encoder import encodeStringColumn
from splitdata import split_data
############### Preprocess ##############
print("#########################Preprocess#########################")
df = pd.read_csv('Data/results_LHR_AMS.csv', sep=";", parse_dates=True)

# ## LHR_AMS
df_2 = pd.read_csv('Data/LHR_AMS.csv', sep=";", parse_dates=True)

# ## add column name
df_2.columns = ["mainShipmentRouteNumber", "speed", "time", "truckNumber", "timestamp", "shipmentEndCity",
                "shipmentStartCity", "city", "country"]
## new csv : lifecycle = started
createInputCSV(df,df_2)
## new csv : lifecycle = end

### add column activity
#addActivity(df, df_2)
print("##############################################################")
## LabelEncoder
print("#########################Label Encoder#########################")
newdf = pd.read_csv('Data/activityStartDf.csv')
df_encoded_input= encodeStringColumn(newdf)
df_encoded_input.to_csv('Data/df_encoded_input.csv', index=False)
df_encoded_input = pd.read_csv('Data/df_encoded_input.csv')
print("##############################################################")
############### Decision Tree #################
all_features = df_encoded_input.columns.tolist()
all_features.remove('activity')
X = df_encoded_input[all_features]
y = df_encoded_input[['activity']]
print("##########################split data##########################")
x_train,x_test,y_train,y_test = split_data(X,y,test_size=0.3,select_column='mainShipmentRouteNumber')
print(x_train)
print(y_train)
print(x_test)
print(y_test)
print("##############################################################")
print("########################Classification########################")
clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(x_train, y_train)
#decision_function = clf.decision_function(x_test)
predict_actual = clf.predict(x_test)
accuracy_acutal=clf.score(x_test,y_test)
classification_result = classification_report(y_test,predict_actual)
print(predict_actual,accuracy_acutal,classification_result,sep='\n')
rules = get_rules(clf,all_features , ['Connection','Drive','Load','Pause'])
for r in rules:
    print(r)
print("##############################################################")