import ML_Modeling as ML_M
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# % Accuracy
print((accuracy_score(ML_M.Y_test, ML_M.predicted_Y)*100))

#classification report
print(classification_report(ML_M.Y_test, ML_M.predicted_Y))