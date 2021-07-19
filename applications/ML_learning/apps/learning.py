import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from IPython.display import set_matplotlib_formats
import pathlib


# np.set_printoptions(suppress=True, precision=3)


def getCsvData():
    df = pd.read_csv('../templates/house_price.csv')
    # print(df.head())

    return df


def generatePredictModel():
    with open('../templates/house_price.csv', 'r') as fd:
        feature_names = np.array(fd.read().split('\n')[0].split(','))

    learning_data = np.loadtxt('../templates/house_price.csv', delimiter=',', skiprows=1)
    # print(learning_data[:, np.logical_or(feature_names == 'FarFromStation', feature_names == 'Age')])

    true_data = np.loadtxt('../templates/house_price.csv', delimiter=',', skiprows=1, usecols=4)
    # print(true_data)

    return learning_data, true_data


if __name__ == 'learning':
    # csv_data = getCsvData()
    # print(csv_data)

    x1, yt = generatePredictModel()
    print(x1)
    print(yt)
    # plt.scatter(x_axis, y_axis, s=10, c='b')
    # plt.xlabel('Far from station', fontsize=14)
    # plt.ylabel('Price(included management price)', fontsize=14)
    # plt.show()
