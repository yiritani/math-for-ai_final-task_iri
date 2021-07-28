from .utils import data_processing, calc, show_plot
from pathlib import Path
import yaml

path = Path(__file__).parent
with open(str(path) + '/utils/config/config.yml') as yml:
    config = yaml.safe_load(yml)


# if __name__ == '__main__':
def main():
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
    w = calc.initialize(inserted_axis_x, yt)

    # 回帰直線のスタートと終了地点を生成
    reg_start, reg_end = calc.generate_regression_line(normalized_x, w)

    # home_station = float(input('How many minutes is your house from the station? '))
    # home_age = float(input('How old is your house?' ))
    # home_price = float(input('How price is your house? '))

    # 我が家の条件正規化
    my_home_normalized_x = ((config['MY_HOME_TERM']['FAR_FROM_STATION'] / 2.0) + config['MY_HOME_TERM']['AGE'] - mean_x) / std_x
    my_home_y = config['MY_HOME_TERM']['PRICE']

    # 散布図と回帰直線の描画
    show_plot.show_scatter_regression(normalized_x, yt, reg_start, reg_end, my_home_normalized_x, my_home_y)
