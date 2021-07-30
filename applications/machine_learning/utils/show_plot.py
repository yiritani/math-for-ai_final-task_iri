import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .config import config_getter

config = config_getter.config_initialize()


def show_scatter_regression(x, yt, xl, yl, my_home_x=None, my_home_y=None):
    # 散布図と回帰直線の描画
    plt.figure(figsize=(6, 6))
    plt.scatter(x, yt, s=10, c='b')
    plt.scatter(my_home_x, my_home_y, s=100, c='r', marker="*")
    plt.xlabel('FarFromStation + Age', fontsize=14)
    plt.ylabel('TotalPrice', fontsize=14)
    plt.plot(xl[:, 1], yl, c='k')
    plt.title('Is the price of your home reasonable?')

    # dockerではshow()を使うのが面倒くさいからpngを保存する
    plt.savefig(config_getter.get_png_file_path() + config['FILE']['PNG_FILE_NAME'])
    print('\033[31m' + 'PNG file output success!' + '\033[0m')
