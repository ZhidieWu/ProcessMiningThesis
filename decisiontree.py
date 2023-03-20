from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
def decision_tree(X,y):

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
    return accuracy