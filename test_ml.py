
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import compute_model_metrics, train_model
from ml.data import apply_label


# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # add description for the first test
    """
    assert apply_label(np.array([0])) == "<=50K"
    assert apply_label(np.array([1])) == ">50K"


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    """
    X_train = np.array([[0], [1], [2], [3]])
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)
    assert model.n_features_in_ == X_train.shape[1]


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    y = np.array([0, 0, 1, 1])

    preds = np.array([0, 0, 1, 1])

    precision, recall, f1 = compute_model_metrics(y, preds)

    assert precision == 1.0
    assert recall == 1.0
    assert f1 == 1.0
