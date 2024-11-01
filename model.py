import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def load_model():
    # Load and train the model
    X_train, y_train = load_training_data()
    model = SVC()
    model.fit(X_train, y_train)
    return model

def load_training_data():
    # Load training data from a file or database
    X_train = np.load('X_train.npy')
    y_train = np.load('y_train.npy')
    return X_train, y_train
