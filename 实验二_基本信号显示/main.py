import matplotlib.pyplot as plt
import numpy as np

# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)  # 0到3pi之间间隔均匀的取100个数
y = np.sin(x)  # y=sin(x)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.subplot(1, 2, 1)  # 一行二列的第一张图片
plt.title(r'$f(x)=sin(x)$')  # 图片标题
plt.plot(x, y)  # 绘制图像

x1 = [t * 0.375 * np.pi for t in x]  # 创建x行的数据 x=0.375*pi*t
y1 = np.sin(x1)  # 创建y行的数据 y=sin(x)
plt.subplot(1, 2, 2)  # 一行二列的第二张图片
plt.title(u"测试2")  # 注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$')  # 图片标题
plt.plot(x, y1)  # 绘制图像
plt.show()  # 展示图片

