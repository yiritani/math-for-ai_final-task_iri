from utils import data_processing, calc, show_plot
from pathlib import Path
import yaml

path = Path(__file__).parent
with open(str(path) + '/utils/config/config.yml') as yml:
    config = yaml.load(yml)


if __name__ == '__main__':
    # ベースとなる散布図と回帰直線の生成開始
    # 駅徒歩 + 築年数　と　家賃を返してもらう
    x1, yt = data_processing.generatePredictModel()

    # 正規化
    normalized_x, mean_x, std_x = data_processing.normalize(x1)

    # 行列型変数に変換
    matrix_x = data_processing.convertMatrixVariable(normalized_x)

    # 常に1の値を持つダミー列を追加
    inserted_axis_x = data_processing.insertAxis1(matrix_x)

    # 初期化処理　後続で使うため、重みベクトル「w」を返してもらう
    w = calc.initialize(inserted_axis_x, yt)

    # 回帰直線のスタートと終了地点を生成
    reg_start, reg_end = calc.generateRegressionLine(normalized_x, w)

    # 我が家の条件正規化
    my_home_normalized_x = (config['MY_HOME_TERM']['FAR_FROM_STATION'] + config['MY_HOME_TERM']['AGE'] - mean_x) / std_x
    my_home_y = config['MY_HOME_TERM']['PRICE']

    # 散布図と回帰直線の描画
    show_plot.showScatterRegression(normalized_x, yt, reg_start, reg_end, my_home_normalized_x, my_home_y)
