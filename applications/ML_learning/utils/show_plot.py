import matplotlib.pyplot as plt
from .config import config_getter

config = config_getter.config_initialize()


def showScatterRegression(x, yt, xl, yl):
    # 散布図と回帰直線の描画
    plt.figure(figsize=(6, 6))
    plt.scatter(x, yt, s=10, c='b')
    plt.xlabel('FarFromStation + Age', fontsize=14)
    plt.ylabel('TotalPrice', fontsize=14)
    plt.plot(xl[:, 1], yl, c='k')

    # dockerではshow()を使うのが面倒くさいからpngを保存する
    plt.savefig(config_getter.get_png_file_path() + config['FILE']['PNG_FILE_NAME'])

    plt.show()
