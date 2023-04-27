from sklearn.metrics import accuracy_score, classification_report
def show_classification_report(clf,x_train,y_train,x_test,y_test):
    model = clf.fit(x_train, y_train.values.ravel())
    predict_actual = clf.predict(x_test)
    accuracy_acutal = clf.score(x_test, y_test)
    classification_result = classification_report(y_test, predict_actual)
    print(predict_actual, accuracy_acutal, classification_result, sep='\n')
    return model