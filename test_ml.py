import pytest
from sklearn.ensemble import RandomForestClassifier
import ml.model as model
from ml.model import train_model
import os

# TODO: implement the first test. Change the function name and input as needed
def data_shape_test():
    """
    # Ensures that the number of rows is correct after processing the data
    """
    assert data.shape[0] == '15', f'Expected 15 rows, but got {data.shape[0]}'
    pass


# TODO: implement the second test. Change the function name and input as needed
def correct_model_test():
    """
    # Ensures that the model used is RandomForest
    """
    assert isinstance(model, RandomForestClassifier), f'Expected model to be an instance of RandomForestClassifier, but got {type(model)}'
    pass


# TODO: implement the third test. Change the function name and input as needed
def results_test():
    """
    # Ensures that the model produces the expected results on the test set
    """
    assert precision is not None, 'Expected precision to be calculated, but got None'
    assert recall is not None, 'Expected recall to be calculated, but got None'
    assert fbeta is not None, 'Expected fbeta to be calculated, but got None'
    pass
