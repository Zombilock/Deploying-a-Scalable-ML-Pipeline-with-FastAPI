import pytest
from train_model import X_train, X_test
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics



# TODO: implement the first test. Change the function name and input as needed
def data_shape_test():
    """
    # Ensures that the number of cols is correct between the training and test sets
    """
    
    pass


# TODO: implement the second test. Change the function name and input as needed
def correct_model_test():
    """
    # Ensures that the model used is RandomForest
    """
    X = np.array([[0, 0], [1, 1]])
    y = np.array([0, 1])

    model = train_model(X, y)

    assert isinstance(model, RandomForestClassifier), f'Expected model to be an instance of RandomForestClassifier, but got {type(model)}'
    pass


# TODO: implement the third test. Change the function name and input as needed
def results_test():
    """
    # Ensures that the model produces the expected results on the test set
    """
    y_true = [0, 1, 0, 1, 0]
    y_preds = [0, 1, 0, 0, 0]
    precision, recall, fbeta = compute_model_metrics(y_true, y_preds)

    assert precision is not None, 'Expected precision to be calculated, but got None'
    assert recall is not None, 'Expected recall to be calculated, but got None'
    assert fbeta is not None, 'Expected fbeta to be calculated, but got None'
    pass
