import Encoding_Data as ED
from sklearn.model_selection import train_test_split
from sklearn import linear_model


X_train, X_test, Y_train, Y_test = train_test_split(ED.X, ED.Y, test_size=0.3,random_state=101)

reg = linear_model.LogisticRegression()
reg.fit(X_train,Y_train)

predicted_Y = reg.predict(X_test)