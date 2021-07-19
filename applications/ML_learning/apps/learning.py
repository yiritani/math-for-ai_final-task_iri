import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from IPython.display import set_matplotlib_formats
import pathlib


# np.set_printoptions(suppress=True, precision=3)


def getCsvData():
    df = pd.read_csv('../templates/house_price.csv')

    return df


def generatePredictModel():
    with open('../templates/house_price.csv', 'r') as fd:
        feature_names = np.array(fd.read().split('\n')[0].split(','))

    csv_data = np.loadtxt('../templates/house_price.csv', delimiter=',', skiprows=1)
    learning_data = csv_data[:, np.logical_or(feature_names == 'FarFromStation', feature_names == 'Age')]

    true_data = csv_data[:, feature_names == 'TotalPrice']

    return learning_data, true_data


if __name__ == 'learning':
    # csv_data = getCsvData()
    # print(csv_data)

    x1, yt = generatePredictModel()
    print(x1)
    # print(yt)
    y = np.insert(yt, 0, 1.0, axis=1)
    print(y)

    plt.scatter(x1, y, s=10, c='b')
    plt.xlabel('terms', fontsize=14)
    plt.ylabel('Price', fontsize=14)
    plt.show()
