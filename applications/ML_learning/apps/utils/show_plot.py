import matplotlib.pyplot as plt


def showPlot(x_params, y_params):
    plt.scatter(x_params, y_params, s=10, c='b')
    plt.xlabel('terms', fontsize=14)
    plt.ylabel('Price', fontsize=14)
    plt.show()


def showScatterRegression(x, yt, xl, yl):
    print(xl)
    # 散布図と回帰直線の描画
    plt.figure(figsize=(6, 6))
    plt.scatter(x, yt, s=10, c='b')
    plt.xlabel('density', fontsize=14)
    plt.ylabel('alchol', fontsize=14)
    plt.plot(xl[:, 1], yl, c='k')
    plt.show()