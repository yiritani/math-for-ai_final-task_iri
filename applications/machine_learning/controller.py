from .utils import data_processing, linear_calc, show_plot
from pathlib import Path
import yaml

path = Path(__file__).parent
with open(str(path) + '/utils/config/config.yml') as yml:
    config = yaml.safe_load(yml)


def main(far_from_station, age, price, loops, alpha):
    # ベースとなる散布図と回帰直線の生成開始
    # 駅徒歩 + 築年数　と　家賃を返してもらう
    x1, yt = data_processing.generate_predict_model()

    # 正規化
    normalized_x, mean_x, std_x = data_processing.normalize(x1)

    # 行列型変数に変換
    matrix_x = data_processing.convert_matrix_variable(normalized_x)

    # 常に1の値を持つダミー列を追加
    inserted_axis_x = data_processing.insert_axis1(matrix_x)

    # 初期化処理　後続で使うため、重みベクトル「w」を返してもらう
    w = linear_calc.initialize(inserted_axis_x, yt, loops, alpha)

    # 回帰直線のスタートと終了地点を生成
    reg_start, reg_end = linear_calc.generate_regression_line(normalized_x, w)

    # 我が家の条件正規化
    my_home_normalized_x = ((far_from_station / 2.0) + age - mean_x) / std_x
    my_home_y = price

    # 散布図と回帰直線の描画
    show_plot.show_scatter_regression(normalized_x, yt, reg_start, reg_end, my_home_normalized_x, my_home_y)
