import pandas as pd
import classfications
#decision tree
from sklearn.tree import DecisionTreeClassifier
from classficationrules import decision_tree_rules
#Random forest
from sklearn.ensemble import RandomForestClassifier
from classficationrules import random_forest_rules
#knn
from sklearn.neighbors import KNeighborsClassifier
#Logistic Regression Classfier
from sklearn.linear_model import LogisticRegression
# Gradient Boosting Decision Tree
from sklearn.ensemble import GradientBoostingClassifier
#Naive Bayes
from sklearn.naive_bayes import  MultinomialNB

# ## Preprocess
from preprocessInput import createInputCSV
from encoder import encodeStringColumn
from splitdata import split_data
############### Preprocess ##############
"""
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
"""
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
print("########################Classification########################")
print("1. Decision Tree")
clf = DecisionTreeClassifier(random_state=1234)
model = classfications.show_classification_report(clf,x_train,y_train,x_test,y_test)
all_features.remove('mainShipmentRouteNumber')
rules = decision_tree_rules(model,all_features , ['Connection','Drive','Load','Pause'])
for r in rules:
    print(r)
print("2. Random Forest")
clf = RandomForestClassifier(n_estimators=2)
model = classfications.show_classification_report(clf,x_train,y_train,x_test,y_test)
random_forest_rules(model)
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