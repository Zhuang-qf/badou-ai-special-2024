"""
标准化：
由于我们训练模型的时候，输入的数据返回可能比较大，同样样本中个数据可能量纲不一致，这样的数据容易对模型训练的构建结果产生影响。
去除数据的单位限制，转换为无量纲的纯数值，以便不同单位或量级的指标能够进行比较和加权。
"""
import numpy as np
from matplotlib import pyplot as plt


def text1(x):
    """
    0-1归一化，减最小值
    :return:
    """

    res = [(float(i) - min(x)) / float(max(x) - min(x)) for i in x]
    return res


def text2(x):
    """
    -1-1归一化，减均值
    :param x:
    :return:
    """
    res = [(float(i) - np.mean(x)) / (max(x) - min(x)) for i in x]
    return res


def text3(x):
    """
    零均值归一化（z-sore标准化）
    经过处理后的数据均值为0，标准差为1（正态分布）
    y = (x-μ)/σ
    :param x:
    :return:
    """
    mean = np.mean(x)
    sigma = sum([(i - np.mean(x)) * (i - np.mean(x)) for i in x]) / len(x)
    res = [(x - mean) / sigma for i in x]
    return res


if __name__ == '__main__':
    l = [-10, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11,
         11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 30]
    a = text1(l)
    b = text2(l)
    c = text3(l)
    cs = []  # 生成纵坐标
    for i in l:
        c = l.count(i)
        cs.append(c)
    print(cs)
    plt.plot(l, cs, "r")
    plt.plot(a, cs, "g")
    plt.plot(b, cs, "b")
    plt.show()
