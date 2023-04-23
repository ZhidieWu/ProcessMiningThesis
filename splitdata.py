#split_data(X,y,test_size=0.3,select_column='mainShipmentRouteNumber')
import random
import pandas as pd
from sklearn.model_selection import train_test_split
def split_data(X,y,test_size,select_column):
    #
    if select_column != "":
        x_columns = X.columns.tolist().remove(select_column)
        new_x_train = pd.DataFrame(columns=x_columns)
        new_x_test = pd.DataFrame(columns=x_columns)
        new_y_train = pd.DataFrame(columns=y.columns.tolist())
        new_y_test = pd.DataFrame(columns=y.columns.tolist())
        select_column_type = tuple(X[select_column].unique())
        select_column_type_count = len(select_column_type)
        select_column_type_train_count = select_column_type_count * (1-test_size)
        train_x_select_column_random_sample = random.sample(select_column_type, k=int(select_column_type_train_count))
        print(select_column_type)
        print(train_x_select_column_random_sample)
        for train_x_select_column in train_x_select_column_random_sample:
            for index, row in X.iterrows():
                new_x_row = X.iloc[index].drop(select_column)
                new_y_row = y.iloc[index]
                if row[select_column] == train_x_select_column:
                    new_x_train = new_x_train.append(new_x_row)
                    new_y_train = new_y_train.append(new_y_row)
                else:
                    new_x_test = new_x_test.append(new_x_row)
                    new_y_test = new_y_test.append(new_y_row)
        new_y_train=new_y_train.astype('int')
        new_y_test=new_y_test.astype('int')
    else:
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size, random_state=42)
        new_x_train, new_x_test, new_y_train, new_y_test = x_train, x_test, y_train, y_test
    return new_x_train,new_x_test,new_y_train,new_y_test