import pandas as pd
import classfications
#decision tree
from sklearn.tree import DecisionTreeClassifier
from classficationrules import new_decision_tree_rules
#Random forest
from sklearn.ensemble import RandomForestClassifier
#knn
from sklearn.neighbors import KNeighborsClassifier
#Logistic Regression Classfier
from sklearn.linear_model import LogisticRegression
# Gradient Boosting Decision Tree
from sklearn.ensemble import GradientBoostingClassifier
#Naive Bayes
from sklearn.naive_bayes import  MultinomialNB
# ## Preprocess
from preprocess import createInputCSV
from preprocess import createOutputCSV
from preprocess import createInputObjectCSV
from preprocess import createOutputObjectCSV
from preprocess import createCSVFortDataObject
from encoder import encodeStringColumn
from splitdata import split_data
#json
import json
from processJson import processjson
from processJson import merge_state_from_json
############### Artifact ################
artifact_dict = {'Truck':['speed','country','city'],'Container':[]}
selected_artifact = 'Truck'
instanceId = 'mainShipmentRouteNumber'
############### Preprocess ##############

print("#########################Preprocess#########################")
#df = pd.read_csv('Data/results_LHR_AMS.csv', sep=";", parse_dates=True)
'''
# ## LHR_AMS
df_2 = pd.read_csv('Data/newnewnew2.csv', sep=";", parse_dates=True)

# ## add column name
df_2.columns = ["mainShipmentRouteNumber", "speed", "time", "truckNumber", "timestamp", "shipmentEndCity",
                "shipmentStartCity", "city", "country","activity"]
## new csv : lifecycle = started
#createInputObjectCSV(df_2)
## new csv : lifecycle = end
#createOutputObjectCSV(df_2)
createCSVFortDataObject(df_2,"mainShipmentRouteNumber")'''
print("##############################################################")
## LabelEncoder
print("#########################Label Encoder#########################")
newdf = pd.read_csv('Data/activityPairDf.csv')
artifact_dict[selected_artifact].append(instanceId)
artifact_dict[selected_artifact].append('activity')
newdf = newdf.sort_values('activity', ascending=True)
newdf = newdf[artifact_dict[selected_artifact]]
newdf.to_csv('Data/activityPairDf.csv', index=False)
df_encoded_input = encodeStringColumn(newdf)
df_encoded_input.to_csv('Data/pair_encoded_input.csv', index=False)

#newdf = pd.read_csv('Data/activityEndDf.csv')
#df_encoded_output = encodeStringColumn(newdf)
#df_encoded_output.to_csv('Data/df_encoded_output.csv', index=False)


text_columns = []
for column in newdf.columns:
    if newdf[column].dtype == 'object':
        text_columns.append(column)


df_encoded_input = pd.read_csv('Data/pair_encoded_input.csv')
#df_encoded_output = pd.read_csv('Data/df_encoded_output.csv')

print("##############################################################")
############### Decision Tree #################
##input
all_features = df_encoded_input.columns.tolist()
all_features.remove('activity')
X = df_encoded_input[all_features]
y = df_encoded_input[['activity']]
print("##########################split data##########################")
x_train,x_test,y_train,y_test = split_data(X,y,test_size=0.3,select_column=instanceId)
print("########################Classification########################")
print("1.1 Decision Tree -- Input DataObject")
clf = DecisionTreeClassifier(random_state=1234)
model = classfications.show_classification_report(clf,x_train,y_train,x_test,y_test)
all_features.remove(instanceId)
print(newdf['activity'].unique())
rules,input_dict = new_decision_tree_rules(model,all_features ,newdf['activity'].unique(),'input',text_columns,selected_artifact)
print(input_dict)
for r in rules:
    print(r)

##output
'''
print("1.2 Decision Tree -- Output DataObject")
all_features = df_encoded_output.columns.tolist()
all_features.remove('activity')
X = df_encoded_output[all_features]
y = df_encoded_output[['activity']]
x_train,x_test,y_train,y_test = split_data(X,y,test_size=0.3,select_column='mainShipmentRouteNumber')
clf = DecisionTreeClassifier(random_state=1234)
model = classfications.show_classification_report(clf,x_train,y_train,x_test,y_test)
all_features.remove('mainShipmentRouteNumber')
rules,output_dict = decision_tree_rules(model,all_features , newdf['activity'].unique(),'output',text_columns)
print(output_dict)
for r in rules:
    print(r)

print("2. Random Forest")
clf = RandomForestClassifier(n_estimators=2)
model = classfications.show_classification_report(clf,x_train,y_train,x_test,y_test)
print("3. KNN algorithm")
clf = KNeighborsClassifier()
classfications.show_classification_report(clf,x_train,y_train,x_test,y_test)
print("4. Gradient Boosting Decision Tree")
clf = GradientBoostingClassifier(n_estimators = 200)
model=classfications.show_classification_report(clf,x_train,y_train,x_test,y_test)
print("5. Multinomial Naive Bayes Classifier")
clf = MultinomialNB(alpha=0.01)
classfications.show_classification_report(clf,x_train,y_train,x_test,y_test)
print("##############################################################")
'''

# json file
print("############################json############################")
with open("Data/input_dataobject.json","w") as f:
    json.dump(input_dict,f,indent=4,ensure_ascii=False)

result_dict = merge_state_from_json(input_dict,text_columns)

#with open("Data/input_dataobject.json","r") as input_json:
#    input_dict = json.load(input_json)
'''
#for output
#with open("Data/output_dataobject.json","r") as output_json:
#    output_dict = json.load(output_json)
with open("Data/output_dataobject.json","w") as f:
    json.dump(output_dict,f,indent=4,ensure_ascii=False)
result_dict = processjson(input_dict,output_dict)
'''
#result_dict
print(result_dict)
with open("Data/final_dataobject.json","w") as f:
    json.dump(result_dict,f,indent=4,ensure_ascii=False)
print("##############################################################")

