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


def generatePredictModel(df):
    x1 = df['FarFromStation'].values
    print(x1[:10])

    y = df['Price'].values
    print(y[:10])

    return x1, y


if __name__ == 'learning':
    csv_data = getCsvData()
    # print(csv_data)

    x_axis, y_axis = generatePredictModel(csv_data)

    plt.scatter(x_axis, y_axis, s=10, c='b')
    plt.xlabel('Far from station', fontsize=14)
    plt.ylabel('Price(included management price)', fontsize=14)
    plt.show()
