from typing import Tuple, Optional, Any

import numpy as np
from numpy import ndarray

from .config import config_getter


def generate_predict_model():
    with open(config_getter.get_price_file_path(), 'r') as fd:
        feature_names = np.array(fd.read().split('\n')[0].split(','))

    csv_data = np.loadtxt(config_getter.get_price_file_path(), delimiter=',', skiprows=1)

    learning_data = csv_data[:, np.logical_or(feature_names == 'FarFromStation', feature_names == 'Age')]
    learning_data = np.array([i[0] / 2 + i[1] for i in learning_data])  # とりあえず駅徒歩と築年数は足してみた。多分改善の余地あり

    true_data = csv_data[:, feature_names == 'TotalPrice']
    true_data = np.array([i[0] for i in true_data])
    aaa = [i for i in learning_data]
    aaa.sort()
    print(aaa)
    return learning_data, true_data


def normalize(target_param):
    target_param_mean = np.mean(target_param)
    target_param_std = np.std(target_param)

    return (target_param - target_param_mean) / target_param_std, target_param_mean, target_param_std


def convert_matrix_variable(target_param) -> ndarray:
    return np.reshape(target_param, (-1,1))


def insert_axis1(target_param) -> ndarray:
    return np.insert(target_param, 0, 1.0, axis=1)
