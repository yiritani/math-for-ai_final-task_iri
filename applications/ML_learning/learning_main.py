import numpy as np

from utils import data_processing, calc, show_plot
from utils.config import config_getter

config = config_getter.config_initialize()
np.set_printoptions(suppress=True, precision=3)


def generatePredictModel():
    with open(config_getter.get_price_file_path(), 'r') as fd:
        feature_names = np.array(fd.read().split('\n')[0].split(','))

    csv_data = np.loadtxt(config_getter.get_price_file_path(), delimiter=',', skiprows=1)

    learning_data = csv_data[:, np.logical_or(feature_names == 'FarFromStation', feature_names == 'Age')]
    learning_data = np.array([i[0] + i[1] for i in learning_data])  # 係数っぽくするためにとりあえず駅徒歩と築年数は足してみた。多分改善の余地あり

    true_data = csv_data[:, feature_names == 'TotalPrice']
    true_data = np.array([i[0] for i in true_data])

    return learning_data, true_data


if __name__ == 'learning_main':
    # 駅徒歩 + 築年数　と　家賃を返してもらう
    x1, yt = generatePredictModel()

    # 正規化
    normalized_x = data_processing.normalize(x1)

    # 行列型変数に変換
    matrix_x = data_processing.convertMatrixVariable(normalized_x)

    # 常に1の値を持つダミー列を追加
    inserted_axis_x = data_processing.insertAxis1(matrix_x)

    # 初期化処理　後続で使うため、重みベクトル「w」を返してもらう
    w = calc.initialize(inserted_axis_x, yt)

    # 回帰直線のスタートと終了地点を生成
    reg_start, reg_end = calc.generateRegressionLine(normalized_x, w)

    # 散布図と回帰直線の描画
    show_plot.showScatterRegression(normalized_x, yt, reg_start, reg_end)
