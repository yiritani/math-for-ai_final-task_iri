import numpy as np


def normalize(target_param):
    target_param_mean = np.mean(target_param)
    target_param_std = np.std(target_param)

    return (target_param - target_param_mean) / target_param_std


def convertMatrixVariable(target_param):
    return np.reshape(target_param, (-1,1))


def insertAxis1(target_param):
    return np.insert(target_param, 0, 1.0, axis=1)
