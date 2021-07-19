import numpy as np
from numpy import ndarray

from applications.config import config_getter

config = config_getter.config_initialize()


def pred(x, w):
    return x @ w


def generateRegressionLine(normalize, w):
    xl = np.array([[1, normalize.min()], [1, normalize.max()]])
    yl = pred(xl, w)

    return xl, yl


def initialize(x: ndarray, yt: ndarray, is_logging=False) -> ndarray:
    M = x.shape[0]
    D = x.shape[1]

    iters = config['DATA_PROCESS']['ITERS']
    alpha = config['DATA_PROCESS']['ALPHA']

    w = np.ones(D)
    history = np.zeros((0, 2))

    yp, yd = 0, 0


    for k in range(iters):
        # 予測値の計算 (7.8.1)
        yp = pred(x, w)

        # 誤差の計算 (7.8.2)
        yd = yp - yt

        # 勾配降下法の実装 (7.8.4)
        w = w - alpha * (x.T @ yd) / M

        # 学習曲線描画用データの計算、保存
        if k % 100 == 0:
            # 損失関数値の計算 (7.6.1)
            loss = np.mean(yd ** 2) / 2
            # 計算結果の記録
            history = np.vstack((history, np.array([k, loss])))
            # 画面表示
            if is_logging:
                print("iter = %d  loss = %f" % (k, loss), w)

    if is_logging:
        print('予測値:', yp[:10])
        print('実測値', yt[:10])
        print('誤差', yd[:10])

    return w
